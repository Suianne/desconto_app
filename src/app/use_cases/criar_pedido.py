from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO
from src.app.factories.desconto_factory import DescontoFactory


class CriarPedido:
    def __init__(self, pedido_gateway: IPedidoGateway):
       self.pedido_gateway = pedido_gateway 

    def executar(self, input_dto: CriarPedidoInputDTO) -> CriarPedidoOutputDTO:
        desconto = DescontoFactory.criar(input_dto.tipo_desconto)

        pedido = Pedido(input_dto.cliente, input_dto.valor_original, desconto)

        self.pedido_gateway.salvar(pedido, input_dto.tipo_desconto)

        return CriarPedidoOutputDTO(
            cliente=input_dto.cliente,
            valor_original=input_dto.valor_original,
            valor_desconto=pedido.valor_desconto(),
            valor_final=pedido.valor_final(),
            tipo_desconto=input_dto.tipo_desconto
        )

    
    