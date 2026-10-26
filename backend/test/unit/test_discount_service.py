import pytest
from src.models.discount_model import DiscountRequest
from src.services.discount_service import DiscountService

def test_calculate_simple_discount():
    req = DiscountRequest(original_price=100.0, discount_percentage=10.0)
    res = DiscountService.calculate_discount(req)

    assert res.original_price == 100.0
    assert res.discount_percentage == 10.0
    assert res.discount_amount == 10.0
    assert res.final_price == 90.0

def test_calculate_discount_with_coupon():
    req = DiscountRequest(original_price=200.0, discount_percentage=10.0, cupom="EXTRA10")
    res = DiscountService.calculate_discount(req)

    # 10% + 10% bonus = 20%
    assert res.discount_percentage == 20.0
    assert res.discount_amount == 40.0
    assert res.final_price == 160.0
    assert res.cupom_applied == "EXTRA10"

