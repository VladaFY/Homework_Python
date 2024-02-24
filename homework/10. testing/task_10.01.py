import unittest
import sys
sys.path.append('C:/Users/vyuldasheva/Documents/Adaptation/dar-python-mentoring-master/homework/6_classes')

from task_6_1 import Matrix



class TestMatrix(unittest.TestCase):

    def test_add_positive(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 + matrix2
        self.assertEqual(result.matrix, [[6, 8], [10, 12]])

    def test_sub_positive(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 - matrix2
        self.assertEqual(result.matrix, [[-4, -4], [-4, -4]])

    def test_mul_positive(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 * matrix2
        self.assertEqual(result.matrix, [[19, 22], [43, 50]])
        
        matrix3 = Matrix([[1, 4], [-9, 100]])
        result_2 = matrix3 * 2       
        self.assertEqual(result_2.matrix, [[2, 8], [-18, 200]])


    def test_transpose_positive(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        result = matrix.transpose()
        self.assertEqual(result.matrix, [[1, 4], [2, 5], [3, 6]])

    def test_eq_positive(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[1, 2], [3, 4]])
        result = matrix1 == matrix2
        self.assertTrue(result)

    def test_is_squared_positive(self):
        matrix = Matrix([[1, 2], [3, 4]])
        result = matrix.is_squared()
        self.assertTrue(result)

    def test_add_negative(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        with self.assertRaises(TypeError):
            result = matrix1 + '1223'
        

    def test_invalid_matrix_creation(self):
        with self.assertRaises(TypeError):
            matrix = Matrix((1,3,4,6))  # Попытка создания матрицы с неправильными параметрами

if __name__ == '__main__':
    unittest.main()

# a = TestMatrix()
# print(a.test_invalid_matrix_creation())
