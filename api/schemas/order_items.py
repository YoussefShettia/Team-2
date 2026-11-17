from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class OrderItemBase(BaseModel):
    quantity: int


class OrderItemCreate(OrderItemBase):
    order_id: int
    sandwich_id: int


class OrderItemUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    quantity: Optional[int] = None


class OrderItem(OrderItemBase):
    id: int
    order_id: int
    sandwich: Sandwich = None

    class ConfigDict:
        from_attributes = True
