from src.app.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP, IDesconto

class DescontoFactory:
    descontos = {
        "normal": DescontoNormal,
        "vip": DescontoVIP,
        "premium": DescontoPremium
    }

    @classmethod

    def criar(cls, tipo_desconto: str) -> IDesconto:
        tipo = tipo_desconto.lower().strip()
        classe_desconto = cls.descontos.get(tipo)

        if not classe_desconto:
            raise ValueError(f"Tipo de desconto'{tipo_desconto} inválido.")

        return classe_desconto()
        