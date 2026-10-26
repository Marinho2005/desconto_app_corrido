from src.models.discount_model import DiscountRequest, DiscountResponse


class DiscountService:
    """Camada de aplicação responsável pelo cálculo de descontos."""

    COUPON_EXTRA10 = "EXTRA10"
    COUPON_BONUS = 10.0

    @classmethod
    def calculate_discount(cls, request: DiscountRequest) -> DiscountResponse:
        percentage = request.discount_percentage
        coupon_applied = None

        if request.cupom == cls.COUPON_EXTRA10:
            percentage += cls.COUPON_BONUS
            coupon_applied = request.cupom

        discount_amount = request.original_price * percentage / 100
        final_price = request.original_price - discount_amount

        return DiscountResponse(
            original_price=request.original_price,
            discount_percentage=percentage,
            discount_amount=discount_amount,
            final_price=final_price,
            cupom_applied=coupon_applied,
        )
