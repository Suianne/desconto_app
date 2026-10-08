from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.frameworks.database.memory_database import MemoryDatabase

if __name__ == "__main__":
   # Configuração do repositório e serviço
   database = MemoryDatabase()
   repository = MemoryPedidoRepository(database)
   use_case = CriarPedido(repository)
   controller = PedidoController(use_case)

    # 2. Execução das ações através do Controller e Use Case
   controller.criar_pedido(cliente="Cliente 1", valor_original=100.0, tipo_desconto="normal")
   controller.criar_pedido(cliente="Cliente 2", valor_original=100.0, tipo_desconto="vip")
   controller.criar_pedido(cliente="Cliente 3", valor_original=100.0, tipo_desconto="premium")

    # 3. Listar ou processar os pedidos criados
   controller.listar_pedidos()
   