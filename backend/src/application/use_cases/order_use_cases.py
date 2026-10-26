from src.application.ports.order_gateway import OrderGateway
from src.application.use_cases.calculate_discount import CalculateDiscountUseCase
from src.domain.entities.order import Order
from src.models.discount_model import DiscountRequest


class CreateOrderUseCase:
    """Cria um pedido, calcula seu desconto e persiste o resultado."""

    def __init__(
        self,
        gateway: OrderGateway,
        calculate_discount: CalculateDiscountUseCase | None = None,
    ) -> None:
        self.gateway = gateway
        self.calculate_discount = calculate_discount or CalculateDiscountUseCase()

    def execute(self, request: DiscountRequest) -> Order:
        discount = self.calculate_discount.execute(request)
        order = Order(
            original_price=discount.original_price,
            discount_percentage=discount.discount_percentage,
            final_price=discount.final_price,
            cupom=request.cupom,
        )
        return self.gateway.save(order)


class ListOrdersUseCase:
    """Lista os pedidos já registrados."""

    def __init__(self, gateway: OrderGateway) -> None:
        self.gateway = gateway

    def execute(self) -> list[Order]:
        return self.gateway.list_all()
