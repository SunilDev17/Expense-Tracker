from data import load_expense
from features import *


def main():
    print("Hello there ,Welcome to the Expense Tracker")
    print("1. Add expense\n 2. View expense\n 3. Total expense\n 4. Exit\n "
          "5. Delete expense\n 6. Category expense\n 7. Edit expense")
    while True:
        try:
            see = int(input("Enter the option: "))
        except ValueError:
            print("Invalid option")
            continue
        match see:
            case 1:
               add_expense()
            case 2:
                view_expense()
            case 3:
               expense=calculate_expense()
               print(f"Total expense: {expense}")
            case 4:
                break
            case 5:
                deleted=delete_expense()
                print(deleted)
            case 6:
                category_amount=category_expense()
                print(f"Total_Category_Expense:{category_amount}")
            case 7:
                edit_expense()
            case _:
                print("Invalid option")


if __name__ == "__main__":
    load_expense()
    main()