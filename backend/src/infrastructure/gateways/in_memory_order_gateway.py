from src.domain.entities.order import Order


class InMemoryOrderGateway:
    """Gateway simples para persistir pedidos durante a execução."""

    def __init__(self) -> None:
        self._orders: list[Order] = []

    def save(self, order: Order) -> Order:
        self._orders.append(order)
        return order

    def list_all(self) -> list[Order]:
        return list(self._orders)
