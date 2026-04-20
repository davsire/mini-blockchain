from abc import ABC, abstractmethod
import os
from typing import Any


class InterfaceBase(ABC):
    def __init__(self, titulo: str):
        self.titulo = titulo

    @abstractmethod
    def mostrar_tela(self, *args) -> Any:
        self.limpar_tela()
        print(f'==== {self.titulo} ====', end='\n\n')

    def limpar_tela(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
