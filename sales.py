from datetime import datetime
from snacks import find_snack_by_id
sales_records = []

def view_sales_records():
    if not sales_records:
        print("No sales records found.")
    else:
        print("Sales Records:")
        for record in sales_records:
            print(f"Snack ID: {record['snack_id']}, Date: {record['date']}")

def record_sale():
    snack_id = input("Enter the snack ID to record sale: ")
    snack = find_snack_by_id(snack_id)

    if snack:
        if snack.availability == "yes":
            sales_records.append({"snack_id": snack_id, "date": datetime.now()})
            snack.availability = "no"
            print("Sale recorded successfully!")
        else:
            print("Snack not available.")
    else:
        print("Snack not found.")
