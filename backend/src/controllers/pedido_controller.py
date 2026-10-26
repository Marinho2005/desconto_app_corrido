try:
    from src.models.pedido import Pedido
    from src.models.desconto import IDesconto
    from src.services.pedido_service import PedidoService
except ImportError:
    try:
        from models.pedido import Pedido
        from models.desconto import IDesconto
        from services.pedido_service import PedidoService
    except ImportError:
        from backend.src.models.pedido import Pedido
        from backend.src.models.desconto import IDesconto
        from backend.src.services.pedido_service import PedidoService

class PedidoController:
    def __init__(self, service: PedidoService = None):
        self.service = service or PedidoService()

    def criar_pedido(self, valor: float, desconto: IDesconto) -> float:
        pedido = Pedido(valor, desconto)
        return self.service.processar_pedido(pedido)

