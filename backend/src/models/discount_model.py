from pydantic import BaseModel, Field


class DiscountRequest(BaseModel):
    original_price: float = Field(gt=0)
    discount_percentage: float = Field(ge=0, le=100)
    cupom: str | None = None


class DiscountResponse(BaseModel):
    original_price: float
    discount_percentage: float
    discount_amount: float
    final_price: float
    cupom_applied: str | None = None
