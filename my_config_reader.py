from config_reader_interface import ConfigReaderInterface
from config_exception import ConfigException

class MyConfigReader(ConfigReaderInterface):
    def read_config(self, filepath):
        config_path = Path(filepath)
        if not config_path.is_file():
            raise ConfigException(f"Файл конфигурации {config_path} не существует.")
        config = {}
        try:
            with config_path.open('r') as file:
                for line in file:
                    name, value = line.strip().split('=')
                    config[name.strip()] = value.strip()
            buffer_size = config.get('buffer_size')
            if not buffer_size.isdigit() or int(buffer_size) <= 0:
                raise ConfigException("Некорректный размер буфера в конфигурационном файле.")
            return config
        except ValueError as e:
            raise ConfigException(f"Ошибка форматирования в конфигурационном файле: {str(e)}")
        except Exception as e:
            raise ConfigException(f"Неизвестная ошибка при чтении конфигурационного файла: {str(e)}")
