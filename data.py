import json

expense_list = []

def save_expense():
    with open("expense.json", "w") as file:
        json.dump(expense_list, file, indent=4)


def load_expense():
    try:
        with open("expense.json", "r") as file:
            loaded_expense= json.load(file)
        expense_list.clear()
        expense_list.extend(loaded_expense)
    except (FileNotFoundError, json.JSONDecodeError):
        expense_list.clear()