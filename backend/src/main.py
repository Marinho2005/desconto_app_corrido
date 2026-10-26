from src.controllers.discount_controller import DiscountController
from src.models.discount_model import DiscountRequest


def main() -> None:
    """Demonstra o fluxo main -> controller -> use case -> domínio."""
    controller = DiscountController()
    request = DiscountRequest(
        original_price=100.0,
        discount_percentage=15.0,
        cupom="EXTRA10",
    )
    result = controller.calculate(request)
    print(f"Valor original: R$ {result.original_price:.2f}")
    print(f"Desconto aplicado: {result.discount_percentage:.2f}%")
    print(f"Valor final: R$ {result.final_price:.2f}")


if __name__ == "__main__":
    main()
