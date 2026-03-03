from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


def is_text_like(value: Any) -> bool:
    try:
        _ = value.strip()
        _ = value.split()
        return True
    except AttributeError:
        return False


def is_list_like(value: Any) -> bool:
    try:
        _ = value.append
        return True
    except AttributeError:
        return False


def count_iter(items: Any) -> int:
    c: int = 0
    for _ in items:
        c += 1
    return c


def sum_numbers(values: Any) -> Union[int, float]:
    total: Union[int, float] = 0
    for v in values:
        total += v
    return total


def avg_numbers(total: Union[int, float], count: int) -> float:
    if count == 0:
        return 0.0
    return (total / count)


def validate_numeric_list(data: Any) -> bool:
    if not is_list_like(data):
        return False

    found = False
    for item in data:
        found = True
        try:
            _ = 0 + item
        except TypeError:
            return False

    return found


def validate_text(data: Any) -> bool:
    if not is_text_like(data):
        return False
    for _ in data:
        return True
    return False


def validate_log(data: Any) -> bool:
    if not is_text_like(data):
        return False
    if data.find(":") == -1:
        return False
    return True


def parse_log_entry(text: str) -> tuple[str, str]:
    parts = list[str] = text.split(":", 1)
    level: str = parts[0].strip().upper()
    message: str = parts[1].strip()
    if not message or not level:
        raise ValueError("Invalid log entry")
    return level, message


def print_processing_data(data: Any) -> None:
    """to match the suject display: string with quotes, other normally"""
    if is_text_like(data):
        print(f'Processing data: "{data}"')
    else:
        print(f"Processing data: {data}")


class DataProcessor(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return "Output: " + result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        return validate_numeric_list(data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError(
                    "NumericProcessor expects a non-empty list of numbers"
                )

            count: int = count_iter(data)
            total: Union[int, float] = sum_numbers(data)
            avg: float = avg_numbers(total, count)

            return (
                "Processed " + f"{count}" +
                " numeric values, sum=" + f"{total}" +
                ", avg=" + f"{avg}"
            )
        except (TypeError, ValueError) as exc:
            return "Numeric processing failed: " + f"{exc}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        return validate_text(data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("TextProcessor expects a non-empty string")

            chars: int = count_iter(data)
            words: int = count_iter(data.split())

            return (
                "Processed text: " + f"{chars}" +
                " characters, " + f"{words}" + " words"
            )
        except (TypeError, ValueError) as exc:
            return "Text processing failed: " + f"{exc}"


class LogProcessor(DataProcessor):
    LEVEL_PREFIXES: Dict[str, str] = {
        "ERROR": "[ALERT]",
        "WARNING": "[WARN]",
        "WARN": "[WARN]",
        "INFO": "[INFO]",
        "DEBUG": "[DEBUG]",
    }

    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        return validate_log(data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError(
                    "LogProcessor expects 'LEVEL: message' format"
                )

            level, message = parse_log_entry(data)
            prefix: str = self.LEVEL_PREFIXES.get(level, "[INFO]")

            if level == "ERROR":
                return prefix + " ERROR level detected: " + message
            return prefix + " " + level + " level detected: " + message
        except (TypeError, ValueError) as exc:
            return "Log processing failed: " + f"{exc}"


def print_header() -> None:
    print("=== CODE NEXUS- DATA PROCESSOR FOUNDATION ===")


def demo_one(proc: DataProcessor, data: Any, ok_msg: str) -> None:
    print(f"Initializing {proc.name} ...")
    print_processing_data(data)

    if proc.validate(data):
        print(f"Validation: {ok_msg}")
    else:
        print("Validation: Invalid data")

    result = proc.process(data)
    print(proc.format_output(result))


def demo_polymorphism() -> None:
    print("=== Polymorphic Processing Demo ===")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    inputs: List[Any] = [[1, 2, 3], "Hello Nexus!", "INFO: System ready"]
    i: int = 0
    for proc in processors:
        data = inputs[i]
        out = proc.process(data)
        print("Result " + f"{i + 1}" + ": " + out)
        i += 1


def main() -> None:
    print_header()
    demo_one(NumericProcessor(), [1, 2, 3, 4, 5], "Numeric data verified")
    demo_one(TextProcessor(), "Hello Nexus World", "Text data verified")
    demo_one(LogProcessor(), "ERROR: Connection timeout", "Log entry verified")
    demo_polymorphism()


if __name__ == "__main__":
    main()
