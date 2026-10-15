from datetime import datetime
import json

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: expenses.json contains invalid data.")
        return []


def get_amount():
    while True:
        try:
            amount = float(input("Enter Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number!")


expenses = load_expenses()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Expenses")
    print("4. Show Category-wise Expense")
    print("5. Delete Expense")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 5!")
        continue

    if choice == 1:
        exp_name = input("Enter Expense Name: ").strip().title()

        if not exp_name:
            print("Expense name cannot be empty!")
            continue

        amount = get_amount()
        category = input("Enter Category: ").strip().title()

        if not category:
            print("Category cannot be empty!")
            continue

        date_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        exp_dict = {
            "name": exp_name,
            "amount": amount,
            "category": category,
            "date_time": date_time
        }

        expenses.append(exp_dict)
        save_expenses(expenses)

        print("Expense Added Successfully!")
        print("Added On:", date_time)

    elif choice == 2:
        if not expenses:
            print("No expenses found!")
        else:
            print(
                f"{'No.':<5}{'Expense':<20}"
                f"{'Amount':<12}{'Category':<18}{'Date & Time'}"
            )
            print("-" * 80)

            for number, expense in enumerate(expenses, start=1):
                print(
                    f"{number:<5}"
                    f"{expense['name']:<20}"
                    f"{expense['amount']:<12.2f}"
                    f"{expense['category']:<18}"
                    f"{expense['date_time']}"
                )

    elif choice == 3:
        total = sum(expense["amount"] for expense in expenses)

        print("\nTotal Expenses")
        print("=" * 30)
        print(f"Total: Rs. {total:.2f}")

    elif choice == 4:
        if not expenses:
            print("No expenses found!")
            continue

        category_total = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount

        print("\nCategory-wise Expenses")
        print(f"{'Category':<20}{'Amount (Rs.)':>15}")
        print("-" * 35)

        for category, total in category_total.items():
            print(f"{category:<20}{total:>15.2f}")

    elif choice == 5:
        if not expenses:
            print("Not Expenses Found!")

        else:
            for number, expense in enumerate(expenses, start=1):
                print(number, expense["name"], expense["amount"])
            try:
                delete = int(input("Enter Number to Delete Item: "))
            except ValueError:
                print("Please Enter Numbers Only!")
                continue

            if delete < 1 or delete > len(expenses):
                print("Invalid Number!")
            else:
                deleted_expenses = expenses.pop(delete - 1)
                save_expenses(expenses)
                print("Expenses Deleted Successfully: ",deleted_expenses["name"])

    elif choice == 6:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Enter a valid number from 1 to 6!")
