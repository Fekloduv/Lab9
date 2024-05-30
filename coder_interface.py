from abc import ABC, abstractmethod

class CoderInterface(ABC):
    @abstractmethod
    def run(self, text, option):
        pass