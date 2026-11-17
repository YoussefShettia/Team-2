from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field
from schemas.order_item import OrderItemRead
from schemas.payment import PaymentRead

class OrderBase(BaseModel):
    user_id: int
    status: str = Field(default="pending", max_length=50)
    delivery_address: str | None = None
    notes: str | None = None

class OrderCreate(OrderBase): pass
class OrderUpdate(BaseModel):
    status: str | None = Field(default=None, max_length=50)
    delivery_address: str | None = None
    notes: str | None = None

class OrderRead(OrderBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    total_amount: Decimal
    created_at: datetime
    updated_at: datetime
    items: list[OrderItemRead] = []
    payment: PaymentRead | None = None