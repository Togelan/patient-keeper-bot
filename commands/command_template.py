from abc import ABC, abstractmethod


class CommandTemplate(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

