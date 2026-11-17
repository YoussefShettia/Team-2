from fastapi.testclient import TestClient
from ..controllers import order_items as controller
from ..main import app
import pytest
from ..models import order_items as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order_item(db_session):
    # Create a sample order item
    order_item_data = {
        "order_id": 1,
        "sandwich_id": 1,
        "quantity": 2
    }

    order_item_object = model.OrderItem(**order_item_data)

    # Call the create function
    created_item = controller.create(db_session, order_item_object)

    # Assertions
    assert created_item is not None
    assert created_item.order_id == 1
    assert created_item.sandwich_id == 1
    assert created_item.quantity == 2
