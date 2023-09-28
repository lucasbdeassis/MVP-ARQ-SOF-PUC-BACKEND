from hermes.views.transaction_schema import (
    CreateTransactionSchema,
    UpdateTransactionSchema,
)


class TestTransactionSchema:
    def test_create_transaction_schema(self):
        schema = CreateTransactionSchema(
            datetime="2021-01-01T00:00:00",
            amount=100,
            description="test",
            category="test",
            id="123",
        )
        assert not getattr(schema, "id", False)

    def test_update_transaction_schema(self):
        schema = UpdateTransactionSchema(
            amount=100,
            id="123",
        )
        assert not getattr(schema, "id", False)
