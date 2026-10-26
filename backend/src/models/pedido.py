try:
    from src.models.desconto import IDesconto
except ImportError:
    try:
        from models.desconto import IDesconto
    except ImportError:
        from backend.src.models.desconto import IDesconto

class Pedido:
    def __init__(self, valor: float, desconto: IDesconto):
        self.valor = valor
        self.desconto = desconto

    def calcular_total(self) -> float:
        desconto_valor = self.desconto.calcular(self.valor)
        return self.valor - desconto_valor

