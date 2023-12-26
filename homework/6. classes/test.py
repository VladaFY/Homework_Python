from abc import ABC

class Course:
    course = {'₽': 60, '$': 1.2, '€': 1}


    def __set_name__(self, owner, name):
        # print(self.__class__)
        # print(self.__dict__)
        print(f'вызов публичного метода __set_name__ c параметром name = {name}')
        print(f'вызов публичного метода __set_name__ c параметром owner = {owner}\n')
        self.name = '_' + name
        # print(self.__dict__)


    def __set__(self, instance, value):
        print(f'вызов публичного метода __set__ c параметром instance = {instance}')
        print(f'вызов публичного метода __set__ c параметром value = {value}\n')
        
        if isinstance(value, dict):
            setattr(type(self), self.name, value)
        else:
            getattr(type(self), self.name)[instance.currency] = value


    def __get__(self, instance, owner):
        print(f'вызов публичного метода __get__ c параметром instance = {instance}')
        print(f'вызов публичного метода __get__ c параметром owner = {owner}')
        print(f'вызов публичного метода __get__ c параметром self = {self}')
        print(f'вызов публичного метода __get__ c использованием self.name = {self.name}\n')

        if instance is None:
            print('instance is None')
            return lambda currency_class: self.course[currency_class.currency]
        if not hasattr(type(self), self.name):
            print('not hasattr(type(self), self.name)')
            # print(self.__dict__)
            setattr(type(self), self.name, self.course)
            # print('self.__dict__')
            # print(self.__dict__)
        return getattr(type(self), self.name)
    
class Currency(ABC):
    """
    Currency - это абстрактный базовый класс (ABC) для валют.
    Определяет общие атрибуты и методы, которые должны быть в каждом классе валюты.

    :param amount: Сколько денег
    :type float: float
    """
    # courses - это атрибут класса, который хранит курсы валют.
    # Значениями являются курсы валют, а ключами - символы валют.
    # courses = {"$": 1.2, "₽": 60, "€": 1}
    courses = Course()



    # Конструктор класса принимает один аргумент - количество валюты.
    def __init__(self, amount):
        print(f'вызов публичного метода __init__ c присвоением self.amount = {amount}')
        self.amount = amount

    def __str__(self):
        """
        __str__ - это специальный метод, который возвращает строковое представление объекта.
        В данном случае, он возвращает количество валюты и символ валюты.

        :return: Строковое представление объекта в формате "количество символ".
        :rtype: str
        """
        print('вызов приватного метода __str__')
        # print(self.__class__)
        # print(self.__class__.__name__)
        # print(self.__dict__)
        # print(self.__dir__)
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
        print('вызов приватного метода to')
        # print(f'other_currency.symbol: {other_currency.symbol}')
        # print(f'self.symbol: {self.symbol}')
        ratio = self.courses[other_currency.symbol] / self.courses[self.symbol]
        # print(f'ratio: {ratio}')
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
        print('вызов приватного метода __add__')
        if isinstance(other, Currency):
            other = other.to(type(self))
        return type(self)(int(self.amount + other.amount))


class Euro(Currency):
    symbol = "€"
    currency = "Euro"


class Dollar(Currency):
    symbol = "$"


class Ruble(Currency):
    symbol = "₽"

e = Euro(5)
# print(e)
# e1 = Euro(10)
# print(e1)
# print(e + e1)
# print(e.to(Dollar))
# # 6 $
# print(sum([Euro(i).amount for i in range(5)]))
# print(e > Euro(6))
# print(e + Dollar(10))
# print(Dollar(10) + e)

print(Euro.courses)

# print(Euro.courses(Dollar))
# print(Euro.courses[Dollar.symbol])
# Euro.courses[Dollar.symbol] = 2

# print(Euro.courses(Dollar))
# print(Euro.courses)

# print(e.to(Dollar))
# print(Dollar.symbol)