class Bill:
    def __init__(self, order):
        self.order = order
        self.amount = 0
        self.cgst = 3
        self.sgst = 3
        self.total_payable_amt = 0

    def get_total_amount(self):
        for item in self.order:
            item_price = item[2]
            quantity = item[1]
            total = item_price * quantity
            self.amount += total
        return self.amount

    def calculate_tax(self):
        amt = self.amount
        s_tax = amt * (3 / 100)
        c_tax = amt * (3 / 100)
        total_tax = s_tax + c_tax
        return total_tax

    def get_total_payable_amount(self):
        amt = self.amount
        tax = self.calculate_tax()
        self.total_payable_amt = amt + tax
        return self.total_payable_amt

    def print_bill(self):
        print(f"Your total amount is: {self.get_total_amount()}")
        print(f"Total payble tax is: {self.calculate_tax()}")
        print(f"Your total amount is: {self.get_total_payable_amount()}")
