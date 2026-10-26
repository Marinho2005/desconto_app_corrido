from src.application.ports.order_gateway import OrderGateway
from src.application.use_cases.order_use_cases import (
    CreateOrderUseCase,
    ListOrdersUseCase,
)
from src.controllers.order_controller import OrderController
from src.infrastructure.gateways.in_memory_order_gateway import InMemoryOrderGateway
from src.models.discount_model import DiscountRequest


def main() -> None:
    """Demonstra o fluxo completo de criação, cálculo e listagem."""
    gateway: OrderGateway = InMemoryOrderGateway()
    controller = OrderController(
        create_order=CreateOrderUseCase(gateway),
        list_orders=ListOrdersUseCase(gateway),
    )

    controller.create(
        DiscountRequest(original_price=100.0, discount_percentage=15.0, cupom="EXTRA10")
    )
    controller.create(
        DiscountRequest(original_price=200.0, discount_percentage=10.0)
    )

    for index, order in enumerate(controller.list(), start=1):
        print(
            f"Pedido {index}: R$ {order.original_price:.2f} -> "
            f"R$ {order.final_price:.2f} ({order.discount_percentage:.2f}% de desconto)"
        )


if __name__ == "__main__":
    main()
