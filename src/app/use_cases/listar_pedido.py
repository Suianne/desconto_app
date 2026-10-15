from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO


class ListarPedidos:
    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self) -> list[CriarPedidoOutputDTO]:
        pedidos = self.pedido_gateway.listar()

        return [
            CriarPedidoOutputDTO(
                cliente=registro["pedido"].cliente,
                valor_original=registro["pedido"].valor_original,
                valor_desconto=registro["pedido"].valor_desconto(),
                valor_final=registro["pedido"].valor_final(),
                tipo_desconto=registro["tipo_desconto"]
            )
            for registro in pedidos
        ]