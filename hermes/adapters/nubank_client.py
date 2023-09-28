import tempfile
from datetime import datetime

from hermes.domain.transaction import Transaction
from hermes.domain.user import User
from hermes.ports import Nubank


class NubankClient:
    _nu: Nubank

    def __init__(self, nu: Nubank):
        self._nu = nu

    def authenticate(self, user: User):
        if not user.nubank_refresh_token or not user.nubank_cert:
            raise Exception("User has no nubank credentials")
        refresh_token = user.nubank_refresh_token
        certificate_bytes = user.nubank_cert
        with tempfile.NamedTemporaryFile(suffix=".p12", delete=False) as cert_file:
            cert_file.write(certificate_bytes)
            cert_file.flush()
            self._nu.authenticate_with_refresh_token(refresh_token, cert_file.name)

    def get_transactions(self):
        transactions = self._nu.get_card_statements()
        if not transactions:
            return []
        return [self._create_transaction(transaction) for transaction in transactions]

    def _create_transaction(self, transaction: dict):
        date_obj = datetime.strptime(transaction["time"].split("T")[0], "%Y-%m-%d")
        data = {
            "id": transaction["id"],
            "description": transaction["description"],
            "amount": transaction["amount"],
            "category": transaction["category"],
            "datetime": transaction["time"],
            "day": date_obj.day,
            "month": date_obj.month,
            "year": date_obj.year,
        }
        if transaction["details"].get("charges"):
            data["installment_purchase"] = True
            data["installments"] = transaction["details"]["charges"]["count"]
            data["installment"] = 1
            data["installment_amount"] = transaction["details"]["charges"]["amount"]
            data["original_transaction_id"] = transaction["id"]
        return Transaction(**data)
