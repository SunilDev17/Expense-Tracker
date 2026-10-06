from datetime import datetime

def validate_amount():
    while True:
        try:
            amount = int(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be greater than 0")
                continue
            return amount
        except ValueError:
            print("Invalid amount")
def validate_category():
    while True:
        category = input("Enter the category: ").strip()
        if not category:
            print("Invalid category")
            continue
        return category

def validate_description():
    while True:
        description = input("Enter the description: ").strip()
        if not description:
            print("Invalid description")
            continue
        return description

def validate_date():
    while True:
        date = input("Enter the date: ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD")