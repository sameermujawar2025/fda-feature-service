# app/models/transaction_models.py
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TransactionRequest(BaseModel):
    transaction_id: Optional[str] = None
    timestamp: datetime

    user_id: Optional[str] = None
    card_number: Optional[str] = None

    amount: float
    currency: str
    transaction_type: Optional[str] = None
    payment_channel: Optional[str] = None

    device_id: Optional[str] = None
    ip_address: Optional[str] = None

    current_latitude: Optional[float] = None
    current_longitude: Optional[float] = None
    current_country: Optional[str] = None
