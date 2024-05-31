from my_config_reader import MyConfigReader
from my_file_reader import MyFileReader
from coder import Coder
import tempfile
class MainClass:
    def __init__(self, config_reader, file_reader, coder):
        self.config_reader = config_reader
        self.file_reader = file_reader
        self.coder = coder

    def run(self, config_path):
        config = self.config_reader.read_config(config_path)
        buffer_size = int(config.get('buffer_size'))
        file_name = config.get('file_name')
        coder_option = config.get('coder_option')

        file_reader = MyFileReader(file_name)
        # Используем временный файл для аккумулирования данных
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            for chunk in file_reader.read_file(buffer_size):
                temp_file.write(chunk)
            temp_file.seek(0)
            data = temp_file.read()

        result = self.coder.run(data, coder_option)

        # Вывод результата
        print(result)

if __name__ == "__main__":
    config_path = "config.txt"

    # Создание объектов классов
    config_reader = MyConfigReader()
    coder = Coder()
    file_reader = MyFileReader("input.txt")

    # Создание и запуск главного класса
    main_class = MainClass(config_reader, file_reader, coder)
    main_class.run(config_path)
