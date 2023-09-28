from uuid import uuid4

from hermes.domain.transaction import Transaction
from hermes.domain.user import User
from hermes.views.transaction_schema import CreateTransactionSchema


class TransactionService:
    user: User

    def __init__(self, transaction_repository, user: User, nubank_client):
        self.transaction_repository = transaction_repository
        self.nubank_client = nubank_client
        self.user = user

    def update_nubank_transactions(self):
        new_transactions: list[Transaction] = self.nubank_client.get_transactions()
        transactions_on_database: list[
            Transaction
        ] = self.transaction_repository.get_all()
        transactions_on_database_ids = [
            transaction.id for transaction in transactions_on_database
        ]
        transactions_to_insert = []

        for transaction in new_transactions:
            if transaction.id not in transactions_on_database_ids:
                if transaction.installments:
                    transactions_to_insert.extend(transaction.get_installments())
                transactions_to_insert.append(transaction)

        for transaction in transactions_to_insert:
            self.transaction_repository.create_transaction(transaction)

    def create_transaction(
        self, transaction: CreateTransactionSchema
    ) -> list[Transaction]:
        transaction = Transaction(
            id=str(uuid4()),
            owner_id=self.user.id,
            **transaction.model_dump(exclude_unset=True)
        )
        transactions = [transaction]
        if transaction.installments:
            transactions.extend(transaction.get_installments())
        for transaction in transactions:
            self.transaction_repository.create_transaction(transaction)
        return transactions

    def list_transactions(self) -> list[Transaction]:
        return self.transaction_repository.get_all(self.user.id)

    def get_by_month(self, month: int, year: int) -> list[Transaction]:
        return self.transaction_repository.get_transactions_by_month(
            month, year, self.user.id
        )

    def get_transaction(self, transaction_id: str) -> Transaction:
        return self.transaction_repository.get_transaction(transaction_id, self.user.id)

    def update_transaction(
        self, transaction_id: str, transaction: CreateTransactionSchema
    ) -> Transaction:
        return self.transaction_repository.update(
            transaction_id, transaction, self.user.id
        )

    def delete_transaction(self, transaction_id: str) -> None:
        self.transaction_repository.delete(transaction_id, self.user.id)
