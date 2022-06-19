class Order:
    def __init__(self, items):
        self.order_items = []
        for item in items:
            self.order_items.append(item)

    def print_ordered_items(self):
        print("item_name ... quantity_ordered ...price")
        for item in self.order_items:
            print(f'{item[0].get_name()} ... {item[1]} ...{item[0].get_price()}')

    def get_order_items(self):
        order_details = []
        for item in self.order_items:
            order_details.append((item[0].get_name(), item[1], item[0].get_price()))
        return order_details
