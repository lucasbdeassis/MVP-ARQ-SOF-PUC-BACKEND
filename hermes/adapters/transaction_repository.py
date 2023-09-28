from pydantic import BaseModel
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql import text

from hermes.domain.transaction import Transaction
from hermes.infra.db import metadata

transactions = Table(
    "transactions",
    metadata,
    Column("id", String, primary_key=True),
    Column("owner_id", String),
    Column("time", DateTime),
    Column("day", Integer),
    Column("month", Integer),
    Column("year", Integer),
    Column("amount", Integer),
    Column("description", String),
    Column("category", String),
    Column("comments", String),
    Column("paid_by", String),
    Column("will_pay", String),
    Column("installment_purchase", Boolean),
    Column("installments", Integer),
    Column("installment", Integer),
    Column("installment_amount", Integer),
    Column("original_transaction_id", String),
    Column("created_at", DateTime, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "updated_at",
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
)


class TransactionRepository:
    conn: Connection

    def __init__(self, conn: Connection):
        self.conn = conn

    def get_transactions_by_month(self, month: int, year: int, user_id: str):
        query = transactions.select().filter_by(
            month=month, year=year, owner_id=user_id
        )
        result = self.conn.execute(query).mappings().all()
        return [Transaction(**row) for row in result]

    def get_all(self, user_id):
        query = transactions.select().filter_by(owner_id=user_id)
        resutl = self.conn.execute(query).mappings().all()
        return [Transaction(**row) for row in resutl]

    def create_transaction(self, obj: BaseModel):
        query = transactions.insert().values(**obj.model_dump())
        self.conn.execute(query)

    def update(self, pk, obj: BaseModel, user_id) -> BaseModel:
        query = (
            transactions.update()
            .where(transactions.c.id == pk)
            .where(transactions.c.owner_id == user_id)
            .values(**obj.model_dump(exclude_unset=True, exclude_none=True))
        )
        self.conn.execute(query)
        return obj

    def get_transaction(self, pk, user_id):
        query = (
            transactions.select()
            .where(transactions.c.id == pk)
            .where(transactions.c.owner_id == user_id)
        )
        result = self.conn.execute(query).mappings().first()
        return Transaction(**result)

    def delete(self, pk, user_id):
        query = (
            transactions.delete()
            .where(transactions.c.id == pk)
            .where(transactions.c.owner_id == user_id)
        )
        self.conn.execute(query)
