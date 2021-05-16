from typing import Optional

from config import Config
from db import SESSION
from fastapi import Cookie, status
from fastapi.responses import Response
from loguru import logger
from models.models import Cart, Item
from pydantic import BaseModel
from sqlalchemy_get_or_create import get_or_create, update_or_create


class Payload(BaseModel):
    external_id: str
    name: Optional[str]
    value: Optional[int]


DOC = {
    status.HTTP_204_NO_CONTENT: {
        "description": "API response successfully",
    },
    400: {
        "description": "Invalid query",
        "content": {"text/plain": {"example": "Bad Request"}},
    },
}


async def create_or_update_item(payload: Payload, cart_id: Optional[str] = Cookie(None)) -> Response:
    try:
        cart, _ = get_or_create(SESSION, Cart, id=cart_id)
        data = payload.dict()
        data["cart_id"] = cart.id
        external_id = data.pop("external_id")
        update_or_create(SESSION, Item, data, external_id=external_id, cart_id=cart_id)
        SESSION.commit()
        response = Response(status_code=status.HTTP_204_NO_CONTENT)
        if not cart_id:
            response.set_cookie(key="cart_id", value=cart.id, max_age=Config.COOKIE_MAX_AGE)
        return response
    except Exception as error:
        SESSION.rollback()
        logger.error(error)
        return Response(status_code=400)
