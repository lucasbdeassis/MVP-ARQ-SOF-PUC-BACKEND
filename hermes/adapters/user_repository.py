from pydantic import BaseModel
from sqlalchemy import Column, DateTime, String, Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql import text

from hermes.domain.user import User
from hermes.infra.db import metadata

users = Table(
    "users",
    metadata,
    Column("id", String, primary_key=True),
    Column("name", String),
    Column("email", String),
    Column("password", String),
    Column("dependent", String),
    Column("nubank_refresh_token", String),
    Column("nubank_cert", String),
    Column("created_at", DateTime, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "updated_at",
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
)


class UserRepository:
    conn: Connection

    def __init__(self, conn: Connection):
        self.conn = conn

    def get_user_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email == email)
        result = self.conn.execute(query).mappings().first()
        return User(**result) if result else None

    def create_user(self, obj: BaseModel):
        query = users.insert().values(**obj.model_dump())
        self.conn.execute(query)

    def update_user(self, pk, obj: BaseModel) -> BaseModel:
        query = (
            users.update()
            .where(users.c.id == pk)
            .values(**obj.model_dump(exclude_unset=True))
        )
        self.conn.execute(query)
        return obj

    def delete_user(self, pk):
        query = users.delete().where(users.c.id == pk)
        self.conn.execute(query)

    def get_user(self, pk):
        query = users.select().where(users.c.id == pk)
        result = self.conn.execute(query).mappings().first()
        return User(**result) if result else None

    def list_users(self):
        query = users.select()
        result = self.conn.execute(query).mappings().all()
        return [User(**row) for row in result]
