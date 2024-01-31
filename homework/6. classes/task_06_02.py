from abc import ABC, abstractmethod

# courses = {"$": 1.2, "₽": 60, "€": 1}
courses = {"$": 0, "₽": 0, "€": 0}


class Curces_descriptor():
    """
    Curces_descriptor - это класс дескриптора. Дескрипторы позволяют определять поведение атрибутов класса.
    В данном случае, Curces_descriptor контролирует доступ к атрибуту _courses.

    :param None: Параметры для инициализации не требуются.
    :type None: None
    """

    def __set_name__(self, owner, name):
        """
        Магический метод. Вызывается при создании объекта класса Curces_descriptor. 
        Превращает переменную в приватную.

        :param owner: ссылка на класс Currency
        :type owner: Currency

        :param name: имя задаваемое атрибуту
        :type name: str

        :return: None
        """
        self.name = '_' + name

    def __get__(self, instance, owner):
        """
        Метод __get__ вызывается при доступе к атрибуту. В данном случае, он возвращает значение _courses.

        :param instance: Экземпляр, через который был получен доступ к атрибуту.
        Может быть равно None, если вызов геттера через объект класса, а не экземпляр класса
        :type instance: дочерние классы от Currency
        :param owner: Класс-владелец.
        :type owner: type
        :return: _courses класса-владельца.
        :rtype: dict
        """
        # print('Геттер')


        if instance:
            return instance.__dict__[self.name]
        return courses

    def __set__(self, instance, value):
        """
        Вызывается при инициализации дочерних классов Currency

        :param self: ссылается на объект класса Course
        :type self: Course

        :param instance: ссылается на объект класса Currency или его подкласс
        :type instance: Currency или его подкласс

        :param value: значение которое мы присваиваем
        :type value: str

        :return: None
        """
        # print('Сеттер')
        
        # Условие, которое определяет, в первый ли раз создается экземпляр класса. 
        # Значение вида "1.2$$" - попадает только из инита. Если при этом значение в словаре равно нулю,
        # значит ранее курс не устанавливался и не менялся, значит можно установить значение по умолчанию.
        # При создании последующих экземпляров класса - обновлять не нужно, т.к. это перезатрет значение курса, выставленное в ручну.
        if value[-2] == value[-1] and courses[value[-1]] == 0:
            courses[value[-1]] = float(value[:-2])
        elif value[-2] != value[-1]:
            courses[value[-1]] = float(value[:-1])

        instance.__dict__[self.name] = courses


class Currency(ABC):
    """
    Абстрактный класс для определния интерфейса

    """
    course = Curces_descriptor()


    @classmethod
    def classmethod(cls):
        """
        Метод-пустышка для демонстрации classmethod
        """
        print(cls.course)
        print('Class method called')

    @abstractmethod
    def currency(self):
        """
        Оболочка метода, который должен быть реализован в каждом подклассе.
        """
        pass

    def __init__(self, amount):
        self.amount = amount

    @staticmethod
    def check_value(value):
        """
        Проверяем, что передаваемый параметр является одним из подклассов
        """
        if not isinstance(value, (Euro, Dollar, Ruble)):
            return False
        return True

    def __str__(self):
        # при попытке получить self.course срабатывает геттер из дескриптора
        return f"{self.amount}{self.__class__.sign}"

    def to(self, target_currency):
        """
        Конвертировать в другую валюту
        
        :param name: ссылается на объект одного из классов валют
        
        :return: класс валюты в которую конвертируем
        """

        # нужно создать экземпляр класса, что бы в словаре courses установился курс по умолчанию для валюты.
        tg = target_currency(0)
        return target_currency((self.amount / self.course[self.__class__.sign]) * self.course[tg.sign])

    def __gt__(self, other):
        """
        Проверка на >
        
        :param other: ссылается на объект класса валюты
        
        :return: bool
        """
        return self.amount > other.to(self.__class__).amount

    def __add__(self, other):
        """
        Проверка на >=
        
        :param other: ссылается на объект класса валюты
        
        :return: bool
        """
        if isinstance(other, Currency):
            other = other.to(type(self))
        return self.__class__(self.amount + other.amount)

    def __sub__(self, other):
        """
        Вычитание двух объектов

        :param other: ссылается на объект класса валюты

        :return: класс валюты
        """
        self.check_value(other)
        return self.__class__(self.amount - other.to(self.__class__).amount)

    def __ge__(self, other):
        """
        Проверка на >=

        :param other: ссылается на объект класса валюты

        :return: bool
        """
        self.check_value(other)
        return self.amount >= other.to(self.__class__).amount

    def __truediv__(self, number):
        """
        Деление на число

        :param other: ссылается на объект класса валюты

        :return: float
        """
        return self.__class__(self.amount / number)

    def __mul__(self, number):
        """
        Умножение на число

        :param other: ссылается на объект класса валюты

        :return: int
        """
        return self.__class__(self.amount * number)


class Euro(Currency):
    sign = '€'

    def __init__(self, amount):
        super().__init__(amount)
        self.course = '1€€'  # здесь вызовется дескриптор, т.к у него приоритет выше чем у свойств атрибутов, а не создастся обычный атрибут course
        self.currency = 'Euro' # вызывается геттер от property. 

    # реализация абстрактного метода
    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, val):
        if val in ['Евро', 'Euro']:
            self.__currency = val
        else:
            print('Значение должно быть "Евро" или "Euro"')



class Dollar(Currency):
    sign = '$'

    def __init__(self, amount):
        super().__init__(amount)
        self.course = '1.2$$'
        self.currency = 'Dollar'

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, val):
        if val in ['Доллар', 'Dollar']:
            self.__currency = val
        else:
            print('Значение должно быть Доллар или Dollar')


class Ruble(Currency):
    sign = '₽'

    def __init__(self, amount):
        super().__init__(amount)
        self.course = '60₽₽'
        self.currency = 'Ruble'

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, val):
        if val in ['Рубль', 'Ruble']:
            self.__currency = val
        else:
            print('Значение должно быть Рубль или Ruble')


e = Euro(5)

print(e)
# 5 €
r = Ruble(1)
print(e.to(Dollar))
# #6 $
print(sum([Euro(i).amount for i in range(5)]))
# #10
print(e > Euro(6))
# #False
print(e + Dollar(10))
# #13 €
print(Dollar(10) + e)
# 16 $
print(e.course)
e.course = '2$'  # установили курс евро в два доллара
print(e.to(Dollar))
# #10 $
# print(Euro.course)
print(Euro.course[Dollar.sign])
# #2
print(Euro.course[Ruble.sign])
# #60
print(e.currency)
# #'Euro'
e.currency = 'Евро'
print(e.currency)
Currency.classmethod()

e.currency  = 'тест'
