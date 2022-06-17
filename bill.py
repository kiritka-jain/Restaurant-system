from price import Price


class Bill:
    def __init__(self, items: list):
        self.items = items
        self.amount = 0
        self.cgst = 3
        self.sgst = 3
        self.total_payable_amt = 0

    def get_total_amount(self):
        for item in self.items:
            item_price = Price(item)
            self.amount += item_price.get_item_price()
        return self.amount

    def calculate_tax(self):
        amt = self.amount
        s_tax = amt * (3 / 100)
        c_tax = amt * (3 / 100)
        total_tax = s_tax + c_tax
        return total_tax

    def get_total_payable_amount(self):
        amt = self.get_total_amount()
        tax = self.calculate_tax()
        self.total_payable_amt = amt + tax
        return self.total_payable_amt

    def print_bill(self):
        print(f"Your total amount is: {self.get_total_amount()}")
        print(f"Total payble tax is: {self.calculate_tax()}")
        print(f"Your total amount is: {self.get_total_payable_amount()}")

