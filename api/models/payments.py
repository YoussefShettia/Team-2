from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)
    card_last4 = Column(String(4))                      # never store the full number
    payment_type = Column(String(20), nullable=False)   # credit, debit, cash
    transaction_status = Column(String(20), nullable=False, default="Pending")

    order = relationship("Order")  # one-way, so orders.py needs no changes