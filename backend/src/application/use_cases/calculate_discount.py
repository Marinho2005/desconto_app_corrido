from src.domain.entities.discount import DiscountCalculation
from src.models.discount_model import DiscountRequest, DiscountResponse


class CalculateDiscountUseCase:
    """Orquestra o cálculo de desconto sem depender do transporte HTTP."""

    COUPON_EXTRA10 = "EXTRA10"
    COUPON_BONUS = 10.0

    def execute(self, request: DiscountRequest) -> DiscountResponse:
        percentage = request.discount_percentage
        coupon_applied = None

        if request.cupom == self.COUPON_EXTRA10:
            percentage += self.COUPON_BONUS
            coupon_applied = request.cupom

        calculation = DiscountCalculation(request.original_price, percentage)
        return DiscountResponse(
            original_price=calculation.original_price,
            discount_percentage=calculation.percentage,
            discount_amount=calculation.amount,
            final_price=calculation.final_price,
            cupom_applied=coupon_applied,
        )
