from abc import ABC, abstractmethod
import pickle
from typing import Any


class DAOBase(ABC):
    @abstractmethod
    def __init__(self, nome_arquivo: str) -> None:
        self.nome_arquivo = nome_arquivo
        self.dados: dict[str, Any] = {}
        try:
            self.carregar_dados()
        except FileNotFoundError:
            self.salvar_dados()

    def salvar_dados(self) -> None:
        with open(self.nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.dados, arquivo)

    def carregar_dados(self) -> None:
        with open(self.nome_arquivo, 'rb') as arquivo:
            self.dados = pickle.load(arquivo)

    def adicionar(self, identificador: str, entidade: Any) -> None:
        self.dados[identificador] = entidade
        self.salvar_dados()

    def obter(self, identificador: str) -> Any:
        return self.dados.get(identificador)

    def obter_todos(self) -> list[Any]:
        return list(self.dados.values())
