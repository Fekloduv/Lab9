from coder_interface import CoderInterface
from config_exception import ConfigException

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
