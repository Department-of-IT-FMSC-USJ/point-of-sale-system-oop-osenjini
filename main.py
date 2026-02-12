from product import Product
from customer import Customer
from invoice import Invoice


products = {}
customers = {}
invoices = {}
payment_history = []

def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    unit_price = float(input("Enter Unit Price: "))
    quantity = int(input("Enter Quantity: "))

    products[product_id] = Product(product_id, name, unit_price, quantity)
    print("✅ Product added successfully!\n")


def add_customer():
    customer_id = input("Enter Customer ID: ")
    gender = input("Enter Gender: ")
    name = input("Enter Customer Name: ")
    loyalty_points = int(input("Enter Loyalty Points: "))
    promotions = input("Enter Promotions: ")
    contact_no = input("Enter Contact Number: ")

    customers[customer_id] = Customer(customer_id, gender, name, loyalty_points, promotions, contact_no)
    print("✅ Customer added successfully!\n")


def create_invoice():
    invoice_no = input("Enter Invoice Number: ")
    customer_id = input("Enter Customer ID: ")

    if customer_id not in customers:
        print("❌ Customer not found!\n")
        return

    invoice = Invoice(invoice_no, customers[customer_id])

    while True:
        product_id = input("Enter Product ID (or 'done' to finish): ")

        if product_id.lower() == "done":
            break

        if product_id not in products:
            print("❌ Product not found!")
            continue

        quantity = int(input("Enter Quantity: "))
        invoice.add_product(products[product_id], quantity)

    invoices[invoice_no] = invoice
    payment_history.append((customer_id, invoice_no))

    print("✅ Invoice created successfully!\n")


def view_all_data():
    print("\n========== ALL DATA ==========")


    print("\n--- Products ---")
    for product in products.values():
        product.display_product()
        print("-------------------")


    print("\n--- Customers ---")
    for customer in customers.values():
        customer.display_customer()
        print("-------------------")


    print("\n--- Invoices ---")
    for invoice in invoices.values():
        invoice.display_invoice()


    print("\n--- Payment History ---")
    for record in payment_history:
        print("Customer ID:", record[0], "| Invoice No:", record[1])

    print("\n================================\n")


def menu():
    while True:
        print("====== POS SYSTEM ======")
        print("1. Add Product")
        print("2. Add Customer")
        print("3. Create Invoice")
        print("4. View All Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            create_invoice()
        elif choice == "4":
            view_all_data()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.\n")


menu()
