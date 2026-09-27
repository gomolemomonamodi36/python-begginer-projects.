# Expense Tracker - Project 3 by Gomolemo
from datetime import datetime

def add_expense():
    item = input("What did you spend on? ")
    amount = float(input("Amount (R): "))
    date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.txt", "a") as f:
        f.write(f"{date} | {item} | R{amount}\n")
    print(f"Saved: {item} - R{amount}")

def view_total():
    try:
        total = 0
        with open("expenses.txt", "r") as f:
            for line in f:
                print(line.strip())
                total += float(line.split("R")[1])
        print(f"\nTotal Spent: R{total}")
    except FileNotFoundError:
        print("No expenses yet")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_total()
    elif choice == "3":
        break
		