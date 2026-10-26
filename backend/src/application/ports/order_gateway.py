from typing import Protocol

from src.domain.entities.order import Order


class OrderGateway(Protocol):
    """Contrato usado pelos casos de uso para persistir pedidos."""

    def save(self, order: Order) -> Order:
        ...

    def list_all(self) -> list[Order]:
        ...
