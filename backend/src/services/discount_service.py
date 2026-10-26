from src.application.use_cases.calculate_discount import CalculateDiscountUseCase
from src.models.discount_model import DiscountRequest, DiscountResponse


class DiscountService:
    """Camada de aplicação responsável pelo cálculo de descontos."""

    @classmethod
    def calculate_discount(cls, request: DiscountRequest) -> DiscountResponse:
        return CalculateDiscountUseCase().execute(request)
