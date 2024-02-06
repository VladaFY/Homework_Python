def myzip(*args):
    iterators = [iter(iterable) for iterable in args]  # Создаем итераторы для каждого аргумента
    while True:
        elements = []
        for iterator in iterators:
            try:
                element = next(iterator)  # Получаем следующий элемент из итератора
                elements.append(element)
            except StopIteration:  # Если итератор исчерпан, удаляем его из списка итераторов
                iterators.remove(iterator)
        if not elements:  # Если список элементов пуст, значит все итераторы исчерпаны, выходим из цикла
            break
        yield from elements  # Возвращаем элементы из списка
        

# Пример использования
result = list(myzip(['A', 'B', 'C'], [1, 2, 3]))
print(result)  # ['A', 1, 'B', 2, 'C', 3]

result = list(myzip('!', ['A', 'B', 'C', 'D'], range(1, 3)))
print(result)  # ['!', 'A', 1, 'B', 2, 'C', 'D']


