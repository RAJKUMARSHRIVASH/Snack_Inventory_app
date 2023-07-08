class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability

snacks = []

def add_snack():
    snack_id = input("Enter the snack ID: ")
    name = input("Enter the snack name: ")
    price = float(input("Enter the snack price: "))
    availability = input("Is the snack available? (yes/no): ")

    snack = Snack(snack_id, name, price, availability)
    snacks.append(snack)
    print("Snack added successfully!")

def remove_snack():
    snack_id = input("Enter the snack ID to remove: ")
    snack = find_snack_by_id(snack_id)
    
    if snack:
        snacks.remove(snack)
        print("Snack removed successfully!")
    else:
        print("Snack not found.")

def update_snack_availability():
    snack_id = input("Enter the snack ID to update availability: ")
    snack = find_snack_by_id(snack_id)
    
    if snack:
        availability = input("Is the snack available? (yes/no): ")
        snack.availability = availability
        print("Snack availability updated successfully!")
    else:
        print("Snack not found.")

def view_snacks():
    if not snacks:
        print("No snacks found.")
    else:
        print("Snacks:")
        for snack in snacks:
            print(f"Snack ID: {snack.snack_id}, Name: {snack.name}, Price: {snack.price}, Availability: {snack.availability}")

def find_snack_by_id(snack_id):
    for snack in snacks:
        if snack.snack_id == snack_id:
            return snack
    return None
