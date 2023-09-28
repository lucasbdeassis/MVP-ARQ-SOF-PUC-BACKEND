from hermes.adapters.user_repository import UserRepository
from hermes.domain.user import User


class TestUserRepository:
    def test_get_user_by_email(self, conn):
        user_repository = UserRepository(conn)
        user = user_repository.get_user_by_email("lucasbdeassis@gmail.com")
        assert isinstance(user, User)
