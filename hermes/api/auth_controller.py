from flask import blueprints, request
from pydantic import BaseModel

from hermes.api.spec import add_schema
from hermes.application.factories import InjectorFactory

auth_controller = blueprints.Blueprint("auth", __name__)


class LoginSchema(BaseModel):
    username: str
    password: str


add_schema([LoginSchema])


@auth_controller.route("/login", methods=["POST"])
def login():
    """
    ---
    post:
      summary: Users login
      description: Users login
      requestBody:
        required: true
        content:
          application/json:
            schema: LoginSchema
      responses:
        200:
          description: returns a token
          content:
            application/json:
              schema:
                type: object
                properties:
                  token:
                    type: string
    """
    request_data = request.get_json()
    user = request_data.get("username")
    password = request_data.get("password")

    if not user or not password:
        return {"error": "missing user or password"}, 400

    with InjectorFactory() as factory:
        user = factory.user_service().get_user_by_email(user)

        if not user:
            return {"error": "wrong user email or password "}, 401

        token = factory.auth_service().user_login(user, password)

    return {"token": token}, 200


@auth_controller.route("/verify-token", methods=["POST"])
def verify_token():
    request_data = request.get_json()
    token = request_data.get("token")

    if not token:
        return {"error": "missing token"}, 400

    with InjectorFactory() as factory:
        user = factory.auth_service().verify_token(token)

        if not user:
            return {"error": "invalid token"}, 401

    return {"user": user}, 200
