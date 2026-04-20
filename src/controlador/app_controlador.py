from controlador.controlador_base import ControladorBase
from controlador.login_cadastro_controlador import LoginCadastroControlador
from entidades.usuario_sessao import UsuarioSessao
from interface.aviso import Aviso
from interface.menu_app import MenuApp


class AppControlador(ControladorBase):
    def __init__(self):
        self.usuario_sessao: UsuarioSessao | None = None
        self.login_cadastro_controlador = LoginCadastroControlador()
        self.menu_app = MenuApp()
        self.aviso = Aviso()
        self.opcoes_menu_app = {
            1: lambda: self.aviso.mostrar_tela('Não implementado'),
            2: lambda: self.aviso.mostrar_tela('Não implementado'),
            3: self.logout
        }

    def executar(self) -> None:
        while True:
            self.usuario_sessao = self.login_cadastro_controlador.executar()
            while self.usuario_sessao:
                opcao_menu = self.menu_app.mostrar_tela()
                self.opcoes_menu_app[opcao_menu]()

    def logout(self) -> None:
        self.usuario_sessao = None
