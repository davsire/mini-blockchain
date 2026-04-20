import qrcode
from criptografia.totp import obter_uri_totp
from interface.interface_base import InterfaceBase


class TotpQrcode(InterfaceBase):
    def __init__(self):
        super().__init__('OTP QRCODE')

    def mostrar_tela(self, chave_totp: str, usuario: str) -> None:
        super().mostrar_tela()

        uri = obter_uri_totp(chave_totp, usuario)
        qr = qrcode.QRCode()
        qr.add_data(uri)
        qr.make()
        qr.print_ascii(invert=True)
        input('Pressione ENTER para continuar...')
