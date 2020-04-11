"""
тест на модуль bowling.py
@author: vndanilchenko@gmail.com
"""

import bowling
import unittest

class BowlingTest(unittest.TestCase):

    def test_result(self):
        obj = bowling.CalculateResult(result='Х4/34-4', name='Команда1')
        obj.run()
        result = obj.game_sum
        self.assertEqual(result, 46, 'количество очков не совпадает')

    def test_quantity_of_sets(self):
        obj = bowling.CalculateResult(result='Х4/34-4', name='Команда1')
        obj.run()
        result = obj.qnty_sets
        self.assertEqual(result, 4, 'количество фреймов не совпадает')

    def test_empty_list_error(self):
        with self.assertRaises(bowling.EmptyList):
            obj = bowling.CalculateResult(result=None, name='Команда1')
            obj.run()

    def test_too_many_sets_error(self):
        with self.assertRaises(bowling.TooManySets):
            obj = bowling.CalculateResult(result='XXXXXXXXXXXXXXXXXXXXXXXXXXXX', name='Команда1')
            obj.run()

    def test_wrong_symbol_error(self):
        with self.assertRaises(bowling.WrongSymbol):
            obj = bowling.CalculateResult(result='XXaa', name='Команда1')
            obj.run()

    def test_over_ten_sum_error(self):
        with self.assertRaises(bowling.OverTenError):
            obj = bowling.CalculateResult(result="X99", name='Команда1')
            obj.run()

    def test_wrong_symbols_count_error(self):
        with self.assertRaises(bowling.WrongSymbolsCountError):
            obj = bowling.CalculateResult(result="111", name='Команда1')
            obj.run()

    def test_double_slash_error(self):
        with self.assertRaises(bowling.DoubleSlashError):
            obj = bowling.CalculateResult(result="X//", name='Команда1')
            obj.run()

    def test_zero_exists_error(self):
        with self.assertRaises(bowling.ZerroExistsError):
            obj = bowling.CalculateResult(result="1110", name='Команда1')
            obj.run()

    def test_wrong_first_symbol_error(self):
        with self.assertRaises(bowling.WrongFirstSymbolError):
            obj = bowling.CalculateResult(result="11/9", name='Команда1')
            obj.run()

if __name__ == '__main__':
    unittest.main()