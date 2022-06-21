class Bill:
    SGST = 3
    CGST = 3

    def __init__(self, order):
        self.order = order
        self.amount = 0
        self.total_payable_amt = 0

    def _get_total_amount(self):
        amount = 0
        for item in self.order:
            item_price = item[2]
            quantity = item[1]
            total = item_price * quantity
            amount += total
        return amount

    def _calculate_tax(self):
        amt = self._get_total_amount()
        s_tax = amt * (self.SGST / 100)
        c_tax = amt * (self.CGST / 100)
        total_tax = s_tax + c_tax
        return total_tax

    def get_total_payable_amount(self):
        self.amount = self._get_total_amount()
        tax = self._calculate_tax()
        self.total_payable_amt = self.amount + tax
        return self.total_payable_amt

    def print_bill(self):
        print(f"Your total amount is: {self._get_total_amount()}")
        print(f"Total payble tax is: {self._calculate_tax()}")
        print(f"Your total amount is: {self.get_total_payable_amount()}")
