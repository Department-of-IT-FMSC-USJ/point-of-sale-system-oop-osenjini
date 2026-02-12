from datetime import datetime

class Invoice:
    def __init__(self, invoice_no, customer):
        self.invoice_no = invoice_no
        self.date = datetime.now()
        self.customer = customer
        self.products = []
        self.total_price = 0

    def add_product(self, product, quantity):
        if product.quantity >= quantity:
            product.update_stock(quantity)
            self.products.append((product, quantity))
            self.total_price += product.unit_price * quantity
        else:
            print("Not enough stock available!")

    def display_invoice(self):
        print("\n===== INVOICE =====")
        print("Invoice No:", self.invoice_no)
        print("Date:", self.date)
        print("Customer:", self.customer.name)
        print("\nProducts Purchased:")

        for product, quantity in self.products:
            subtotal = product.unit_price * quantity
            print(f"{product.name} x {quantity} = {subtotal}")

        print("\nTotal Price:", self.total_price)
        print("====================")
