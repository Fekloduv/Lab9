from abc import ABC, abstractmethod

class FileReaderInterface(ABC):
    @abstractmethod
    def read_file(self, buffer_size):
        pass