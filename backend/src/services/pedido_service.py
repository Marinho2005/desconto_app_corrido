try:
    from src.models.pedido import Pedido
    from src.repositories.pedido_repository import PedidoRepository
except ImportError:
    try:
        from models.pedido import Pedido
        from repositories.pedido_repository import PedidoRepository
    except ImportError:
        from backend.src.models.pedido import Pedido
        from backend.src.repositories.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, repository: PedidoRepository = None):
        self.repository = repository or PedidoRepository()

    def processar_pedido(self, pedido: Pedido) -> float:
        total = pedido.calcular_total()
        self.repository.salvar(pedido)
        return total

