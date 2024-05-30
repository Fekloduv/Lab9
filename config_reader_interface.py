from abc import ABC, abstractmethod

class ConfigReaderInterface(ABC):
    @abstractmethod
    def read_config(self, filepath):
        pass