def fabric(lambda_func):
    """
    Фабрика декораторов.

    :param lambda_func: функция, которая будет применена к результату работы декорируемой функции
    :type lambda_func: function
    :return: декоратор
    :rtype: function
    """
    def repeat_decorator(func1):
        """
        Принимает декорируемый декоратор.

        :param func1: декорируемый декоратор
        :type func1: function
        :return: декоратор с аргументами
        :rtype: function
        """
        def repeat_decorator_args(*func1_args, **func1_kwargs):
            """
            Принимает аргументы декорируемого декоратора.

            :param func1_args: позиционные аргументы декорируемого декоратора
            :type func1_args: tuple
            :param func1_kwargs: именованные аргументы декорируемого декоратора
            :type func1_kwargs: dict
            :return: декоратор функции
            :rtype: function
            """
            def foo_decorator(func2):
                """
                Принимает декорируемую функцию.

                :param func2: декорируемая функция
                :type func2: function
                :return: декоратор с аргументами функции
                :rtype: function
                """
                def foo_decorator_args(*foo_args, **foo_kwargs):
                    """
                    Принимает аргументы декорируемой функции.

                    :param foo_args: позиционные аргументы декорируемой функции
                    :type foo_args: tuple
                    :param foo_kwargs: именованные аргументы декорируемой функции
                    :type foo_kwargs: dict
                    :return: результат работы декоратора
                    :rtype: any
                    """
                    if fabric.enabled:
                        return lambda_func(func1(*func1_args)(func2)(*foo_args))
                    return lambda_func((func2)(*foo_args))
                return foo_decorator_args
            return foo_decorator
        return repeat_decorator_args
    return repeat_decorator


fabric.enabled = True
fabric.off = lambda: fabric.__setattr__('enabled', False)
fabric.on = lambda: fabric.__setattr__('enabled', True)

# @fabric(lambda x: x**2)


def repeat(times):
    """
    Повторить вызов times раз, и вернуть среднее значение.

    :param times: количество повторений вызова функции
    :type times: int
    :return: декоратор
    :rtype: function
    """
    def inner(func):
        def wrapper(*args, **kwargs):
            result = 0
            for _ in range(times):
                result += func()
            return result/times
        return wrapper
    return inner


repeat = fabric(lambda x: x**2)(repeat)


# @repeat(3)
def foo(*args, **kwargs):
    """
    Функция, которая работает... и все (может принимать на вход любые параметры).

    :param args: позиционные аргументы
    :type args: tuple
    :param kwargs: именованные аргументы
    :type kwargs: dict
    :return: число 4
    :rtype: int
    """
    print("Foo called!")
    return 4


foo = repeat(3)(foo)

print(foo(1, 3, 5))
fabric.off()
print(foo(1, 3, 5))
fabric.on()
print(foo(1, 3, 5))
fabric.off()
print(foo(1, 3, 5))
fabric.on()
print(foo(1, 3, 5))
