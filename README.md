Иванов Анатолий Павлович 5030102/10401

Цель работы

Целью данной лабораторной работы является разработка программной системы, которая считывает конфигурационные данные из файла, читает данные из другого файла с заданным размером буфера, и выполняет кодирование или декодирование этих данных с использованием заданного ключа.

Описание классов и их функциональности

ConfigException

Назначение: Класс исключения для ошибок, связанных с конфигурацией.

Функциональность: Логирует сообщения об ошибках в файл error.log.

FileReaderInterface

Назначение: Абстрактный базовый класс для чтения файлов.

Функциональность: Определяет абстрактный метод read_file.

MyFileReader

Назначение: Реализация интерфейса для чтения файлов.

Функциональность: Читает файл по частям с заданным размером буфера и генерирует их.

ConfigReaderInterface

Назначение: Абстрактный базовый класс для чтения конфигурационных файлов.

Функциональность: Определяет абстрактный метод read_config.

MyConfigReader

Назначение: Реализация интерфейса для чтения конфигурационных файлов.

Функциональность: Читает конфигурационный файл, парсит его и возвращает словарь с конфигурацией.

CoderInterface
Назначение: Абстрактный базовый класс для кодирования/декодирования текста.

Функциональность: Определяет абстрактный метод run.

Coder
Назначение: Реализация интерфейса для кодирования/декодирования текста.

Функциональность: Использует шифр Цезаря с заданным ключом для кодирования или декодирования текста.

MainClass
Назначение: Главный класс, управляющий процессом чтения конфигурации, чтения файла и кодирования/декодирования.

Функциональность: Запрашивает путь к конфигурационному файлу, читает конфигурацию, использует её для чтения файла и кодирования/декодирования данных.

Выводы
В результате выполнения лабораторной работы была разработана программная система, которая успешно считывает конфигурационные данные, читает файлы с заданным размером буфера и выполняет кодирование или декодирование текста. Система демонстрирует использование принципов ООП, таких как абстракция, наследование и полиморфизм, а также обработку исключений для управления ошибками.
