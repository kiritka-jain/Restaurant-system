from pizza import Pizza
from burger import Burger


class Price:
    def __init__(self, item):
        self.item = item
        self.price = 0
        self.base_price = 0
        self.add_on_price = 0

    def get_item_price(self):
        if type(self.item) == Pizza:
            self.price = self._set_pizza_price()
            return self.price
        if type(self.item) == Burger:
            self.price = self._set_burger_price()
            return self.price

    def _set_pizza_price(self):
        pizza = self.item
        total_toppings = len(pizza.get_toppings())
        crust = pizza.get_crust()
        size = pizza.get_size()
        if size == 'Regular':
            self.base_price = 200
        if size == "Medium":
            self.base_price = 300
        if size == 'Large':
            self.base_price = 400
        if crust == 'Regular':
            self.add_on_price = 0
        if crust == "Thin":
            self.add_on_price = 50
        if crust == "Cheese-Burst":
            self.add_on_price = 100
        self.price = self.base_price + self.add_on_price + (30 * total_toppings)
        return self.price

    def _set_burger_price(self):
        burger = self.item
        size = burger.get_size()
        name = burger.get_name()
        if name == 'aloo-tikki':
            self.base_price = 30
        if name == 'channa-tikki':
            self.base_price = 40
        if name == 'chiken':
            self.base_price = 50
        if size == 'small':
            self.add_on_price = 0
        if size == 'medium':
            self.add_on_price = 10
        if size == 'large':
            self.add_on_price = 20
        self.price = self.base_price + self.add_on_price
        return self.price
