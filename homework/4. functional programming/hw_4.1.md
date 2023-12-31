# Задание 4.1 - Фабрика декораторов

Необходимо написать фабрику декораторов (также декоратор).
Фабрика (функция) принимает аргумент - функцию (lambda).
Возвращает декоратор, который должен вызывать функцию (lambda) с аргументом - результатом декорируемого декоратора.

Пример:

```python
def fabric(lambda_func):
    """Фабрика декоратор"""
    
    pass # Здесь необходимо реализовать код декоратора fabric


@fabric(lambda x: x ** 2)
def repeat(times):
    """Повторить вызов times раз, и вернуть среднее значение"""
    pass # Здесь необходимо реализовать код декоратора repeat


@repeat(3)
def foo(*args, **kwargs):
    """Функция которая работает... и все (может принимать на вход любые параметры)"""
    print("Foo called!")
    return 4 # К этому значению далее применяется lambda функция (аргумент для fabric)

>>> print('Ожидаемый результат')
Ожидаемый результат
>>> foo(1, 3, 5)
Foo called!
Foo called!
Foo called!
16
>> fabric.off()
>> foo([1, 3, 5])
Foo called!
16
```

## Дополнительно

1. Красивый, читаемый код ("Всегда пишите код так, будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете." — Martin Golding).
2. Документирование функций обязательно. Используем стиль документации Sphinx.
3. Реализуемый декоратор (фабрика) должен иметь функции для включения/отключения декоратора. При выключении - декорируемый декоратор не отрабатывает (в примере выше, функция не будет вызываться times раз), но сам декоратор(фабрика) работает - т.е. вызывается lambda на результат работы функции.
4. Иметь в виду, что функции и декораторы могут быть различными.
5. Ориентироваться на пользователя, который может использовать декоратор как угодно, с различными параметрами.
