from hermes.domain.transaction import Transaction


class TestTransaction:
    def test_create_transaction(self):
        transaction = {
            "id": "64f7415b-94b9-455c-b90b-569db67a840b",
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

    def test_get_installments(self):
        transaction = {
            "id": "64f7415b-94b9-455c-b90b-569db67a840b",
            "description": "Pg *Rechia Store",
            "category": "transaction",
            "amount": 11724,
            "datetime": "2023-09-05T14:55:23Z",
            "source": "upfront_national",
            "title": "vestuário",
            "day": 5,
            "month": 9,
            "year": 2023,
            "installment_purchase": True,
            "installments": 3,
            "installment": 1,
            "installment_amount": 3908,
            "original_transaction_id": "64f7415b-94b9-455c-b90b-569db67a840b",
        }
        transaction = Transaction(**transaction)
        installments = transaction.get_installments()
        assert len(installments) == 2
        assert installments[0].installment == 2
        assert installments[0].original_transaction_id == transaction.id
