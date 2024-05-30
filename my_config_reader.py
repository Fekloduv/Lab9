from config_reader_interface import ConfigReaderInterface
from config_exception import ConfigException

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