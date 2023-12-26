from abc import ABC


class CourseDescriptor:
    """
    CourseDescriptor - это класс дескриптора. Дескрипторы позволяют определять поведение атрибутов класса.
    В данном случае, CourseDescriptor контролирует доступ к атрибуту _courses.

    :param None: Параметры для инициализации не требуются.
    :type None: None
    """

    def __get__(self, instance, owner):
        """
        Метод __get__ вызывается при доступе к атрибуту. В данном случае, он возвращает значение _courses.

        :param instance: Экземпляр, через который был получен доступ к атрибуту.
        :type instance: Currency
        :param owner: Класс-владелец.
        :type owner: type
        :return: _courses класса-владельца.
        :rtype: dict
        """
        return owner._courses

    def __set__(self, instance, value):
        """
        Метод __set__ вызывается при изменении атрибута. В данном случае, он проверяет тип нового значения.
        Если значение является словарем, оно присваивается _courses.
        Если значение является числом, все курсы в _courses обновляются этим числом.
        Если значение не является ни словарем, ни числом, вызывается исключение TypeError.

        :param instance: Экземпляр, через который был получен доступ к атрибуту.
        :type instance: Currency
        :param value: Новое значение для атрибута.
        :type value: Union[dict, int, float]
        :raises TypeError: Если значение не является словарем или числом.
        """
        if isinstance(value, dict):
            instance.__class__._courses = value
        elif isinstance(value, (int, float)):
            for key in instance.__class__._courses:
                instance.__class__._courses[key] = value
        else:
            raise TypeError("courses must be a dictionary or a number")


class Currency(ABC):
    """
    Currency - это абстрактный базовый класс (ABC) для валют.
    Определяет общие атрибуты и методы, которые должны быть в каждом классе валюты.

    :param None: Параметры для инициализации не требуются.
    :type None: None
    """
    # _courses - это приватный атрибут класса, который хранит курсы валют.
    # Значениями являются курсы валют, а ключами - символы валют.
    _courses = {"$": 1.2, "₽": 60, "€": 1}

    # courses - это дескриптор, который контролирует доступ к _courses.
    # При обращении к courses вызывается метод __get__ дескриптора, который возвращает значение _courses.
    # При установке значения courses вызывается метод __set__ дескриптора, который обновляет _courses.
    courses = CourseDescriptor()

    # Конструктор класса принимает один аргумент - количество валюты.
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        """
        __str__ - это специальный метод, который возвращает строковое представление объекта.
        В данном случае, он возвращает количество валюты и символ валюты.

        :return: Строковое представление объекта в формате "количество символ".
        :rtype: str
        """
        return f"{self.amount} {self.symbol}"

    def to(self, other_currency):
        """
        to - это метод, который конвертирует данную валюту в другую валюту.
        Он принимает класс валюты в качестве аргумента и возвращает новый экземпляр этого класса.
        Конвертация производится на основе курсов валют, хранящихся в _courses.

        :param other_currency: Класс валюты, в которую нужно конвертировать.
        :type other_currency: type
        :return: Новый экземпляр класса other_currency.
        :rtype: other_currency
        """
        ratio = self.courses[other_currency.symbol] / self.courses[self.symbol]
        return other_currency(self.amount * ratio)

    def __gt__(self, other):
        """
        __gt__ - это специальный метод, который определяет поведение оператора >.
        В данном случае, он сравнивает количество валюты данного объекта с количеством валюты другого объекта.

        :param other: Объект, с которым сравнивается данный объект.
        :type other: Currency
        :return: True, если количество валюты данного объекта больше, иначе False.
        :rtype: bool
        """
        return self.amount > other.amount

    def __add__(self, other):
        """
        __add__ - это специальный метод, который определяет поведение оператора +.
        В данном случае, он конвертирует другую валюту в данную валюту и складывает их количество.

        :param other: Объект, который нужно добавить к данному объекту.
        :type other: Currency
        :return: Новый экземпляр класса с суммой количества валют.
        :rtype: type(self)
        """
        if isinstance(other, Currency):
            other = other.to(type(self))
        return self.__class__(self.amount + other.amount)

    def __sub__(self, other):
        """
        Вычитание валют.
        Args:
            other (Currency): Другая валюта.

        Returns:
            Currency: Результат вычитания валют.
        """
        return type(self)(self.amount - other.to(type(self)).amount)

    def __mul__(self, number):
        """
        Умножение валюты на число.

        Args:
            number (float): Число для умножения.

        Returns:
            Currency: Результат умножения валюты на число.
        """
        return type(self)(self.amount * number)

    def __truediv__(self, number):
        """
        Деление валюты на число.

        Args:
            number (int): Число для деления.

        Returns:
            Currency: Результат деления валюты на число.
        """
        return type(self)(self.amount / number)

    def __eq__(self, other):
        """
        Сравнение валют по сумме.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если суммы равны, иначе False.
        """
        return self.amount == other.to(type(self)).amount

    def __lt__(self, other):
        """
        Сравнение валют: меньше чем.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если данная валюта меньше другой, иначе False.
        """
        return self.amount < other.to(type(self)).amount

    def __gt__(self, other):
        """
        Сравнение валют: больше чем.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если данная валюта больше другой по сумме, иначе False.
        """
        return self.amount > other.to(type(self)).amount

    def __le__(self, other):
        """
        Сравнение валют: меньше или равно.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если данная валюта меньше или равна другой по сумме, иначе False.
        """
        return self.amount <= other.to(type(self)).amount

    def __ge__(self, other):
        """
        Сравнение валют: больше или равно.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если данная валюта больше или равна другой по сумме, иначе False.
        """
        return self.amount >= other.to(type(self)).amount


class Euro(Currency):
    symbol = "€"
    currency = "Euro"


class Dollar(Currency):
    symbol = "$"


class Ruble(Currency):
    symbol = "₽"


e = Euro(5)
print(e)
# 5 €
print(e.to(Dollar))
# 6 $
print(sum([Euro(i).amount for i in range(5)]))
# #10 €
print(e > Euro(6))
# False
print(e + Dollar(10))
# #13 €
print(Dollar(10) + e)
# 16 $
print(Euro.courses[Dollar.symbol])
Euro.courses[Dollar.symbol] = 2
print(Euro.courses[Dollar.symbol])
