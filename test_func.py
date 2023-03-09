import unittest
from function import city_func
class city_func_test(unittest.TestCase):
    def test_city_population_func(self):
        outcome=city_func('santiago','chile',50000)
        self.assertEqual(outcome,'Santiago,Chile - population 50000')
    def test_city_func(self):
        outcome=city_func('santiago','chile')
        self.assertEqual(outcome,'Santiago,Chile')
unittest.main()