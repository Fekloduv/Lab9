from file_reader_interface import FileReaderInterface
from config_exception import ConfigException

class MyFileReader(FileReaderInterface):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self, buffer_size):
        if buffer_size <= 0:
            raise ConfigException("Размер буфера должен быть положительным числом.")
        if not self.file_path.is_file():
            raise ConfigException(f"Файл {self.file_path} не существует.")
        try:
            with self.file_path.open('r') as file:
                while True:
                    chunk = file.read(buffer_size)
                    if not chunk:
                        break
                    yield chunk
        except Exception as e:
            raise ConfigException(f"Ошибка при чтении файла: {str(e)}")
