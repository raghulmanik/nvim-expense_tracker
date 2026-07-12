from get_function import get_date, get_transaction_summary_and_totals
from ui.menu import (
    print_available_commands,
    print_add_helper_commands,
    print_add_transaction,
    print_category_summary,
    print_transaction_list,
)
from category_mapping import category_mapping
from transaction_manager import TransactionManager


def add_transaction():

    date = get_date()

    if date is None:
        return

    manager = TransactionManager(date)

    print_add_transaction(date)

    while True:
        choice = input("> ").strip().lower()

        # help - to view commands
        if choice == "h":
            print_available_commands()
            continue

        # v - to view transactions
        if choice == "v":
            print_transaction_list(manager.get_transactions())
            continue

        if choice == "s":

            """print category summary"""
            transactions = manager.get_transactions()

            category_date = get_transaction_summary_and_totals(transactions)

            summary = category_date["summary"]
            totals = category_date["totals"]
            print_category_summary(summary, totals)

            continue

        if choice == "p":
            transaction = manager.pop_transaction()
            if transaction is None:
                print("No transaction is available")
            else:
                print(f"✓ Removed: {transaction['subcategory']}")
            continue

        if choice == "b":
            break

        # Expect : <command> <amount>

        parts = choice.split()

        if len(parts) != 2:
            print("\nInvalid Format")
            print_add_helper_commands()
            continue

        command, amount = parts

        if command not in category_mapping:
            print(f"Unknown command: {command}")
            continue

        try:
            amount = int(amount)
        except ValueError:
            print("Amount must be a number")
            continue

        transaction_type, category, subcategory = category_mapping[command]

        transaciton = {
            "transaction_type": transaction_type,
            "category": category,
            "subcategory": subcategory,
            "amount": int(amount),
        }

        manager.add_transaction(transaciton)

        print(f"✓ Added ₹{amount} to {subcategory}")
