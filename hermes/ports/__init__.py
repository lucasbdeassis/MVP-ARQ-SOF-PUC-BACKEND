from typing import Protocol

from hermes.domain.user import User


class UserRepository(Protocol):
    def get_user(self, user_id: str) -> User:
        pass

    def crete_user(self, user: User) -> None:
        pass

    def update_user(self, user: User) -> None:
        pass

    def delete_user(self, user_id: str) -> None:
        pass

    def get_user_by_email(self, email: str) -> User:
        pass

    def list_users(self) -> list[User]:
        pass


class Nubank(Protocol):
    def authenticate_with_refresh_token(self, refresh_token: str, cert_file: str):
        ...

    def get_card_statements(self):
        ...
