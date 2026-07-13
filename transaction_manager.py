from file_manager import fm_load_transaction, fm_save_transaction


class TransactionManager:
    """Manage transactions for one selected date."""

    def __init__(self, selected_date):

        self.id = 0
        self.date = selected_date
        self.report = fm_load_transaction()
        self.transactions = self.report.get(selected_date, [])

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self._save_transaction()

    def _save_transaction(self):

        self.report[self.date] = self.transactions
        fm_save_transaction(self.report)

    def get_transactions(self):

        for id, transactions in enumerate(self.transactions):
            transactions["id"] = id

        return self.transactions

    def pop_transaction(self):

        if not self.transactions:
            return None

        removed_transaction = self.transactions.pop()
        self._save_transaction()

        return removed_transaction

    def remove_transaction(self, index):
        """remove transaction by index"""
        if index < 0 or index > len(self.transactions):
            return None

        removed_transaction = self.transactions.pop()
        self._save_transaction()

        return removed_transaction
