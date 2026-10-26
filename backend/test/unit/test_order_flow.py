from src.application.use_cases.order_use_cases import (
    CreateOrderUseCase,
    ListOrdersUseCase,
)
from src.controllers.order_controller import OrderController
from src.infrastructure.gateways.in_memory_order_gateway import InMemoryOrderGateway
from src.models.discount_model import DiscountRequest


def test_order_controller_creates_and_lists_orders() -> None:
    gateway = InMemoryOrderGateway()
    controller = OrderController(
        create_order=CreateOrderUseCase(gateway),
        list_orders=ListOrdersUseCase(gateway),
    )

    created = controller.create(
        DiscountRequest(original_price=100.0, discount_percentage=10.0)
    )

    assert created.final_price == 90.0
    assert controller.list() == [created]
