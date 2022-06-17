from bill import Bill
from burger import Burger
from pizza import Pizza

pizza = Pizza('Medium', 'Thin', ['onion', 'capsicum', 'red paprika'])
burger = Burger('large','channa-tikki')
aloo_burger = Burger('small','aloo-tikki')
order = [pizza,burger,aloo_burger]
bill = Bill(order)
bill.print_bill()
