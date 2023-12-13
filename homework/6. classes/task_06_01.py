import random


class Matrix:
    def __init__(self, rows, cols=None):
        """
        Инициализация объекта Matrix.
        :param rows: int или список списков int
        :param cols: int
        """
        if isinstance(rows, int):  # Если rows - это целое число
            self.rows = rows  # Устанавливаем количество строк
            self.cols = cols  # Устанавливаем количество столбцов
            # Создаем матрицу с случайными числами от 1 до 10
            self.matrix = [
                [random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
        else:  # Если rows - это список списков
            self.matrix = rows  # Устанавливаем матрицу
            self.rows = len(rows)  # Устанавливаем количество строк
            self.cols = len(rows[0])  # Устанавливаем количество столбцов

    def __str__(self):
        matrix_str = '\n'.join(
            ['\t'.join([str(cell) for cell in row]) for row in self.matrix])
        return matrix_str

    def __add__(self, other):
        """
        Сложение двух матриц.

        :param other: Matrix
        :return: Matrix
        """
        if self.rows != other.rows or self.cols != other.cols:  # Если размерности матриц не совпадают
            # Вызываем исключение
            raise ValueError("Размерности матриц не совпадают.")
        # Возвращаем новую матрицу, которая является результатом сложения двух матриц
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        """
        Вычитание двух матриц.

        :param other: Matrix
        :return: Matrix
        """
        if self.rows != other.rows or self.cols != other.cols:  # Если размерности матриц не совпадают
            # Вызываем исключение
            raise ValueError("Размерности матриц не совпадают.")
        # Возвращаем новую матрицу, которая является результатом вычитания двух матриц
        return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __mul__(self, other):
        """
        Умножение двух матриц или матрицы на скаляр.

        :param other: Matrix или int
        :return: Matrix
        """
        if isinstance(other, Matrix):  # Если other - это матрица
            if self.cols != other.rows:  # Если количество столбцов первой матрицы не равно количеству строк второй матрицы
                # Вызываем исключение
                raise ValueError("Размерности матриц не совпадают.")
            # Возвращаем новую матрицу, которая является результатом умножения двух матриц
            return Matrix([[sum(a*b for a, b in zip(self_row, other_col)) for other_col in zip(*other.matrix)] for self_row in self.matrix])
        else:  # Если other - это скаляр
            # Возвращаем новую матрицу, которая является результатом умножения матрицы на скаляр
            return Matrix([[self.matrix[i][j] * other for j in range(self.cols)] for i in range(self.rows)])

    def transpose(self):
        """
        Транспонирование матрицы.

        :return: Matrix
        """
        # Возвращаем новую матрицу, которая является транспонированной исходной матрицы
        return Matrix([[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)])

    def __eq__(self, other):
        """
        Проверка равенства двух матриц.

        :param other: Matrix
        :return: bool
        """
        if self.rows != other.rows or self.cols != other.cols:  # Если размерности матриц не совпадают
            return False  # Возвращаем False
        # Возвращаем True, если все соответствующие элементы двух матриц равны
        return all(self.matrix[i][j] == other.matrix[i][j] for i in range(self.rows) for j in range(self.cols))

    def is_squared(self):
        """
        Проверка, является ли матрица квадратной.

        :return: bool
        """
        return self.rows == self.cols  # Возвращаем True, если количество строк равно количеству столбцов

    def is_symmetric(self):
        """
        Проверка, является ли матрица симметричной.

        :return: bool
        """
        if not self.is_squared():  # Если матрица не квадратная
            return False  # Возвращаем False
        # Возвращаем True, если элементы матрицы, отраженные относительно главной диагонали, равны
        return all(self.matrix[i][j] == self.matrix[j][i] for i in range(self.rows) for j in range(self.cols))


a = Matrix(2, 2)  # generate random matrix
b = Matrix([[1, 2], [3, 4]])  # concreate matrix
c = a * b
print(c)
# [[4, 5],
# [6, 7]]
print(c.is_squared())
# True
