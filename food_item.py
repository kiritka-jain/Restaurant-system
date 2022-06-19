class FoodItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
