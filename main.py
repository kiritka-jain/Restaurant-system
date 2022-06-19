from bill import Bill
from food_item import FoodItem
from menu import Menu
from order import Order

items = []
for i in range(10):
    item = FoodItem("item" + str(i), 100 + i)
    items.append(item)
menu = Menu(items)

order_items = [(items[0],2),(items[1],3),(items[3],1)]
order_1 = Order(order_items)
order_1_list = order_1.get_order_items()
bill = Bill(order_1_list)
bill.print_bill()


