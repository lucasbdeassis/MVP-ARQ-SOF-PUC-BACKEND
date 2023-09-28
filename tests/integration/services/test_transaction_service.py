from hermes.views.transaction_schema import CreateTransactionSchema


class TestTransactionService:
    def test_create_transaction(self, transaction_service, transaction_repository):
        schema = CreateTransactionSchema(
            time="2021-01-01T00:00:00",
            amount=100,
            description="test",
            category="test",
            id="123",
        )
        transaction = transaction_service.create_transaction(schema)[0]
        assert transaction.id != "123"
        assert transaction == transaction_repository.get_by_id(transaction.id)

    def test_get_all(self, transaction_service):
        transactions = transaction_service.get_all()
        assert isinstance(transactions, list)

    def test_get_by_month(self, transaction_service):
        transaction_service.get_by_month(1, 2021)
