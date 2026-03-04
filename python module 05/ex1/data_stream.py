from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Tuple


def copy_list(items: List[Any]) -> List[Any]:
    out: List[Any] = []
    for x in items:
        out.append(x)
    return out


def count_list(items: List[Any]) -> int:
    c: int = 0
    for _ in items:
        c += 1
    return c


def safe_is_dict(x: Any) -> bool:
    return isinstance(x, dict)


def safe_is_str(x: Any) -> bool:
    return isinstance(x, str)


def dict_value(d: Dict[str, Any], key: str, default: Any) -> Any:
    return d.get(key, default)


def is_number(x: Any) -> bool:
    try:
        _ = 0 + x
        return True
    except TypeError:
        return False


def add_numbers(total: Union[int, float], x: Union[int, float]) -> Union[int, float]:
    return total + x


def avg_numbers(total: Union[int, float], n: int) -> Optional[float]:
    if n == 0:
        return None
    return total / n


def abs_number(x: Union[int, float]) -> Union[int, float]:
    if x < 0:
        return -x
    return x


def contains_error(text: str) -> bool:
    return "error" in text.lower()


def format_sensor_batch(batch: List[Any]) -> str:
    s: str = "["
    first: bool = True
    for item in batch:
        if safe_is_dict(item):
            t = dict_value(item, "type", "?")
            v = dict_value(item, "value", "?")
            if not first:
                s += ", "
            s += f"{t}:{v}"
            first = False
    s += "]"
    return s


def format_transaction_batch(batch: List[Any]) -> str:
    s: str = "["
    first: bool = True
    for item in batch:
        if safe_is_dict(item):
            act = dict_value(item, "action", "?")
            amt = dict_value(item, "amount", "?")
            if not first:
                s += ", "
            s += f"{act}:{amt}"
            first = False
    s += "]"
    return s


