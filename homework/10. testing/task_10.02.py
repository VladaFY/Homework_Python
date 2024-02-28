import unittest
import sys
sys.path.append('C:/Users/vyuldasheva/Documents/Adaptation/dar-python-mentoring-master/homework/6_classes')

from task_6_2 import  Euro, Dollar, Ruble

class TestCurrency(unittest.TestCase):

    def test_convert_positive(self):
            euro = Euro(100)
            converted_dollar = euro.to(Dollar)
            self.assertEqual(converted_dollar.amount, 120.0)  # Проверяем правильность конвертации


    def test_check_value_positive(self):
        euro = Euro(100)
        self.assertTrue(euro.check_value(euro))  # Проверяем, что значение является экземпляром класса

    def test_check_value_negative(self):
        class Dummy:
            pass
        dummy = Dummy()
        self.assertFalse(Euro.check_value(dummy))  # Проверяем, что значение не является экземпляром класса

    def test_str_method(self):
        euro = Euro(100)
        self.assertEqual(str(euro), "100€")  # Проверяем правильность форматированного вывода
    
    def test_gt_positive(self):
        euro1 = Euro(100)
        euro2 = Euro(50)
        self.assertTrue(euro1 > euro2)  # Проверяем, что euro1 больше, чем euro2

    def test_gt_negative(self):
        euro1 = Euro(50)
        euro2 = Euro(100)
        self.assertFalse(euro1 > euro2)  # Проверяем, что euro1 не больше, чем euro2

    def test_add_positive(self):
        euro1 = Euro(100)
        euro2 = Euro(50)
        result = euro1 + euro2
        self.assertEqual(result.amount, 150)  # Проверяем правильность сложения

    def test_sub_positive(self):
        euro1 = Euro(100)
        euro2 = Euro(50)
        result = euro1 - euro2
        self.assertEqual(result.amount, 50)  # Проверяем правильность вычитания

    def test_ge_positive(self):
        euro1 = Euro(100)
        euro2 = Euro(50)
        self.assertTrue(euro1 >= euro2)  # Проверяем, что euro1 больше или равно euro2

    def test_truediv_positive(self):
        euro = Euro(100)
        result = euro / 2
        self.assertEqual(result.amount, 50)  # Проверяем правильность деления

    def test_mul_positive(self):
        euro = Euro(100)
        result = euro * 2
        self.assertEqual(result.amount, 200)  # Проверяем правильность умножения

if __name__ == '__main__':
    
    unittest.main()