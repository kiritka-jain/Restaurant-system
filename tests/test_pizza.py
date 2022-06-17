import unittest

from pizza import Pizza


class MyTestCase(unittest.TestCase):

    def test_get_size(self):
        """ returns true if pizza size matches the given size."""
        pizza = Pizza('Medium', 'Thin', ['onion', 'capsicum', 'red paprika'])
        self.assertEqual(pizza.get_size(), "Medium")
        pizza.set_size('Large')
        self.assertEqual(pizza.get_size(), "Large")
        pizza.set_size('Regular')
        self.assertEqual(pizza.get_size(), "Regular")

    def test_get_crust(self):
        """ returns true if pizza crust matches the given crust."""
        pizza = Pizza('Medium', 'Thin', ['onion', 'capsicum', 'red paprika'])
        self.assertEqual(pizza.get_crust(), "Thin")
        pizza.set_crust('cheese burst')
        self.assertEqual(pizza.get_crust(), "cheese burst")
        pizza.set_crust('Regular')
        self.assertEqual(pizza.get_crust(), "Regular")

    def test_get_toppings(self):
        """ returns true if pizza toppings matches the given toppings."""
        pizza = Pizza('Medium', 'Thin', ['onion', 'capsicum', 'red paprika'])
        self.assertEqual(pizza.get_toppings(), ['onion', 'capsicum', 'red paprika'])
        pizza.set_toppings(['onion', 'red paprika'])
        self.assertEqual(pizza.get_toppings(), ['onion', 'red paprika'])
        pizza.set_toppings(['onion'])
        self.assertEqual(pizza.get_toppings(), ['onion'])



if __name__ == '__main__':
    unittest.main()
