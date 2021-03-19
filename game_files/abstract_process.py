from abc import ABCMeta, abstractmethod
from graphics.interface import interface as intr


class Process(metaclass=ABCMeta):
    interface = intr

    @abstractmethod
    def main_loop(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def process_events(self):
        pass
