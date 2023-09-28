from uuid import uuid4

from hermes.domain.user import User


class TestUser:
    def test_user(self):
        user = User(id=uuid4(), name="Teste", email="Teste", password="Teste")
