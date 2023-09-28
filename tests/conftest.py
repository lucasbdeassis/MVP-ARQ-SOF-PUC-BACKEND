from contextlib import contextmanager

import pytest
from sqlalchemy import create_engine

from hermes.adapters.transaction_repository import TransactionRepository
from hermes.adapters.user_repository import UserRepository
from hermes.api import create_app
from hermes.application.auth_service import AuthService
from hermes.application.transaction_service import TransactionService
from hermes.application.user_service import UserService

DB_URL = "postgresql://postgres:postgres@localhost:5432/hermes"

engine = create_engine(DB_URL, echo=False)


@contextmanager
def db_connection():
    connection = engine.connect()
    try:
        yield connection
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.rollback()
        connection.close()


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def conn():
    with db_connection() as connection:
        yield connection


@pytest.fixture(scope="session")
def transaction_repository(conn):
    yield TransactionRepository(conn)


@pytest.fixture(scope="session")
def transaction_service(transaction_repository):
    yield TransactionService(transaction_repository, "nubank_service")


@pytest.fixture(scope="session")
def user_repository(conn):
    yield UserRepository(conn)


@pytest.fixture(scope="session")
def user_service(user_repository):
    yield UserService(user_repository)


@pytest.fixture(scope="session")
def auth_service():
    yield AuthService()


@pytest.fixture(scope="session")
def api_token(client):
    response = client.post(
        "/login", json={"username": "admin@admin.com", "password": "123456"}
    )
    return response.json["token"]
