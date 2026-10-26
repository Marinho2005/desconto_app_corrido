from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    """Entidade de domínio que representa um pedido calculado."""

    original_price: float
    discount_percentage: float
    final_price: float
    cupom: str | None = None
