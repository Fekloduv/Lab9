from file_reader_interface import FileReaderInterface
from config_exception import ConfigException

class MyFileReader(FileReaderInterface):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self, buffer_size):
        if buffer_size <= 0:
            raise ConfigException("Размер буфера должен быть положительным числом.")
        try:
            with open(self.file_path, 'r') as file:
                while True:
                    chunk = file.read(buffer_size)
                    if not chunk:
                        break
                    yield chunk
        except Exception as e:
            raise ConfigException(f"Ошибка при чтении файла: {str(e)}")