from hermes.application.auth_service import AuthService
from hermes.application.user_service import UserService


class TestAuthService:
    def test_authenticate(self, user_service: UserService, auth_service: AuthService):
        user = user_service.get_user_by_email("lucasbdeassis@gmail.com")
        auth_service.user_login(user, "123456")

    def test_verify_token(self, user_service: UserService, auth_service: AuthService):
        user = user_service.get_user_by_email("lucasbdeassis@gmail.com")
        token = auth_service.user_login(user, "123456")
        auth_service.verify_token(token)
