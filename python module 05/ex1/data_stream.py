from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional



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


def format_batch(batch: List[Any]) -> str:
    # Output: [temp:22.5, humidity:65, pressure:1013]
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


def format_event_batch(batch: List[Any]) -> str:
    # Output: [login, error, logout]
    s: str = "["
    first: bool = True
    for item in batch:
        if safe_is_str(item):
            if not first:
                s += ", "
            s += item
            first = False
    return s


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = "Generic"
        self.processed_count: int = 0


    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]) -> List[Any]:
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
        return avg_numbers(total, v)



class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self._validate_non_empty(data_batch)

        n = count_list(data_batch)
        self.processed_count += n

        # If the batch includes buy/sell actions, compute net flow; otherwise generic summary.
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

    def _net_flow_if_possible(self, data_batch: List[Any]) -> (Union[int, float], bool):
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

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        out: List[Dict[str, Union[str, int, float]]] = []
        for s in self.streams:
            out.append(s.get_stats())
        return out


def demo_individual() -> None:
    sensor = SensorStream("SENSOR_001")
    sensor_data: List[Any] = [
        {"type": "temp", "value": 22.5},
        {"type": "humidity", "value": 65},
        {"type": "pressure", "value": 1013}
    ]

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"processing sensor batch: {format_batch(sensor_data)}")
    print(f"Sensor analysis: {sensor.process_batch(sensor_data)}")

    trans = TransactionStream("TRANS_001")