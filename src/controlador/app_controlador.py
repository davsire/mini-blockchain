from controlador.controlador_base import ControladorBase
from controlador.login_cadastro_controlador import LoginCadastroControlador
from entidades.usuario_sessao import UsuarioSessao
from interface.aviso import Aviso
from interface.form_bloco import FormBloco
from interface.lista_blocos import ListaBlocos
from interface.menu_app import MenuApp
from persistencia.bloco_dao import BlocoDAO
from servicos.bloco_servico import BlocoServico


class AppControlador(ControladorBase):
    def __init__(self):
        self.usuario_sessao: UsuarioSessao | None = None
        self.bloco_dao = BlocoDAO()
        self.bloco_servico = BlocoServico(self.bloco_dao)
        self.login_cadastro_controlador = LoginCadastroControlador()
        self.menu_app = MenuApp()
        self.form_bloco = FormBloco()
        self.lista_blocos = ListaBlocos()
        self.aviso = Aviso()

    def executar(self) -> None:
        while True:
            self.usuario_sessao = self.login_cadastro_controlador.executar()
            while self.usuario_sessao:
                try:
                    opcao = self.menu_app.mostrar_tela()
                    if opcao == 1:
                        self.executar_fluxo_adicionar_bloco()
                    elif opcao == 2:
                        self.executar_fluxo_lista_bloco()
                    elif opcao == 3:
                        self.logout()
                except Exception as erro:
                    self.aviso.mostrar_tela(str(erro))

    def executar_fluxo_adicionar_bloco(self) -> None:
        conteudo = self.form_bloco.mostrar_tela()
        self.bloco_servico.criar_bloco(conteudo, self.usuario_sessao)

    def executar_fluxo_lista_bloco(self) -> None:
        bloco_lista = self.bloco_servico.obter_blocos_lista(self.usuario_sessao)
        self.lista_blocos.mostrar_tela(bloco_lista)

    def logout(self) -> None:
        self.usuario_sessao = None
