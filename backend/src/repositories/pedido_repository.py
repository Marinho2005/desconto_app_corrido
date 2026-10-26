try:
    from src.database.connection import DBConnection
    from src.models.pedido import Pedido
except ImportError:
    try:
        from database.connection import DBConnection
        from models.pedido import Pedido
    except ImportError:
        from backend.src.database.connection import DBConnection
        from backend.src.models.pedido import Pedido

class PedidoRepository:
    def __init__(self, db_connection: DBConnection = None):
        self.db_connection = db_connection or DBConnection()

    def salvar(self, pedido: Pedido):
        print(f"Pedido com valor R$ {pedido.valor:.2f} e total R$ {pedido.calcular_total():.2f} salvo.")
        return True

