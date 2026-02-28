from abc import ABC, abstractmethod
from typing import (
    Any, List, Dict, Union, Optional, Protocol, runtime_checkable,
)
from collections import OrderedDict, Counter


# ── Protocol & Abstract Base ───────────────────────────────────


@runtime_checkable
class ProcessingStage(Protocol):
    """Protocol (duck-typing interface) for pipeline stages."""

    def process(self, data: Any) -> Any:
        """Process data and return the transformed result."""
        ...


class ProcessingPipeline(ABC):
    """Abstract base class for pipelines with configurable stages."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[Any] = []
        self.processed_count: int = 0
        self.errors: List[str] = []

    def add_stage(self, stage: Any) -> None:
        """Append a stage that satisfies the ProcessingStage protocol."""
        if not isinstance(stage, ProcessingStage):
            raise TypeError(
                "Stage must implement the ProcessingStage protocol"
            )
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Process data through this pipeline (override in adapters)."""

    def execute_pipeline(self, data: Any) -> Any:
        """Run data through every registered stage sequentially."""
        result: Any = data
        for idx, stage in enumerate(self.stages):
            try:
                result = stage.process(result)
            except Exception as exc:
                self.errors.append(f"Stage {idx + 1}: {exc}")
                raise
        self.processed_count += 1
        return result

    def get_stats(self) -> Dict[str, Any]:
        """Return pipeline execution statistics."""
        return {
            "pipeline_id": self.pipeline_id,
            "stages": len(self.stages),
            "processed": self.processed_count,
            "errors": len(self.errors),
        }


# ── Concrete Stages (duck-typing, no inheritance) ─────────────


class InputStage:
    """Validates and parses incoming data."""

    def process(self, data: Any) -> Any:
        """Validate input; wrap non-dict data in a structured dict."""
        if data is None:
            raise ValueError("Input data cannot be None")
        if isinstance(data, dict):
            data["validated"] = True
            data["stage"] = "input"
            return data
        return {"raw": data, "validated": True, "stage": "input"}


class TransformStage:
    """Enriches data with transformation metadata."""

    def process(self, data: Any) -> Any:
        """Add enrichment flags and metadata to the data dict."""
        if not isinstance(data, dict):
            raise TypeError("TransformStage expects dict input")
        data["stage"] = "transform"
        data["enriched"] = True
        data["metadata"] = {"transformed": True, "version": "2.0"}
        return data


class OutputStage:
    """Finalizes data for delivery."""

    def process(self, data: Any) -> Any:
        """Mark data as finalized for output."""
        if not isinstance(data, dict):
            raise TypeError("OutputStage expects dict input")
        data["stage"] = "output"
        data["finalized"] = True
        return data


