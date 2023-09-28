from pynubank import Nubank

from hermes.adapters.nubank_client import NubankClient
from hermes.adapters.transaction_repository import TransactionRepository
from hermes.adapters.user_repository import UserRepository
from hermes.application.auth_service import AuthService
from hermes.application.transaction_service import TransactionService
from hermes.application.user_service import UserService
from hermes.domain.user import User
from hermes.infra.db import get_connection


class InjectorFactory:
    def __enter__(self):
        self._conn = get_connection()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._conn.rollback()
            raise
        self._conn.commit()
        self._conn.close()

    def user_repository(self) -> UserRepository:
        return UserRepository(self._conn)

    def transaction_repository(self) -> TransactionRepository:
        return TransactionRepository(self._conn)

    def auth_service(self) -> AuthService:
        return AuthService()

    def user_service(self) -> UserService:
        return UserService(self.user_repository())

    def nubank_client(self, user: User = None) -> NubankClient:
        client = NubankClient(Nubank())
        if user.nubank_refresh_token and user.nubank_cert:
            client.authenticate(user)
        return client

    def transaction_service(self, user: User) -> TransactionService:
        return TransactionService(
            self.transaction_repository(), user, self.nubank_client(user)
        )
