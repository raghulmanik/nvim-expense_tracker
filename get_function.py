from datetime import datetime


def get_date():
    """Return a date as a YYYY-MM-DD string, or None when the user goes back."""
    while True:

        choice = input("Enter 't' for today or a date (YYYY-MM-DD):").strip().lower()

        if choice == "t":
            return datetime.today().strftime("%Y-%m-%d")

        if choice == "b":
            return None

        try:
            datetime.strptime(choice, "%Y-%m-%d")
            return choice
        except ValueError:
            print("Invalid input. Enter 't' or 'b', or a date in YYYY-MM-DD format.")


def get_totals(transactions):

    totals = {
        "expense": 0,
        "income": 0,
    }

    for transaction in transactions:
        if transaction["transaction_type"] == "Expense":
            totals["expense"] += transaction["amount"]
        if transaction["transaction_type"] == "Income":
            totals["income"] += transaction["amount"]

    totals["balance"] = totals["income"] - totals["expense"]
    return totals


def get_transaction_summary_and_totals(transactions):
    summary = {}

    for transaction in transactions:
        transaction_type = transaction["transaction_type"]
        category = transaction["category"]
        subcategory = transaction["subcategory"]
        amount = transaction["amount"]

        if transaction_type not in summary:
            summary[transaction_type] = {}

        if category not in summary[transaction_type]:
            summary[transaction_type][category] = {}

        if subcategory not in summary[transaction_type][category]:
            summary[transaction_type][category][subcategory] = 0

        summary[transaction_type][category][subcategory] += amount

    totals = get_totals(transactions)
    return {"summary": summary, "totals": totals}
