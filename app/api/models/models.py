import uuid

from sqlalchemy import INT, VARCHAR, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class Cart(BASE):
    __tablename__ = "cart"

    id = Column(UUID, primary_key=True, default=str(uuid.uuid4()))

    def dumps(self):
        return {"id": self.id}


class Item(BASE):
    __tablename__ = "item"

    id = Column(UUID, primary_key=True, default=str(uuid.uuid4()))
    cart_id = Column(UUID, ForeignKey(Cart.id))
    external_id = Column(VARCHAR, nullable=False, unique=True)
    name = Column(VARCHAR, nullable=True)
    value = Column(INT, nullable=True)

    def dumps(self):
        return {
            "id": self.id,
            "cart_id": self.cart_id,
            "external_id": self.external_id,
            "name": self.name,
            "value": self.value,
        }
