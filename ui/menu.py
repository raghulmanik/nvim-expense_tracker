from category_mapping import category_mapping
from tabulate import tabulate

from get_function import get_totals

LINE_WIDTH = 50


def print_heading(title):
    title = f"  {title.strip().upper()} "
    print()
    print("╭" + "─" * (LINE_WIDTH - 2) + "╮")
    print("│" + title.center(LINE_WIDTH - 2) + "│")
    print("╰" + "─" * (LINE_WIDTH - 2) + "╯")


def print_menu():
    print_heading("Expense Tracker")

    print("\n[1] Add transaction")
    print("[b] Exit")

    print()


def print_add_helper_commands():

    print()
    print("Format: <command> <amount>")
    print("Example: f1 100")
    print()
    print("[h]   View Available commands")
    print("[v]   View Transactions list")
    print("[s]   View Category summary")
    print("[b]   Return to main menu")
    print()


def print_add_transaction(date):
    print_heading(f"Add Transaction [Date :{date}]")

    print_add_helper_commands()


def print_available_commands():

    print_heading("Available Commands")

    current_type = None
    current_category = None

    for code, values in category_mapping.items():
        transaction_type, category, subcategory = values

        if transaction_type != current_type:
            current_type = transaction_type
            current_category = None

            print()
            print(transaction_type.upper())
            print()

        if category != current_category:
            if current_category is not None:
                print()

            current_category = category

            print(f"  {category}")
            print("  " + "─" * 46)

        print(f"  [{code}]  {subcategory}")

    print()


def print_transaction_list(transactions):
    if not transactions:
        print("No Transaction Available")
        return None

    print_heading("Transaction List")

    table_data = [
        {
            "Id": transaction["id"],
            "Type": transaction["transaction_type"],
            "Category": transaction["category"],
            "Item": transaction["subcategory"],
            "Amount": f"₹{transaction['amount']}",
        }
        for transaction in transactions
    ]

    print()
    print(tabulate(table_data, headers="keys", tablefmt="simple_outline"))

    totals = get_totals(transactions)

    income = f"₹{totals['income']:,.2f}"
    expense = f"₹{totals['expense']:,.2f}"
    balance = f"₹{totals['balance']:,.2f}"

    print("-" * LINE_WIDTH)
    print(f"{'Income':<25}{income:>25}")
    print(f"{'Expense':<25}{expense:>25}")
    print("-" * LINE_WIDTH)
    print(f"{'Balance':<25}{balance:>25}")
    print()


def print_category_summary(summary, totals):

    if not summary:
        print("No Transaction Available")
        return None

    print_heading("Category Summary")
    print()

    for transaction_type, categories in summary.items():
        print(transaction_type.upper())
        print("-" * LINE_WIDTH)
        print()

        for category, subcategories in categories.items():

            category_total = sum(subcategories.values())
            left = f"[  {category} ]"

            print(f"{left:<30}Total: ₹{category_total}")

            for subcategory, amount in subcategories.items():
                print(f"    • {subcategory:<25}₹{amount:>5}")
            print()
        print()

    print("-" * LINE_WIDTH)
    print(f"{'Total Income':<25}₹{totals["income"]}")
    print(f"{'Total Expense':<25}₹{totals["expense"]}")
    print(f"{'Total Balance':<25}₹{totals["balance"]}")
    print("-" * LINE_WIDTH)
