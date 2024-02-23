import datetime

class ErrorLogger:
    """
    Класс ErrorLogger реализует контекстный менеджер для логирования ошибок в файл.

    Attributes:
        logfile (str): Путь к файлу для записи информации об ошибках.
    """

    def __init__(self, logfile):
        """
        Инициализация экземпляра класса ErrorLogger.

        Args:
            logfile (str): Путь к файлу для записи информации об ошибках.
        """
        self.logfile = logfile

    def __enter__(self):
        """
        Метод входа в контекстный менеджер.
        Отрабатывает при обращении к экземпляру класса
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Метод выхода из контекстного менеджера.
        Отрабатывает всегда при выходе из контекстного менеджера (где заканчивается блок with...), даже если случилась ошибка
        Args:
            exc_type: Тип возникшего исключения.
            exc_value: Значение исключения.
            traceback: Стек вызовов исключения.

        Returns:
            bool: True, если исключение обработано, False для "прокидывания" ошибки выше.
        """
        if exc_type is not None:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.logfile, 'a') as f:
                f.write(f"Error occurred at {current_datetime}:\n")
                f.write(f"Error type: {exc_type}\n")
                f.write(f"Error message: {exc_value}\n\n")
            return False  # "Прокидываем" ошибку выше
        return True

logfile = "homework\\9_context_manager-DB\\error_log.txt"

# with ErrorLogger(logfile):
#         # Код, который может вызвать ошибку
#     try: 
#         1 / 0  # Генерация исключения деления на ноль
#     except Exception as e:
#         raise e  # "Прокидываем" ошибку выше


# Пример использования контекстного менеджера
with ErrorLogger(logfile):
    # Код, который может вызвать ошибку
    try:
        for i in 1:
            print(i)  # Попытка итерировать неитерируемый объект
    except Exception as e:
        raise e  # "Прокидываем" ошибку выше