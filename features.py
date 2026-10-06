from data import save_expense,expense_list
from validation import *

def add_expense():
    amount=validate_amount()
    category=validate_category()
    description=validate_description()
    date=validate_date()
    expense_list.append({"amount": amount, "category": category, "description": description, "date": date})
    save_expense()

def view_expense():
    if expense_list:
        for number,expense in enumerate(expense_list,start=1):
            print(f"Expense {number}")
            print(f"Amount : {expense['amount']}")
            print(f"Category : {expense['category']}")
            print(f"Description : {expense['description']}")
            print(f"Date :{expense['date']}")
            print("-----------------------------------------")
    else:
        print("No expense")

def calculate_expense():
    total_expense = 0
    if expense_list:
        for expense in expense_list:
            total_expense += expense["amount"]
        return total_expense
    else:
       return "No Expense to calculate"

def delete_expense():
    if not expense_list:
        return "No expense to delete"
    view_expense()
    while True:
        try:
            expense_to_delete = int(input("Enter the expense to delete: "))
            if expense_to_delete < 1 or expense_to_delete > len(expense_list):
                print("Invalid expense to delete")
                continue
            del expense_list[expense_to_delete - 1]
            save_expense()
            return "Expense deleted successfully"
        except ValueError:
            print("Invalid Index Value")

def category_expense():
    category_name=input("Enter the category name: ")
    total_amount=0
    found=False
    for expense in expense_list:
        if category_name == expense["category"]:
            total_amount += expense["amount"]
            found=True
    if found:
        return total_amount
    else:
        return "No category  to calculate expense for"

def edit_expense():
    if not expense_list:
        return "No expense to edit"
    view_expense()
    while True:
        try:
            expense_id=int(input("Enter the expense id: "))
            if expense_id <= 0 or expense_id > len(expense_list):
                continue
            break
        except ValueError:
            print("Invalid option")
    for number,expense in enumerate(expense_list,start=1):
        if expense_id == number:
            found=True
            print("1.Amount\n2.Category\n3.Description\n4.Date\n5.Exit")
            while True:
                try:
                    field=int(input("Enter the field you want to edit: "))
                    if field < 1 or field > 5:
                        continue
                    match field:
                            case 1:
                                amount=validate_amount()
                                expense["amount"]=amount
                            case 2:
                                category=validate_category()
                                expense["category"]=category
                            case 3:
                                description=validate_description()
                                expense["description"]=description
                            case 4:
                                date=validate_date()
                                expense["date"]=date
                            case 5:
                                break
                except ValueError:
                    print("Invalid option")
            save_expense()
    return "Expense edited successfully"

