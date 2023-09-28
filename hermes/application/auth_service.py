import datetime
import random
from typing import Protocol

import jwt

from hermes.application.exceptions import Unauthorized
from hermes.domain.user import User
from settings import SECRET


def generate_random_numbers() -> str:
    return "".join([str(random.randint(0, 9)) for _ in range(6)])


class EmailClient(Protocol):
    def send_email(self, subject: str, body: str, to: str) -> None:
        ...


class AuthService:
    def __init__(self, email_client=None):
        self._email_client = email_client

    def user_login(self, user: User, password: str) -> str:
        if user.password != password:
            raise Unauthorized("Unauthorized")

        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "user": str(user.id),
        }

        return jwt.encode(payload, SECRET, algorithm="HS256")

    def verify_token(self, token: str) -> str:
        try:
            payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise Unauthorized("Token expirado, faça login novamente")
        except jwt.InvalidTokenError:
            raise Unauthorized("Token inválido, faça login novamente")

        return payload["user"]

    def reset_password(self, user: User) -> None:
        new_password = generate_random_numbers()

        try:
            self._email_client.send_email(
                "Recuperação de senha",
                f"Sua nova senha é {new_password}",
                user.email,
            )
        except Exception:
            raise Exception("Error sending email")

        return new_password
