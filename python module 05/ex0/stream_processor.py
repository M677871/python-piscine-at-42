from abc import ABC, abstractmethod
from typing import Any, Lisr, Dict, Union, Optional

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