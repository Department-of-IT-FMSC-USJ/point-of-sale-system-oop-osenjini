class Product:
    def __init__(self, product_id, name, unit_price, quantity):
        self.product_id = product_id
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def update_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Not enough stock available!")

    def display_product(self):
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Unit Price: {self.unit_price}")
        print(f"Quantity: {self.quantity}")
