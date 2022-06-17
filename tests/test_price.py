import unittest

from burger import Burger
from pizza import Pizza
from price import Price


class MyTestCase(unittest.TestCase):

    def test_get_item_price(self):
        actual_input = Price(Pizza('Medium', 'Thin', ['onion', 'capsicum', 'red paprika'])).get_item_price()
        desired_output = 440
        self.assertEqual(actual_input,desired_output)


if __name__ == '__main__':
    unittest.main()
