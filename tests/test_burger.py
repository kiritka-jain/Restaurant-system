import unittest

from burger import Burger


class MyTestCase(unittest.TestCase):
    def test_get_size(self):
        """ returns true if burger size matches the given size."""
        burger = Burger('regular', 'Aloo-tikki')
        self.assertEqual(burger.get_size(), 'regular')
        burger.set_size('extra-large')
        self.assertEqual(burger.get_size(), 'extra-large')

    def test_get_name(self):
        """ return true if burger name matches the given name."""
        burger = Burger('regular', 'Aloo-tikki')
        self.assertEqual(burger.get_name(),'Aloo-tikki')



if __name__ == '__main__':
    unittest.main()
