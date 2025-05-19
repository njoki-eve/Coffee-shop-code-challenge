import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_valid_name(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("ab")

        with self.assertRaises(TypeError):
            Coffee(123)

    def test_immutable_name(self):
        coffee = Coffee("Latte")
        with self.assertRaises(AttributeError):
            coffee.name = "Mocha"

    def test_minimum_price(self):
        customer = Customer("Leo")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 1.0)
        self.assertEqual(order.price, 1.0)

    def test_no_orders(self):
        coffee = Coffee("New Blend")
        self.assertEqual(coffee.num_orders(), 0)
        self.assertEqual(coffee.average_price(), 0)

if __name__ == '__main__':
    unittest.main()