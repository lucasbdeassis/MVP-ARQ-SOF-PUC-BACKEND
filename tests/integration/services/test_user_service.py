from uuid import uuid4

from hermes.domain.user import User


class TestUserService:
    def test_list_users(self, user_service):
        users = user_service.list_users()
        assert isinstance(users, list)

    def test_get_user(self, user_service):
        user_id = user_service.list_users()[0].id
        user = user_service.get_user(user_id)
        assert isinstance(user, User)

    def test_get_user_by_email(self, user_service):
        user_email = user_service.list_users()[0].email
        user = user_service.get_user_by_email(user_email)
        assert isinstance(user, User)

    def test_create_user(self, user_service):
        user = User(
            id=uuid4(),
            name="test",
            email="teste@test.com",
            password="123456",
        )
        user_service.create_user(user)
        user = user_service.get_user(user.id)
        assert isinstance(user, User)
