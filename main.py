from snacks import Snack, add_snack, remove_snack, update_snack_availability
from sales import view_sales_records, record_sale

def main_menu():
    print("Welcome to the Snack Inventory Management System!")
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack availability")
    print("4. View sales records")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_snack_availability()
    elif choice == "4":
        view_sales_records()
    elif choice == "5":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()
