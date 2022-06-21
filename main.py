from bill import Bill
from customer import Customer
from food_item import FoodItem
from menu import Menu
from order import Order
from restaurant import Restaurant

items = []
for i in range(10):
    item = FoodItem("item" + str(i), 100 + i)
    items.append(item)
menu = Menu(items)

restaurant = Restaurant('Dominos', 1001, menu)
customer_1 = Customer('Timmy', 1)
order_items = [(items[0], 2), (items[1], 3), (items[3], 1)]

order_1 = Order(customer_1, order_items)

order_1_list = order_1.get_order_items()
bill = Bill(order_1_list)
bill.print_bill()
