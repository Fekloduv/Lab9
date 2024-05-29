from abc import ABC, abstractmethod


class ConfigException(Exception):
    def __init__(self, message):
        super().__init__(message)
        # Логирование ошибки
        with open('error.log', 'a') as log_file:
            log_file.write(f"{message}\n")

class FileReaderInterface(ABC):
    @abstractmethod
    def read_file(self, buffer_size):
        pass


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


class ConfigReaderInterface(ABC):
    @abstractmethod
    def read_config(self, filepath):
        pass


class MyConfigReader(ConfigReaderInterface):
    def read_config(self, filepath):
        config = {}
        try:
            with open(filepath, 'r') as file:
                for line in file:
                    name, value = line.strip().split('=')
                    config[name.strip()] = value.strip()
            return config
        except ValueError as e:
            raise ConfigException(f"Ошибка форматирования в конфигурационном файле: {str(e)}")
        except FileNotFoundError as e:
            raise ConfigException(f"Файл конфигурации не найден: {str(e)}")
        except Exception as e:
            raise ConfigException(f"Неизвестная ошибка при чтении конфигурационного файла: {str(e)}")


class CoderInterface(ABC):
    @abstractmethod
    def run(self, text, option):
        pass


class Coder(CoderInterface):
    def __init__(self):
        self.key = "Python"

    def _cipher(self, text, key, encode=True):
        result = []
        key = key.lower()
        key_len = len(key)
        key_indexes = [ord(k) - ord('a') for k in key]

        for i, char in enumerate(text):
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                key_index = key_indexes[i % key_len]
                if not encode:
                    key_index = -key_index
                new_char = chr((ord(char) - offset + key_index) % 26 + offset)
                result.append(new_char)
            else:
                result.append(char)
        return ''.join(result)

    def run(self, text, option):
        if option not in ["code", "decode"]:
            raise ConfigException(f"Некорректная опция кодирования: {option}")
        return self._cipher(text, self.key, encode=(option == "code"))


class MainClass:
    def __init__(self, config_reader: ConfigReaderInterface, file_reader: FileReaderInterface, coder: CoderInterface):
        self.config_reader = config_reader
        self.file_reader = file_reader
        self.coder = coder

    def run(self, config_path):
        config = self.config_reader.read_config(config_path)
        buffer_size = int(config.get('buffer_size'))
        file_name = config.get('file_name')
        coder_option = config.get('coder_option')

        file_reader = MyFileReader(file_name)
        data = ''
        for chunk in file_reader.read_file(buffer_size):
            data += chunk

        result = self.coder.run(data, coder_option)

        # Вывод результата
        print(result)

if __name__ == "__main__":
    config_path = "config.txt"  # Замените на путь к вашему конфигурационному файлу

    # Создание объектов классов
    config_reader = MyConfigReader()
    coder = Coder()
    file_reader = MyFileReader("input.txt")  # Замените на путь к вашему входному файлу

    # Создание и запуск главного класса
    main_class = MainClass(config_reader, file_reader, coder)
    main_class.run(config_path)
