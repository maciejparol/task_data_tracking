from datetime import datetime

import pytest
from db import SESSION
from models.models import Item
from starlette.testclient import TestClient

from app import APP

ROUTE = "/api/item"

HEADERS = {"Content-Type": "Application/json"}

REQUIRED_FIELD_SETS = [
    (
        {"value": "1", "name": "str"},
        {"detail": [{"loc": ["body", "external_id"], "msg": "field required", "type": "value_error.missing"}]},
    ),
]


@pytest.mark.parametrize("test_input,test_output", REQUIRED_FIELD_SETS)
def test_item_without_required_fields(test_input, test_output) -> None:
    client = TestClient(APP)
    response = client.post("/api/item", json=test_input)
    assert response.status_code == 422
    assert response.json() == test_output


INCORRECT_FIELD_TYPE_SETS = [
    (
        {"external_id": "test1", "value": "test1"},
        {"detail": [{"loc": ["body", "value"], "msg": "value is not a valid integer", "type": "type_error.integer"}]},
    ),
]


@pytest.mark.parametrize("test_input,test_output", INCORRECT_FIELD_TYPE_SETS)
def test_item_incorrect_field_type(test_input, test_output) -> None:
    client = TestClient(APP)
    response = client.post("/api/item", json=test_input)
    assert response.status_code == 422
    assert response.json() == test_output


update_external_id = str(datetime.now())
UPDATE_ITEM_SUCCESS_SETS = [
    (
        {"external_id": update_external_id, "name": "test1", "value": 1},
        204,
        {"external_id": update_external_id, "name": "test2", "value": 2},
        204,
    ),
]


@pytest.mark.parametrize("test_create, create_status_code, test_update, update_status_code", UPDATE_ITEM_SUCCESS_SETS)
def test_item_create_and_update_success(test_create, create_status_code, test_update, update_status_code):
    client = TestClient(APP)
    response_create = client.post("/api/item", json=test_create)
    assert response_create.status_code == create_status_code
    assert (
        SESSION.query(Item).filter_by(cart_id=response_create.cookies.get("cart_id")).one().name == test_create["name"]
    )
    response_update = client.post("/api/item", json=test_update, cookies=response_create.cookies)
    assert response_update.status_code == 204
    assert (
        SESSION.query(Item).filter_by(cart_id=response_create.cookies.get("cart_id")).one().name == test_update["name"]
    )
