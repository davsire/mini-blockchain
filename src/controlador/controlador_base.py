from abc import ABC, abstractmethod
from typing import Any


class ControladorBase(ABC):
    @abstractmethod
    def executar(self) -> Any:
        pass
