from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    def __init__(self) -> None:
        self.processor_name: str = self.__class__.__name__

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return a result string."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""

    def format_output(self, result: str) -> str:
        """Format the output string with a standard prefix."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized for lists of numeric values."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Check that data is a non-empty list of numbers."""
        if not isinstance(data, list) or not data:
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        """Compute count, sum, and average of numeric list."""
        if not self.validate(data):
            raise ValueError(
                "NumericProcessor expects a non-empty list of numbers"
            )
        count: int = len(data)
        total: Union[int, float] = sum(data)
        avg: float = total / count
        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Processor specialized for text strings."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Check that data is a non-empty string."""
        return isinstance(data, str) and len(data) > 0

    def process(self, data: Any) -> str:
        """Count characters and words in the text."""
        if not self.validate(data):
            raise ValueError(
                "TextProcessor expects a non-empty string"
            )
        char_count: int = len(data)
        word_count: int = len(data.split())
        return (
            f"Processed text: {char_count} characters, "
            f"{word_count} words"
        )


class LogProcessor(DataProcessor):
    """Processor specialized for log entries (LEVEL: message)."""

    LEVEL_PREFIXES: Dict[str, str] = {
        "ERROR": "[ALERT]",
        "WARN": "[WARN]",
        "WARNING": "[WARN]",
        "INFO": "[INFO]",
        "DEBUG": "[DEBUG]",
    }

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Check that data is a log string with a colon separator."""
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        """Parse log level and message, apply appropriate prefix."""
        if not self.validate(data):
            raise ValueError(
                "LogProcessor expects 'LEVEL: message' format"
            )
        level: str
        message: str
        level, message = self._parse_entry(data)
        prefix: str = self.LEVEL_PREFIXES.get(level, "[INFO]")
        return f"{prefix} {level} level detected: {message}"

    def _parse_entry(self, data: str) -> tuple:
        """Split a log entry into level and message components."""
        parts: List[str] = data.split(":", 1)
        return parts[0].strip().upper(), parts[1].strip()


# Helper functions for the demo


def _format_data_display(data: Any) -> str:
    """Format data for display (double-quotes for strings)."""
    if isinstance(data, str):
        return f'"{data}"'
    return repr(data)


def _validation_label(processor: DataProcessor) -> str:
    """Return a human-readable validation label per processor."""
    labels: Dict[str, str] = {
        "NumericProcessor": "Numeric data verified",
        "TextProcessor": "Text data verified",
        "LogProcessor": "Log entry verified",
    }
    return labels.get(processor.processor_name, "Data verified")


def _init_label(processor: DataProcessor) -> str:
    """Return a human-readable initialisation label."""
    labels: Dict[str, str] = {
        "NumericProcessor": "Numeric",
        "TextProcessor": "Text",
        "LogProcessor": "Log",
    }
    return labels.get(processor.processor_name, "Data")


def _demonstrate_individual(
    processors: List[DataProcessor],
    inputs: List[Any],
) -> None:
    """Show each processor handling its specific data type."""
    for processor, data in zip(processors, inputs):
        print(f"\nInitializing {_init_label(processor)} Processor...")
        print(f"Processing data: {_format_data_display(data)}")
        print(f"Validation: {_validation_label(processor)}")
        try:
            result: str = processor.process(data)
            print(processor.format_output(result))
        except (TypeError, ValueError) as exc:
            print(processor.format_output(f"[ERROR] {exc}"))


def _demonstrate_polymorphism(
    processors: List[DataProcessor],
    inputs: List[Any],
) -> None:
    """Process mixed data types through the same interface."""
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    for idx, (proc, data) in enumerate(zip(processors, inputs), 1):
        try:
            result: str = proc.process(data)
            print(f"Result {idx}: {result}")
        except (TypeError, ValueError) as exc:
            print(f"Result {idx}: [ERROR] {exc}")


def main() -> None:
    """Entry point – demonstrates the Data Processor Foundation."""
    print("=== CODE NEXUS- DATA PROCESSOR FOUNDATION ===")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    inputs: List[Any] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout",
    ]
    _demonstrate_individual(processors, inputs)

    poly_processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    poly_inputs: List[Any] = [
        [1, 2, 3],
        "Hello Nexus!",
        "INFO: System ready",
    ]
    _demonstrate_polymorphism(poly_processors, poly_inputs)

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
