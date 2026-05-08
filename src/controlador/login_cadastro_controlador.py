from controlador.controlador_base import ControladorBase
from entidades.usuario_sessao import UsuarioSessao
from interface.aviso import Aviso
from interface.form_cadastro import FormCadastro
from interface.form_login import FormLogin
from interface.form_totp import FormTotp
from interface.menu_inicial import MenuInicial
from interface.totp_qrcode import TotpQrcode
from persistencia.usuario_dao import UsuarioDAO
from servicos.usuario_servico import UsuarioServico


class LoginCadastroControlador(ControladorBase):
    def __init__(self):
        self.usuario_dao = UsuarioDAO()
        self.usuario_servico = UsuarioServico(self.usuario_dao)
        self.menu_inicial = MenuInicial()
        self.form_login = FormLogin()
        self.form_totp = FormTotp()
        self.form_cadastro = FormCadastro()
        self.totp_qrcode = TotpQrcode()
        self.aviso = Aviso()

    def executar(self) -> UsuarioSessao:
        while True:
            try:
                opcao = self.menu_inicial.mostrar_tela()
                if opcao == 1:
                    return self.executar_fluxo_login()
                elif opcao == 2:
                    return self.executar_fluxo_cadastro()
                elif opcao == 3:
                    exit()
            except Exception as erro:
                self.aviso.mostrar_tela(str(erro))

    def executar_fluxo_login(self) -> UsuarioSessao:
        usuario, senha = self.form_login.mostrar_tela()
        usuario_sessao = self.usuario_servico.validar_login_senha(usuario, senha)
        totp = self.form_totp.mostrar_tela()
        self.usuario_servico.validar_totp(usuario_sessao, totp)
        return usuario_sessao

    def executar_fluxo_cadastro(self) -> UsuarioSessao:
        usuario, senha = self.form_cadastro.mostrar_tela()
        usuario_sessao = self.usuario_servico.criar_usuario(usuario, senha)
        self.totp_qrcode.mostrar_tela(usuario_sessao.chave_totp, usuario)
        return usuario_sessao
