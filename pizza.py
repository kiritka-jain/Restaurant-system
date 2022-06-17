class Pizza:
    def __init__(self, size, crust, toppings: list):
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.price = 0

    def set_size(self, size):
        self.size = size

    def set_crust(self, crust):
        self.crust = crust

    def set_toppings(self, toppings):
        self.toppings = toppings

    def get_size(self):
        return self.size

    def get_crust(self):
        return self.crust

    def get_toppings(self):
        return self.toppings
