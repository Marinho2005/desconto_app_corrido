from fastapi import APIRouter

from src.models.discount_model import DiscountRequest, DiscountResponse
from src.services.discount_service import DiscountService


router = APIRouter(tags=["Discounts"])


@router.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    """Calcula o desconto usando a camada de serviços."""
    return DiscountService.calculate_discount(request)