def format_event_batch(batch: List[Any]) -> str:
    s: str = "["
    first: bool = True
    for item in batch:
        if safe_is_str(item):
            if not first:
                s += ", "
            s += item
            first = False
    s += "]"
    return s


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = "Generic"
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        _ = criteria
        return copy_list(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self._validate_non_empty(data_batch)

        n = count_list(data_batch)
        self.processed_count += n

        avg_temp = self._avg_temp(data_batch)
        base = f"{n} readings processed"
        if avg_temp is None:
            return base
        return f"{base}, avg temp: {avg_temp}°C"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            out: List[Any] = []
            for item in data_batch:
                if safe_is_dict(item):
                    v = dict_value(item, "value", 0)
                    if is_number(v) and v > 30:
                        out.append(item)
            return out
        return copy_list(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["sensor_type"] = "environmental"
        return stats

    def _validate_non_empty(self, data_batch: List[Any]) -> None:
        for _ in data_batch:
            return
        raise ValueError("Empty sensor batch")

    def _avg_temp(self, data_batch: List[Any]) -> Optional[float]:
        total: Union[int, float] = 0
        c: int = 0
        for item in data_batch:
            if safe_is_dict(item):
                t = dict_value(item, "type", "")
                v = dict_value(item, "value", 0)
                if t == "temp" and is_number(v):
                    total = add_numbers(total, v)
                    c += 1
        return avg_numbers(total, c)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self._validate_non_empty(data_batch)

        n = count_list(data_batch)
        self.processed_count += n

        net, actions_found = self._net_flow_if_possible(data_batch)
        if not actions_found:
            return f"{n} operations processed"

        sign = "+"
        if net < 0:
            sign = "-"
        return f"{n} operations, net flow: {sign}{abs_number(net)} units"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            out: List[Any] = []
            for item in data_batch:
                if safe_is_dict(item):
                    amt = dict_value(item, "amount", 0)
                    if is_number(amt) and amt > 100:
                        out.append(item)
            return out
        return copy_list(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["domain"] = "financial"
        return stats

    def _validate_non_empty(self, data_batch: List[Any]) -> None:
        for _ in data_batch:
            return
        raise ValueError("Empty transaction batch")

    def _net_flow_if_possible(self, data_batch: List[Any]) -> Tuple[Union[int, float], bool]:
        flow: Union[int, float] = 0
        found_action: bool = False

        for item in data_batch:
            if safe_is_dict(item):
                action = dict_value(item, "action", "")
                amount = dict_value(item, "amount", 0)
                if (action == "buy" or action == "sell") and is_number(amount):
                    found_action = True
                    if action == "buy":
                        flow = add_numbers(flow, amount)
                    else:
                        flow = add_numbers(flow, -amount)

        return flow, found_action


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        self._validate_non_empty(data_batch)

        n = count_list(data_batch)
        self.processed_count += n

        errors = self._count_errors(data_batch)
        if errors == 0:
            return f"{n} events processed"

        label = "error"
        if errors != 1:
            label = "errors"
        return f"{n} events, {errors} {label} detected"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == "error":
            out: List[Any] = []
            for item in data_batch:
                if safe_is_str(item) and contains_error(item):
                    out.append(item)
            return out
        return copy_list(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["domain"] = "system_events"
        return stats

    def _validate_non_empty(self, data_batch: List[Any]) -> None:
        for _ in data_batch:
            return
        raise ValueError("Empty event batch")

    def _count_errors(self, data_batch: List[Any]) -> int:
        c: int = 0
        for item in data_batch:
            if safe_is_str(item) and contains_error(item):
                c += 1
        return c


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> List[str]:
        results: List[str] = []
        for stream in self.streams:
            if stream.stream_id in batches:
                batch = batches[stream.stream_id]
                try:
                    results.append(stream.process_batch(batch))
                except (ValueError, TypeError) as exc:
                    results.append(f"[ERROR] {exc}")
        return results


def demo_individual() -> None:
    sensor = SensorStream("SENSOR_001")
    sensor_data: List[Any] = [
        {"type": "temp", "value": 22.5},
        {"type": "humidity", "value": 65},
        {"type": "pressure", "value": 1013}
    ]

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: {format_sensor_batch(sensor_data)}")
    print(f"Sensor analysis: {sensor.process_batch(sensor_data)}")

    trans = TransactionStream("TRANS_001")
    trans_data: List[Any] = [
        {"action": "buy", "amount": 100},
        {"action": "sell", "amount": 150},
        {"action": "buy", "amount": 75}
    ]

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print(f"Processing transaction batch: {format_transaction_batch(trans_data)}")
    print(f"Transaction analysis: {trans.process_batch(trans_data)}")

    event = EventStream("EVENT_001")
    event_data: List[Any] = ["login", "error", "logout"]

    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(f"Processing event batch: {format_event_batch(event_data)}")
    print(f"Event analysis: {event.process_batch(event_data)}")


def print_batch_results(results: List[str]) -> None:
    print("Batch 1 Results:")
    print(f"- Sensor data: {results[0]}")
    print(f"- Transaction data: {results[1]}")
    print(f"- Event data: {results[2]}")


def demo_polymorphic() -> None:
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    sensor = SensorStream("SENSOR_002")
    trans = TransactionStream("TRANS_002")
    event = EventStream("EVENT_002")

    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    batches: Dict[str, List[Any]] = {
        "SENSOR_002": [
            {"type": "humidity", "value": 60},
            {"type": "pressure", "value": 1012}
        ],
        "TRANS_002": [
            {"amount": 200},
            {"amount": 50},
            {"amount": 100},
            {"amount": 75}
        ],
        "EVENT_002": ["login", "update", "logout"]
    }

    results = processor.process_all(batches)
    print_batch_results(results)

    print("Stream filtering active: High-priority data only")
    sensor_critical = sensor.filter_data(
        [
            {"type": "temp", "value": 35.0},
            {"type": "temp", "value": 40.0},
            {"type": "temp", "value": 20.0},
        ],
        criteria="critical",
    )
    trans_large = trans.filter_data(
        [
            {"action": "buy", "amount": 500},
            {"action": "sell", "amount": 50},
        ],
        criteria="large",
    )
    print(
        f"Filtered results: {count_list(sensor_critical)} critical sensor alerts, "
        f"{count_list(trans_large)} large transaction"
    )


def main() -> None:
    print("=== CODE NEXUS- POLYMORPHIC STREAM SYSTEM ===")
    demo_individual()
    demo_polymorphic()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
