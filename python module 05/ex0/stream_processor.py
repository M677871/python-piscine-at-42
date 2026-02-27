from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

Number = Union[int, float]

class DataProcessor(ABC):
    def __init__(self) -> None:
        self.processor_name: str = self.__class__.__name__

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(str, data:Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output from {self.processor_name}: {result}"
    

class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()


    def validate(str, data) -> bool:
        if not isinstance(data, str):
            return False
        for _ in data:
            return True
        return False


    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("TestProcessor expects a non-empty string.")
        text: str = data
        chars: int = self.ft_strlen(text)
        words: int = self.count_words(text)
        return f"Processed text: {chars} characters, {words} words"


    def ft_strlen(self, s: str) -> int:
        lenght: int = 0
        for _ in s:
            lenght += 1
        return lenght


    def count_words(self, s: str) -> int:
        whitespace: str = " \t\n\r\f\v"
        count: int = 0
        in_word: bool = False
        for ch in s:
            if ch in whitespace:
                in_word = False
            else:
                if not in_word:
                    count += 1
                    in_word = True
        return count


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        return self._all_numbers(data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("NumericProcessor expects a list of numbers")

        values: List[Number] = data
        count: int = self._count_items(values)
        if count == 0:
            raise ValueError("NumericProcessor expects a non-empty list of numbers")

        total: Number = self._sum_items(values)
        avg: float = self._average(total, count)
        return f"Processed {count} numeric values, sum={total}, avg={avg}"


    def _all_numbers(self, values: List[Any]) -> bool:
        for x in values:
            if not isinstance(x, (int, float)):
                return False
        return True

    def _count_items(self, values: List[Number]) -> int:
        c: int = 0
        for _ in values:
            c += 1
        return c

    def _sum_items(self, values: List[Number]) -> Number:
        total: Number = 0
        for x in values:
            total = total + x
        return total

    def _average(self, total: Number, count: int) -> float:
        return float(total) / float(count)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self._level_prefix: Dict[str, str] = {
            "ERROR": "[ALERT]",
            "WARN": "[WARN]",
            "WARNING": "[WARN]",
            "INFO": "[INFO]",
        }

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        for ch in data:
            if ch == ":":
                return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("LogProcessor expects a string like 'LEVEL: message'")

        line: str = data
        level_raw, message_raw = self._split_level_message(line)

        level: str = self._to_upper(self._trim_spaces(level_raw))
        message: str = self._trim_spaces(message_raw)

        if not self._has_any_char(level) or not self._has_any_char(message):
            raise ValueError("Invalid log format (needs LEVEL: message)")

        prefix: str = self._prefix_for_level(level)
        return f"{prefix} {level} level detected: {message}"

    def _split_level_message(self, line: str) -> tuple[str, str]:
        level_chars: List[str] = []
        message_chars: List[str] = []
        seen_colon: bool = False

        for ch in line:
            if not seen_colon:
                if ch == ":":
                    seen_colon = True
                else:
                    level_chars.append(ch)
            else:
                message_chars.append(ch)

        if not seen_colon:
            raise ValueError("Invalid log format (missing ':')")

        return self._join_chars(level_chars), self._join_chars(message_chars)

    def _join_chars(self, chars: List[str]) -> str:
        out: str = ""
        for ch in chars:
            out = out + ch
        return out

    def _trim_spaces(self, text: str) -> str:
        whitespace: str = " \t\n\r\v\f"
        start: int = 0
        end: int = 0
        idx: int = 0
        last_index: int = -1

        for _ in text:
            last_index += 1

        # left trim
        for ch in text:
            if ch in whitespace:
                start += 1
            else:
                break

        # right trim
        end = last_index
        if last_index >= 0:
            i: int = 0
            # walk to end again to allow reverse-like indexing without len()
            chars: List[str] = []
            for ch in text:
                chars.append(ch)
                i += 1
            while end >= start and chars[end] in whitespace:
                end -= 1
            return self._slice_chars(chars, start, end)

        return ""

    def _slice_chars(self, chars: List[str], start: int, end: int) -> str:
        out: str = ""
        i: int = 0
        for ch in chars:
            if i >= start and i <= end:
                out = out + ch
            i += 1
        return out

    def _to_upper(self, text: str) -> str:
        # use built-in upper()
        return text.upper()

    def _has_any_char(self, text: str) -> bool:
        for _ in text:
            return True
        return False

    def _prefix_for_level(self, level: str) -> str:
        # avoid dict.get() if you want ultra-basic
        for k in self._level_prefix:
            if k == level:
                return self._level_prefix[k]
        return "[INFO]"


def main() -> None:
    print("=== CODE NEXUS- DATA PROCESSOR FOUNDATION ===")

    processors: List[DataProcessor] = [NumericProcessor(), TextProcessor(), LogProcessor()]
    inputs: List[Any] = [[1, 2, 3, 4, 5], "Hello Nexus World", "ERROR: Connection timeout"]

    for p, d in zip(processors, inputs):
        print(f"Processing data: {d!r}")
        print(f"Validation: {p.validate(d)}")
        try:
            result: str = p.process(d)
            print(p.format_output(result))
        except (TypeError, ValueError) as exc:
            print(p.format_output(f"[ERROR] {exc}"))

    print("=== Polymorphic Processing Demo ===")
    mixed_processors: List[DataProcessor] = [NumericProcessor(), TextProcessor(), LogProcessor()]
    mixed_inputs: List[Any] = [[1, 2, 3], "Hello Nexus", "INFO: System ready"]

    idx: int = 1
    for p, d in zip(mixed_processors, mixed_inputs):
        try:
            result = p.process(d)
            print(f"Result {idx}: {result}")
        except (TypeError, ValueError) as exc:
            print(f"Result {idx}: [ERROR] {exc}")
        idx += 1

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()