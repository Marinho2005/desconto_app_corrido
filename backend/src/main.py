import sys
import os

# Adiciona o diretório backend e backend/src ao sys.path para suportar qualquer forma de execução
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, current_dir)

try:
    from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
    from src.controllers.pedido_controller import PedidoController
except ImportError:
    try:
        from models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
        from controllers.pedido_controller import PedidoController
    except ImportError:
        from backend.src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
        from backend.src.controllers.pedido_controller import PedidoController

def main():
    controller = PedidoController()
    valor_compra = 100.0

    print(f"Valor original da compra: R$ {valor_compra:.2f}\n")

    total_normal = controller.criar_pedido(valor_compra, DescontoNormal())
    print(f"Total com Desconto Normal (10%): R$ {total_normal:.2f}\n")

    total_vip = controller.criar_pedido(valor_compra, DescontoVIP())
    print(f"Total com Desconto VIP (20%): R$ {total_vip:.2f}\n")

    total_premium = controller.criar_pedido(valor_compra, DescontoPremium())
    print(f"Total com Desconto Premium (30%): R$ {total_premium:.2f}\n")

if __name__ == "__main__":
    main()

