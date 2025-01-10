class Inventory:
    def __init__(self):
        self.stock = {}
    
    def add_item(self, item_name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity invalid")
        if item_name in self.stock:
            self.stock[item_name] += quantity
        else:
            self.stock[item_name] = quantity
        print(f"Added {quantity} of {item_name}. New stock: {self.stock[item_name]}.")
    
    def remove_item(self, item_name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity Invalid")
        if item_name not in self.stock:
            raise ValueError(f"Item '{item_name}' does not exist in inventory.")
        if self.stock[item_name] < quantity:
            raise ValueError(f"Insufficient stock for '{item_name}'. Current stock: {self.stock[item_name]}.")
        self.stock[item_name] -= quantity
        print(f"Removed {quantity} of {item_name}. Remaining stock: {self.stock[item_name]}.")
        if self.stock[item_name] == 0:
            del self.stock[item_name]

    def query_item(self, item_name):
        if item_name not in self.stock:
            print(f"Item '{item_name}' is not in stock.")
            return 0
        print(f"Current stock of {item_name}: {self.stock[item_name]}.")
        return self.stock[item_name]
    
def main():
    try:
        inventory = Inventory()
        inventory.add_item("Apples", 50)
        inventory.add_item("Bananas", 30)
        inventory.query_item("Apples")
        inventory.remove_item("Apples", 10)
        inventory.query_item("Apples")
        inventory.remove_item("Oranges", 5)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()