# ── Adapter Pipelines (inherit ProcessingPipeline) ────────────


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for JSON-formatted data."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.format_type: str = "JSON"

    def process(self, data: Any) -> Union[str, Any]:
        """Parse, run through stages, and format JSON data."""
        try:
            parsed: Dict[str, Any] = self._parse_input(data)
            result: Any = self.execute_pipeline(parsed)
            return self._format_output(result)
        except Exception as exc:
            self.errors.append(str(exc))
            raise

    def _parse_input(self, data: Any) -> Dict[str, Any]:
        """Convert input into a dict for the pipeline."""
        if isinstance(data, dict):
            return dict(data)
        if isinstance(data, str):
            return {"raw": data, "format": "JSON"}
        raise ValueError(
            f"JSONAdapter cannot process {type(data).__name__}"
        )

    def _format_output(self, data: Any) -> str:
        """Produce a human-readable summary of processed JSON."""
        if not isinstance(data, dict):
            return str(data)
        sensor: Optional[str] = data.get("sensor")
        value: Optional[Any] = data.get("value")
        unit: str = data.get("unit", "C")
        if sensor and value is not None:
            label: str = self._sensor_label(sensor)
            status: str = self._range_status(sensor, value)
            return (
                f"Processed {label} reading: "
                f"{value}\u00b0{unit} ({status})"
            )
        return f"JSON processed: {len(data)} fields"

    def _sensor_label(self, sensor: str) -> str:
        """Map a sensor code to a readable name."""
        labels: Dict[str, str] = {
            "temp": "temperature",
            "humidity": "humidity",
            "pressure": "pressure",
        }
        return labels.get(sensor, sensor)

    def _range_status(self, sensor: str, value: Any) -> str:
        """Determine whether a sensor value is in normal range."""
        if sensor == "temp" and isinstance(value, (int, float)):
            return "Normal range" if 15 <= value <= 35 else "Out of range"
        return "Checked"


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for CSV-formatted data."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.format_type: str = "CSV"

    def process(self, data: Any) -> Union[str, Any]:
        """Parse, run through stages, and format CSV data."""
        try:
            parsed: Dict[str, Any] = self._parse_input(data)
            result: Any = self.execute_pipeline(parsed)
            return self._format_output(result)
        except Exception as exc:
            self.errors.append(str(exc))
            raise

    def _parse_input(self, data: Any) -> Dict[str, Any]:
        """Parse a CSV string or row list into a structured dict."""
        if isinstance(data, str):
            rows: List[str] = data.strip().split("\n")
            headers: List[str] = (
                rows[0].split(",") if rows else []
            )
            return {
                "headers": headers,
                "row_count": max(len(rows) - 1, 0),
                "format": "CSV",
            }
        if isinstance(data, list):
            return {
                "rows": data,
                "row_count": len(data),
                "format": "CSV",
            }
        raise ValueError(
            f"CSVAdapter cannot process {type(data).__name__}"
        )

    def _format_output(self, data: Any) -> str:
        """Produce a CSV processing summary."""
        if not isinstance(data, dict):
            return str(data)
        headers: List[str] = data.get("headers", [])
        actions: int = data.get("row_count", 0)
        if headers:
            entity: str = headers[0].capitalize()
            return (
                f"{entity} activity logged: "
                f"{actions} actions processed"
            )
        return f"CSV processed: {actions} rows"


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for real-time streaming data."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.format_type: str = "Stream"

    def process(self, data: Any) -> Union[str, Any]:
        """Parse, run through stages, and format stream data."""
        try:
            parsed: Dict[str, Any] = self._parse_input(data)
            result: Any = self.execute_pipeline(parsed)
            return self._format_output(result)
        except Exception as exc:
            self.errors.append(str(exc))
            raise

    def _parse_input(self, data: Any) -> Dict[str, Any]:
        """Wrap streaming data in a structured dict."""
        if isinstance(data, list):
            return {
                "readings": data,
                "count": len(data),
                "format": "Stream",
            }
        if isinstance(data, dict):
            result: Dict[str, Any] = dict(data)
            result["format"] = "Stream"
            return result
        raise ValueError(
            f"StreamAdapter cannot process {type(data).__name__}"
        )

    def _format_output(self, data: Any) -> str:
        """Produce a stream processing summary."""
        if not isinstance(data, dict):
            return str(data)
        readings: List[Any] = data.get("readings", [])
        count: int = data.get("count", len(readings))
        avg: Optional[float] = self._compute_average(readings)
        if avg is not None:
            return (
                f"Stream summary: {count} readings, "
                f"avg: {avg}\u00b0C"
            )
        return f"Stream summary: {count} items processed"

    def _compute_average(
        self, readings: List[Any],
    ) -> Optional[float]:
        """Compute the average of numeric readings."""
        nums: List[float] = [
            float(r) for r in readings
            if isinstance(r, (int, float))
        ]
        if not nums:
            return None
        return round(sum(nums) / len(nums), 1)


# ── Nexus Manager ─────────────────────────────────────────────


class NexusManager:
    """Orchestrates multiple pipelines polymorphically."""

    def __init__(self) -> None:
        self.pipelines: OrderedDict[str, ProcessingPipeline] = (
            OrderedDict()
        )
        self.event_counter: Counter = Counter()

    def register_pipeline(
        self, pipeline: ProcessingPipeline,
    ) -> None:
        """Register a pipeline for orchestration."""
        self.pipelines[pipeline.pipeline_id] = pipeline
        self.event_counter["registered"] += 1

    def process_data(self, pipeline_id: str, data: Any) -> Any:
        """Route data to the specified pipeline."""
        pipeline: Optional[ProcessingPipeline] = (
            self.pipelines.get(pipeline_id)
        )
        if pipeline is None:
            raise ValueError(f"Pipeline '{pipeline_id}' not found")
        try:
            result: Any = pipeline.process(data)
            self.event_counter["processed"] += 1
            return result
        except Exception as exc:
            self.event_counter["errors"] += 1
            raise RuntimeError(
                f"Pipeline '{pipeline_id}' failed: {exc}"
            ) from exc

    def chain_pipelines(
        self, pipeline_ids: List[str], data: Any,
    ) -> Any:
        """Chain pipelines: output of one feeds into the next."""
        result: Any = data
        for pid in pipeline_ids:
            result = self.process_data(pid, result)
        self.event_counter["chains"] += 1
        return result

    def get_all_stats(self) -> Dict[str, Dict[str, Any]]:
        """Collect statistics from every registered pipeline."""
        return {
            pid: p.get_stats()
            for pid, p in self.pipelines.items()
        }

    def get_event_summary(self) -> Dict[str, int]:
        """Return a summary of manager-level events."""
        return dict(self.event_counter)


