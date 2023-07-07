from datetime import datetime

sales_records = []

def view_sales_records():
    if not sales_records:
        print("No sales records found.")
    else:
        print("Sales Records:")
        for record in sales_records:
            print(f"Snack ID: {record['snack_id']}, Date: {record['date']}")

def find_snack_by_id(snack_id, snacks):
    for snack in snacks:
        if snack.snack_id == snack_id:
            return snack
    return None

def record_sale(snack_id, snacks):
    snack = find_snack_by_id(snack_id, snacks)

    if snack:
        if snack.availability == "yes":
            sales_records.append({"snack_id": snack_id, "date": datetime.now()})
            snack.availability = "no"
            print("Sale recorded successfully!")
        else:
            print("Snack not available.")
    else:
        print("Snack not found.")
