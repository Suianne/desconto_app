from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.use_cases.listar_pedido import ListarPedidos  # Import do Use Case de listagem
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.adapters.controllers.pedido_controller import PedidoController

if __name__ == "__main__":
   database = MemoryDatabase()
   repository = MemoryPedidoRepository(database)
   criar_uc = CriarPedido(repository)
   listar_uc = ListarPedidos(repository)
   presenter = PedidoPresenter()

   controller = PedidoController(criar_pedido_use_case=criar_uc, listar_pedidos_use_case=listar_uc, presenter=presenter)

   
  # Desconto Normal
p1 = controller.criar_pedido(cliente="Ana Silva", valor_original=150.00, tipo_desconto="normal")

# Desconto VIP
p2 = controller.criar_pedido(cliente="Carlos Oliveira", valor_original=500.00, tipo_desconto="vip")

# Desconto Premium
p3 = controller.criar_pedido(cliente="Empresa Tech LTDA", valor_original=1250.50, tipo_desconto="premium")
   
pedidos = controller.listar_pedidos()
print(pedidos)