from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.presenters.pedido_presenter import PedidoPresenter  # Import do Presenter adicionado

if __name__ == "__main__":
    # 1. Configuração do repositório, caso de uso, presenter e controller
    database = MemoryDatabase()
    repository = MemoryPedidoRepository(database)
    use_case = CriarPedido(repository)
    presenter = PedidoPresenter()  # Instância do Presenter criada
    
    # O Controller agora recebe o Use Case e o Presenter
    controller = PedidoController(criar_pedido_use_case=use_case, presenter=presenter)

    # 2. Execução das ações através do Controller e Use Case
    p1 = controller.criar_pedido(cliente="Cliente 1", valor_original=100.0, tipo_desconto="normal")
    p2 = controller.criar_pedido(cliente="Cliente 2", valor_original=100.0, tipo_desconto="vip")
    p3 = controller.criar_pedido(cliente="Cliente 3", valor_original=100.0, tipo_desconto="premium")

    print("--- Pedidos Criados ---")
    print(p1)
    print(p2)
    print(p3)

    # 3. Listar ou processar os pedidos criados
    print("\n--- Lista de Todos os Pedidos ---")
    pedidos = controller.listar_pedidos()
    print(pedidos)