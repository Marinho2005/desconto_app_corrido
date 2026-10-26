from src.application.use_cases.order_use_cases import (
    CreateOrderUseCase,
    ListOrdersUseCase,
)
from src.domain.entities.order import Order
from src.models.discount_model import DiscountRequest


class OrderController:
    """Encaminha as operações de pedidos para os casos de uso."""

    def __init__(
        self,
        create_order: CreateOrderUseCase,
        list_orders: ListOrdersUseCase,
    ) -> None:
        self.create_order = create_order
        self.list_orders = list_orders

    def create(self, request: DiscountRequest) -> Order:
        return self.create_order.execute(request)

    def list(self) -> list[Order]:
        return self.list_orders.execute()
