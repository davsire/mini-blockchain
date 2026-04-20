from entidades.bloco import Bloco
from persistencia.dao_base import DAOBase


class BlocoDAO(DAOBase):
    def __init__(self):
        super().__init__('blocos.pkl')

    def salvar_bloco(self, bloco: Bloco) -> None:
        self.adicionar(bloco.id_bloco, bloco)

    def obter_bloco(self, id_bloco: str) -> Bloco | None:
        return self.obter(id_bloco)

    def obter_blocos(self) -> list[Bloco]:
        return self.obter_todos()
