from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class CreateTransactionSchema(BaseModel):
    time: date
    amount: int
    description: str
    category: str
    comments: Optional[str] = None
    paid_by: Optional[str] = "user"
    will_pay: Optional[str] = "user"
    installment_purchase: Optional[bool] = False
    installments: Optional[int] = None
    installment: Optional[int] = None
    installment_amount: Optional[int] = None


class UpdateTransactionSchema(BaseModel):
    time: Optional[datetime] = None
    amount: Optional[int] = None
    description: Optional[str] = None
    category: Optional[str] = None
    comments: Optional[str] = None
    paid_by: Optional[str] = None
    will_pay: Optional[str] = None
    installment_purchase: Optional[bool] = None
    installments: Optional[int] = None
    installment: Optional[int] = None
    installment_amount: Optional[int] = None
