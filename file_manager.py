import os
import json


def fm_save_transaction(transaction_report):
    """save file in transaction.json"""
    with open("transaction.json", "w") as file:
        json.dump(transaction_report, file, indent=4)


def fm_load_transaction():
    """loads and return transaction_report or return an empty dictionary"""

    if os.path.exists("transaction.json"):
        with open("transaction.json", "r") as file:
            return json.load(file)
    else:
        return {}
