from abc import ABC, abstractmethod
from typing import Any


Number = int | float
NumericData = Number | list[Number]
TextData = str | list[str]
LogEntry = dict[str, str]
LogData = LogEntry | list[LogEntry]


def _is_number(value: Any) -> bool:
    return type(value) is int or type(value) is float


def _is_numeric_list(data: Any) -> bool:
    if not isinstance(data, list):
        return False
    for item in data:
        if not _is_number(item):
            return False
    return True


def _is_text_list(data: Any) -> bool:
    if not isinstance(data, list):
        return False
    for item in data:
        if not isinstance(item, str):
            return False
    return True


def _is_log_entry(data: Any) -> bool:
    if not isinstance(data, dict):
        return False
    for key, value in data.items():
        if not isinstance(key, str) or not isinstance(value, str):
            return False
    return True


def _is_log_list(data: Any) -> bool:
    if not isinstance(data, list):
        return False
    for item in data:
        if not _is_log_entry(item):
            return False
    return True


def _format_log_entry(entry: LogEntry) -> str:
    if "log_level" in entry and "log_message" in entry:
        return f"{entry['log_level']}: {entry['log_message']}"

    parts: list[str] = []
    for key, value in entry.items():
        parts.append(f"{key}={value}")
    return ", ".join(parts)


class DataProcessor(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._data: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No processed data available")
        return self._data.pop(0)

    def _store(self, value: str) -> None:
        self._data.append((self._next_rank, value))
        self._next_rank += 1


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        return _is_number(data) or _is_numeric_list(data)

    def ingest(self, data: NumericData) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) or _is_text_list(data)

    def ingest(self, data: TextData) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        return _is_log_entry(data) or _is_log_list(data)

    def ingest(self, data: LogData) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for entry in data:
                self._store(_format_log_entry(entry))
        else:
            self._store(_format_log_entry(data))


def _print_validation(processor: DataProcessor, data: Any) -> None:
    print(f"Trying to validate input {data!r}: {processor.validate(data)}")


def _extract_values(
    processor: DataProcessor,
    label: str,
    count: int,
) -> None:
    for _ in range(count):
        rank, value = processor.output()
        print(f"{label} {rank}: {value}")


def _test_numeric_processor() -> None:
    processor = NumericProcessor()

    print("Testing Numeric Processor...")
    _print_validation(processor, 42)
    _print_validation(processor, "Hello")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        processor.ingest("foo")
    except ValueError as exc:
        print(f"Got exception: {exc}")

    data: list[Number] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    processor.ingest(data)
    print("Extracting 3 values...")
    _extract_values(processor, "Numeric value", 3)


def _test_text_processor() -> None:
    processor = TextProcessor()

    print("Testing Text Processor...")
    _print_validation(processor, 42)
    data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {data}")
    processor.ingest(data)
    print("Extracting 1 value...")
    _extract_values(processor, "Text value", 1)


def _test_log_processor() -> None:
    processor = LogProcessor()

    print("Testing Log Processor...")
    _print_validation(processor, "Hello")
    data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {data}")
    processor.ingest(data)
    print("Extracting 2 values...")
    _extract_values(processor, "Log entry", 2)


def main() -> None:
    print("=== Code Nexus- Data Processor ===")
    _test_numeric_processor()
    _test_text_processor()
    _test_log_processor()


if __name__ == "__main__":
    main()
