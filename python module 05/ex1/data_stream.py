from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class with core streaming functionality."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = "Generic"
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a result summary."""

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter data based on criteria. Default returns all."""
        if criteria is None:
            return list(data_batch)
        return list(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):
    """Stream handler for environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings and compute averages."""
        self._validate_batch(data_batch)
        self.processed_count += len(data_batch)
        avg_temp: Optional[float] = self._compute_avg_temp(data_batch)
        base: str = f"{len(data_batch)} readings processed"
        if avg_temp is not None:
            return f"{base}, avg temp: {avg_temp}\u00b0C"
        return base

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter sensor data; 'critical' keeps values above 30."""
        if criteria == "critical":
            return [
                d for d in data_batch
                if isinstance(d, dict) and d.get("value", 0) > 30
            ]
        return list(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor-specific statistics."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["sensor_type"] = "environmental"
        return stats

    def _validate_batch(self, data_batch: List[Any]) -> None:
        """Raise if the batch is empty."""
        if not data_batch:
            raise ValueError("Empty sensor batch")

    def _compute_avg_temp(
        self, data_batch: List[Any],
    ) -> Optional[float]:
        """Compute average of temperature readings in the batch."""
        temps: List[float] = [
            d["value"] for d in data_batch
            if isinstance(d, dict) and d.get("type") == "temp"
        ]
        if not temps:
            return None
        return sum(temps) / len(temps)


class TransactionStream(DataStream):
    """Stream handler for financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transactions and compute net flow."""
        self._validate_batch(data_batch)
        self.processed_count += len(data_batch)
        net: float = self._compute_net_flow(data_batch)
        sign: str = "+" if net >= 0 else ""
        return (
            f"{len(data_batch)} operations, "
            f"net flow: {sign}{int(net)} units"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter transactions; 'large' keeps amounts above 100."""
        if criteria == "large":
            return [
                d for d in data_batch
                if isinstance(d, dict) and d.get("amount", 0) > 100
            ]
        return list(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction-specific statistics."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["domain"] = "financial"
        return stats

    def _validate_batch(self, data_batch: List[Any]) -> None:
        """Raise if the batch is empty."""
        if not data_batch:
            raise ValueError("Empty transaction batch")

    def _compute_net_flow(self, data_batch: List[Any]) -> float:
        """Calculate net flow: buys add, sells subtract."""
        flow: float = 0.0
        for txn in data_batch:
            if not isinstance(txn, dict):
                continue
            amount: float = float(txn.get("amount", 0))
            action: str = txn.get("action", "")
            if action == "buy":
                flow += amount
            elif action == "sell":
                flow -= amount
        return flow


class EventStream(DataStream):
    """Stream handler for system event data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process events and count errors."""
        self._validate_batch(data_batch)
        self.processed_count += len(data_batch)
        error_count: int = self._count_errors(data_batch)
        label: str = "error" if error_count == 1 else "errors"
        return (
            f"{len(data_batch)} events, "
            f"{error_count} {label} detected"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter events; 'error' keeps only error events."""
        if criteria == "error":
            return [
                e for e in data_batch
                if isinstance(e, str) and "error" in e.lower()
            ]
        return list(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event-specific statistics."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["domain"] = "system_events"
        return stats

    def _validate_batch(self, data_batch: List[Any]) -> None:
        """Raise if the batch is empty."""
        if not data_batch:
            raise ValueError("Empty event batch")

    def _count_errors(self, data_batch: List[Any]) -> int:
        """Count items that contain 'error'."""
        return sum(
            1 for e in data_batch
            if isinstance(e, str) and "error" in e.lower()
        )


class StreamProcessor:
    """Manages multiple stream types and processes them polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a data stream for processing."""
        self.streams.append(stream)

    def process_all(
        self, batches: Dict[str, List[Any]],
    ) -> List[str]:
        """Process data batches for every registered stream."""
        results: List[str] = []
        for stream in self.streams:
            batch: Optional[List[Any]] = batches.get(stream.stream_id)
            if batch is None:
                continue
            try:
                result: str = stream.process_batch(batch)
                results.append(result)
            except (ValueError, TypeError) as exc:
                results.append(f"[ERROR] {exc}")
        return results

    def get_all_stats(
        self,
    ) -> List[Dict[str, Union[str, int, float]]]:
        """Collect statistics from all registered streams."""
        return [stream.get_stats() for stream in self.streams]


# ── Display helpers ────────────────────────────────────────────


def _fmt_sensor(batch: List[Dict[str, Any]]) -> str:
    """Format sensor batch for human-readable display."""
    items: List[str] = [
        f"{d.get('type', '?')}:{d.get('value', '?')}"
        for d in batch
    ]
    return f"[{', '.join(items)}]"


def _fmt_transaction(batch: List[Dict[str, Any]]) -> str:
    """Format transaction batch for display."""
    items: List[str] = [
        f"{d.get('action', '?')}:{d.get('amount', '?')}"
        for d in batch
    ]
    return f"[{', '.join(items)}]"


def _fmt_events(batch: List[str]) -> str:
    """Format event batch for display."""
    return f"[{', '.join(batch)}]"


# ── Demo functions ─────────────────────────────────────────────


def _demo_individual_streams() -> None:
    """Demonstrate each stream type processing its own data."""
    sensor: SensorStream = SensorStream("SENSOR_001")
    sensor_data: List[Dict[str, Any]] = [
        {"type": "temp", "value": 22.5},
        {"type": "humidity", "value": 65},
        {"type": "pressure", "value": 1013},
    ]
    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: {_fmt_sensor(sensor_data)}")
    print(f"Sensor analysis: {sensor.process_batch(sensor_data)}")

    trans: TransactionStream = TransactionStream("TRANS_001")
    trans_data: List[Dict[str, Any]] = [
        {"action": "buy", "amount": 100},
        {"action": "sell", "amount": 150},
        {"action": "buy", "amount": 75},
    ]
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print(
        f"Processing transaction batch: "
        f"{_fmt_transaction(trans_data)}"
    )
    print(f"Transaction analysis: {trans.process_batch(trans_data)}")

    event: EventStream = EventStream("EVENT_001")
    event_data: List[str] = ["login", "error", "logout"]
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(f"Processing event batch: {_fmt_events(event_data)}")
    print(f"Event analysis: {event.process_batch(event_data)}")


def _demo_polymorphic_processing() -> None:
    """Demonstrate unified processing of mixed stream types."""
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor: StreamProcessor = StreamProcessor()
    sensor: SensorStream = SensorStream("SENSOR_002")
    trans: TransactionStream = TransactionStream("TRANS_002")
    event: EventStream = EventStream("EVENT_002")

    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    batches: Dict[str, List[Any]] = {
        "SENSOR_002": [
            {"type": "temp", "value": 25.0},
            {"type": "temp", "value": 30.0},
        ],
        "TRANS_002": [
            {"action": "buy", "amount": 200},
            {"action": "sell", "amount": 50},
            {"action": "buy", "amount": 100},
            {"action": "sell", "amount": 75},
        ],
        "EVENT_002": ["login", "error", "logout"],
    }

    results: List[str] = processor.process_all(batches)
    _print_batch_results(results)
    _demo_filtering(sensor, trans)


def _print_batch_results(results: List[str]) -> None:
    """Print batch processing results with stream labels."""
    labels: List[str] = [
        "Sensor data", "Transaction data", "Event data",
    ]
    print("Batch 1 Results:")
    for label, result in zip(labels, results):
        print(f"- {label}: {result}")


def _demo_filtering(
    sensor: SensorStream,
    trans: TransactionStream,
) -> None:
    """Demonstrate stream filtering with priority criteria."""
    print("\nStream filtering active: High-priority data only")
    sensor_critical: List[Any] = sensor.filter_data(
        [
            {"type": "temp", "value": 35.0},
            {"type": "temp", "value": 40.0},
            {"type": "temp", "value": 20.0},
        ],
        criteria="critical",
    )
    trans_large: List[Any] = trans.filter_data(
        [
            {"action": "buy", "amount": 500},
            {"action": "sell", "amount": 50},
        ],
        criteria="large",
    )
    print(
        f"Filtered results: {len(sensor_critical)} critical sensor "
        f"alerts, {len(trans_large)} large transaction"
    )


def main() -> None:
    """Entry point for the Polymorphic Stream System."""
    print("=== CODE NEXUS- POLYMORPHIC STREAM SYSTEM ===")
    _demo_individual_streams()
    _demo_polymorphic_processing()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
