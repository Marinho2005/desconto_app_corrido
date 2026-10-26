from src.application.use_cases.calculate_discount import CalculateDiscountUseCase
from src.models.discount_model import DiscountRequest, DiscountResponse


class DiscountController:
    """Traduz a entrada externa e encaminha para o caso de uso."""

    def __init__(self, use_case: CalculateDiscountUseCase | None = None) -> None:
        self.use_case = use_case or CalculateDiscountUseCase()

    def calculate(self, request: DiscountRequest) -> DiscountResponse:
        return self.use_case.execute(request)
