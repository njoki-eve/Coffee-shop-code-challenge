import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_valid_name(self):
        c = Customer("Sam")
        self.assertEqual(c.name, "Sam")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_set_name_valid(self):
        c = Customer("Sam")
        c.name = "Max"
        self.assertEqual(c.name, "Max")

    def test_orders(self):
        c = Customer("Leo")
        coffee = Coffee("Americano")
        order = Order(c, coffee, 5.0)
        self.assertEqual(len(c.orders()), 1)

    def test_coffees(self):
        c = Customer("Mia")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Cappuccino")
        Order(c, coffee1, 4.0)
        Order(c, coffee2, 4.5)
        self.assertEqual(len(c.coffees()), 2)

if __name__ == '__main__':
    unittest.main()