from dataclasses import dataclass


@dataclass(frozen=True)
class DiscountCalculation:
    """Entidade de domínio para uma aplicação de desconto."""

    original_price: float
    percentage: float

    @property
    def amount(self) -> float:
        return self.original_price * self.percentage / 100

    @property
    def final_price(self) -> float:
        return self.original_price - self.amount