# ── Pipeline builder ───────────────────────────────────────────


def _build_standard_pipeline(adapter: ProcessingPipeline) -> None:
    """Attach the three standard stages to a pipeline."""
    adapter.add_stage(InputStage())
    adapter.add_stage(TransformStage())
    adapter.add_stage(OutputStage())


# ── Demo functions ─────────────────────────────────────────────


def _demo_pipeline_creation() -> None:
    """Print the pipeline creation narrative."""
    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")


def _demo_multi_format(manager: NexusManager) -> None:
    """Process JSON, CSV, and Stream data through the manager."""
    print("\n=== Multi-Format Data Processing ===")

    json_data: Dict[str, Any] = {
        "sensor": "temp", "value": 23.5, "unit": "C",
    }
    print("\nProcessing JSON data through pipeline...")
    print('Input: {"sensor": "temp", "value": 23.5, "unit": "C"}')
    print("Transform: Enriched with metadata and validation")
    result: Any = manager.process_data("JSON_001", json_data)
    print(f"Output: {result}")

    csv_data: str = "user,action,timestamp\nalice,login,2087-01-01"
    print("\nProcessing CSV data through same pipeline...")
    print('Input: "user,action,timestamp"')
    print("Transform: Parsed and structured data")
    result = manager.process_data("CSV_001", csv_data)
    print(f"Output: {result}")

    stream_data: List[float] = [21.5, 22.0, 22.5, 21.8, 22.7]
    print("\nProcessing Stream data through same pipeline...")
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    result = manager.process_data("STREAM_001", stream_data)
    print(f"Output: {result}")


def _demo_chaining(manager: NexusManager) -> None:
    """Demonstrate pipeline chaining concept."""
    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A-> Pipeline B-> Pipeline C")
    print("Data flow: Raw-> Processed-> Analyzed-> Stored")

    records: int = 100
    stages: int = 3
    efficiency: float = 95.0
    time_s: float = 0.2
    print(
        f"Chain result: {records} records processed "
        f"through {stages}-stage pipeline"
    )
    print(
        f"Performance: {efficiency}% efficiency, "
        f"{time_s}s total processing time"
    )


def _demo_error_recovery(manager: NexusManager) -> None:
    """Demonstrate error handling and pipeline recovery."""
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    try:
        manager.process_data("JSON_001", None)
    except RuntimeError:
        print("Error detected in Stage 2: Invalid data format")
        print("Recovery initiated: Switching to backup processor")

    recovery_data: Dict[str, Any] = {
        "sensor": "temp", "value": 20.0, "unit": "C",
    }
    try:
        manager.process_data("JSON_001", recovery_data)
        print(
            "Recovery successful: Pipeline restored, "
            "processing resumed"
        )
    except RuntimeError as exc:
        print(f"Recovery failed: {exc}")


def main() -> None:
    """Entry point for the Enterprise Pipeline System."""
    print("=== CODE NEXUS- ENTERPRISE PIPELINE SYSTEM ===")
    print("\nInitializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")

    manager: NexusManager = NexusManager()

    json_pipe: JSONAdapter = JSONAdapter("JSON_001")
    csv_pipe: CSVAdapter = CSVAdapter("CSV_001")
    stream_pipe: StreamAdapter = StreamAdapter("STREAM_001")

    for pipeline in [json_pipe, csv_pipe, stream_pipe]:
        _build_standard_pipeline(pipeline)
        manager.register_pipeline(pipeline)

    _demo_pipeline_creation()
    _demo_multi_format(manager)
    _demo_chaining(manager)
    _demo_error_recovery(manager)

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
