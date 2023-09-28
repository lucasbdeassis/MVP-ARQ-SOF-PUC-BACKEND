from hermes.domain.user import User
from hermes.ports import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: str) -> User:
        return self.user_repository.get_user(user_id)

    def list_users(self) -> list[User]:
        return self.user_repository.list_users()

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)

    def get_user_by_id(self, user_id: str) -> User:
        return self.user_repository.get_user(user_id)

    def create_user(self, user: User) -> None:
        self.user_repository.create_user(user)
