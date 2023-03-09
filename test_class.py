import unittest
from classy import Employee
class TestEmployee(unittest.TestCase):
        def setUp(self):
            self.new_employee=Employee('zhang','san',10000)

        def test_default_raise(self):
            self.new_employee.give_raise()
            self.assertEqual(15000,self.new_employee.salary)
            
        def test_custom_raise(self):
            self.new_employee.give_raise(50000)
            self.assertEqual(60000,self.new_employee.salary)
unittest.main()
