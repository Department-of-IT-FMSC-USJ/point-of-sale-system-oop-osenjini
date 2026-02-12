class Customer:
    def __init__(self, customer_id, gender, name, loyalty_points, promotions, contact_no):
        self.customer_id = customer_id
        self.gender = gender
        self.name = name
        self.loyalty_points = loyalty_points
        self.promotions = promotions
        self.contact_no = contact_no

    def display_customer(self):
        print(f"ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Loyalty Points: {self.loyalty_points}")
        print(f"Promotions: {self.promotions}")
        print(f"Contact No: {self.contact_no}")
