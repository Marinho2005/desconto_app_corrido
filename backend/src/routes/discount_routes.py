from fastapi import APIRouter

from src.controllers.discount_controller import DiscountController
from src.models.discount_model import DiscountRequest, DiscountResponse


router = APIRouter(tags=["Discounts"])
controller = DiscountController()


@router.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    """Calcula o desconto usando a camada de serviços."""
    return controller.calculate(request)
