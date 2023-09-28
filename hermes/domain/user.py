from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str
    password: str
    dependent: Optional[str] = None
    nubank_refresh_token: Optional[str] = None
    nubank_cert: Optional[bytes] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        from_attributes = True
        extra = "ignore"
        populate_by_name = True
        use_enum_values = True
        exclude_unset = True
