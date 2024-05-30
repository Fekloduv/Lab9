from abc import ABC, abstractmethod

class ConfigException(Exception):
    def __init__(self, message):
        super().__init__(message)
        # Логирование ошибки
        with open('error.log', 'a') as log_file:
            log_file.write(f"{message}\n")