class Burger:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.price = 0

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name
