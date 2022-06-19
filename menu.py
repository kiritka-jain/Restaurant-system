class Menu:
    def __init__(self, items_list):
        self.items_list = []
        for item in items_list:
            self.items_list.append(item)

    def print_menu(self):
        for item in self.items_list:
            print(f"item: {item.get_name()} ...... price:{item.get_price()}")

    def add_item(self, item):
        self.items_list.append(item)

    def remove_item(self, item):
        self.items_list.remove(item)
