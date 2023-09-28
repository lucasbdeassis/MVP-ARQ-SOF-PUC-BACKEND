from datetime import datetime
from typing import Optional
from uuid import uuid4

from dateutil.relativedelta import relativedelta
from pydantic import BaseModel, model_validator, validator


class Transaction(BaseModel):
    id: str
    owner_id: str
    time: datetime
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    amount: int
    description: str
    category: str
    comments: Optional[str] = None
    paid_by: str = "user"
    will_pay: str = "user"
    installment_purchase: bool = False
    installments: Optional[int] = None
    installment: Optional[int] = None
    installment_amount: Optional[int] = None
    original_transaction_id: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @model_validator(mode="after")
    def get_time_attributes(self):
        if any([self.day, self.month, self.year]):
            assert (
                self.day == self.time.day
                and self.month == self.time.month
                and self.year == self.time.year
            )
            return self
        self.day = self.time.day
        self.month = self.time.month
        self.year = self.time.year
        return self

    @model_validator(mode="after")
    def check_installment_info(self):
        if self.installment_purchase:
            assert self.installments is not None
            assert self.installment is not None
            assert self.original_transaction_id is not None
            assert self.installment_amount is not None
        return self

    @validator("will_pay")
    def validate_will_pay(cls, v):
        if v not in ("user", "partner", "both"):
            raise ValueError("invalid will_pay")
        return v

    @validator("paid_by")
    def validate_paid_by(cls, v):
        if v not in ("user", "partner", "both"):
            raise ValueError("invalid paid_by")
        return v

    def get_installments(self) -> list["Transaction"]:
        if not self.installment_purchase:
            raise Exception("transaction is not an installment purchase")
        installments = []
        for i in range(2, self.installments + 1):
            installment_time = self.time + relativedelta(months=i - 1)
            installments.append(
                Transaction(
                    id=str(uuid4()),
                    time=installment_time,
                    day=installment_time.day,
                    month=installment_time.month,
                    year=installment_time.year,
                    amount=self.amount,
                    description=self.description,
                    category=self.category,
                    comments=self.comments,
                    paid_by=self.paid_by,
                    will_pay=self.will_pay,
                    installment_purchase=self.installment_purchase,
                    installments=self.installments,
                    installment=i,
                    installment_amount=self.installment_amount,
                    original_transaction_id=self.id,
                    created_at=self.created_at,
                    updated_at=self.updated_at,
                )
            )
        return installments
