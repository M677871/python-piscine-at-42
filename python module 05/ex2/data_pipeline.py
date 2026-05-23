from abc import ABC, abstractmethod
from typing import Any, Protocol


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


def _csv_escape(value: str) -> str:
    escaped = ""
    needs_quotes = False

    for char in value:
        if char == '"':
            escaped += '""'
            needs_quotes = True
        else:
            escaped += char

        if char == "," or char == "\n" or char == "\r":
            needs_quotes = True

    if needs_quotes:
        return f'"{escaped}"'
    return escaped


def _json_escape(value: str) -> str:
    escaped = ""

    for char in value:
        code = ord(char)
        if char == "\\":
            escaped += "\\\\"
        elif char == '"':
            escaped += '\\"'
        elif char == "\b":
            escaped += "\\b"
        elif char == "\f":
            escaped += "\\f"
        elif char == "\n":
            escaped += "\\n"
        elif char == "\r":
            escaped += "\\r"
        elif char == "\t":
            escaped += "\\t"
        elif code < 32:
            digits = hex(code)[2:]
            escaped += "\\u" + "0" * (4 - len(digits)) + digits
        else:
            escaped += char

    return escaped


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

    def total_processed(self) -> int:
        return self._next_rank

    def remaining(self) -> int:
        return len(self._data)


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []
        for _, value in data:
            values.append(_csv_escape(value))

        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items: list[str] = []
        for rank, value in data:
            items.append(f'"item_{rank}": "{_json_escape(value)}"')

        print("JSON Output:")
        print("{" + ", ".join(items) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processor = self._find_processor(element)
            if processor is None:
                print(
                    "DataStream error- Can't process element in stream: "
                    f"{element}"
                )
                continue

            try:
                processor.ingest(element)
            except Exception as exc:
                print(
                    "DataStream error- Processor failed to ingest element "
                    f"{element}: {exc}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb < 0:
            raise ValueError("Number of elements to export cannot be negative")

        for processor in self._processors:
            exported: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    exported.append(processor.output())
                except IndexError:
                    break

            if exported:
                plugin.process_output(exported)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            print(
                f"{processor.name}: total "
                f"{processor.total_processed()} items processed, remaining "
                f"{processor.remaining()} on processor"
            )

    def _find_processor(self, element: Any) -> DataProcessor | None:
        for processor in self._processors:
            try:
                if processor.validate(element):
                    return processor
            except Exception as exc:
                print(
                    "DataStream error- Processor validation failed for "
                    f"{element}: {exc}"
                )
        return None


def _build_first_batch() -> list[Any]:
    return [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]


def _build_second_batch() -> list[Any]:
    return [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]


def main() -> None:
    print("=== Code Nexus- Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    first_batch = _build_first_batch()
    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    second_batch = _build_second_batch()
    print(f"Send another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
