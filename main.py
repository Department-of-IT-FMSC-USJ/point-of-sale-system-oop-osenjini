from product import Product
from customer import Customer
from invoice import Invoice


products = {}
customers = {}
payment_history = [] 


products["P001"] = Product("P001", "Laptop", 1200, 10)
products["P002"] = Product("P002", "Mouse", 25, 50)

customers["C001"] = Customer("C001", "Male", "John Doe", 100, "10% Discount", "123456789")


invoice1 = Invoice("INV001", customers["C001"])
invoice1.add_product(products["P001"], 1)
invoice1.add_product(products["P002"], 2)

invoice1.display_invoice()


payment_history.append(("C001", "INV001"))

print("\nCustomer Payment History:")
for record in payment_history:
    print("Customer ID:", record[0], "| Invoice No:", record[1])
