class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, order_item):
        # Add an item to the order
        pass

    def calculate_total(self):
        total = 0
        for order_item in self.items:
            total += order_item.menu_item.price * order_item.quantity
        return total

class CafeMenu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, menu_item):
        # Add a menu item to the menu
        pass

class CafeBillingApp:
    def __init__(self):
        self.menu = CafeMenu()

    def create_menu(self):
        # Add menu items to self.menu
        pass

    def take_order(self):
        order = Order()
        # Display menu to cafe staff
        # Allow staff to select items and add to order
        return order

    def calculate_bill(self, order):
        total = order.calculate_total()
        # Apply discounts, taxes, service charges
        # Return the final amount to be paid

    def run(self):
        self.create_menu()
        while True:
            print("1. Take Order")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                order = self.take_order()
                total_amount = self.calculate_bill(order)
                print("Total Bill:", total_amount)
            elif choice == "2":
                break

if __name__ == "__main__":
    cafe_app = CafeBillingApp()
    cafe_app.run()
