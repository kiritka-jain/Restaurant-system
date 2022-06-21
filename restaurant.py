from menu import Menu


class Restaurant:
    def __init__(self, name, r_id,menu:Menu):
        self.name = name
        self.r_id = r_id
        self.menu = menu
        self.orders = []

    def place_order(self,order):
        self.orders.append(order)


