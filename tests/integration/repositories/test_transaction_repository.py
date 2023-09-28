from uuid import uuid4

from hermes.adapters.transaction_repository import TransactionRepository
from hermes.domain.transaction import Transaction


class TestTransactionRepository:
    def test_create_transaction(self, conn):
        transaction = {
            "id": uuid4(),
            "description": "Pg *Rechia Store",
            "category": "transaction",
            "amount": 11724,
            "datetime": "2023-09-05T14:55:23Z",
            "source": "upfront_national",
            "title": "vestuário",
            "day": 5,
            "month": 9,
            "year": 2023,
        }
        transaction = Transaction(**transaction)
        TransactionRepository(conn).create_transaction(transaction)

    def test_get_all(self, conn):
        transactions = TransactionRepository(conn).get_all()
        assert isinstance(transactions, list)
        assert isinstance(transactions[0], Transaction)

    def test_get_transactions_by_month(self, conn):
        transactions = TransactionRepository(conn).get_transactions_by_month(9, 2023)
        assert isinstance(transactions, list)
        assert isinstance(transactions[0], Transaction)

    def test_update(self, conn):
        repository = TransactionRepository(conn)
        transaction = repository.get_all()[0]
        transaction.description = "Teste"
        repository.update(transaction.id, transaction)

    def test_get_by_id(self, conn):
        transaction = TransactionRepository(conn).get_all()[0]
        assert TransactionRepository(conn).get_by_id(transaction.id) == transaction
