from PyQt6.QtWidgets import (
    QWidget, QApplication,
    QLabel, QLineEdit, QPushButton, 
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame,
    
)
from PyQt6.QtCore import Qt
import sys
import util as u
CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER

class W_login (QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        # Layout principal da janela
        layout_main = QVBoxLayout()

        layout_cima = QHBoxLayout()
        layout_meio = QGridLayout()
        layout_baixo = QGridLayout()

        # 1. Crie o Frame que servirá como container
        frame_main = QFrame()
        
        # titulo
        frame_titulo = QFrame()
        layout_frTitulo = QVBoxLayout()
        
        self.lb_titulo = QLabel('Login')
        
        layout_frTitulo.addWidget(self.lb_titulo, 0, CENTER)
        frame_titulo.setLayout(layout_frTitulo)
        layout_cima.addWidget(frame_titulo, 0, CENTER_TOP)
        self.lb_titulo.setStyleSheet(u.TopTitle.label)
        frame_titulo.setStyleSheet(u.TopTitle.frame)
        frame_titulo.setFixedWidth(250)
        frame_titulo.setFixedHeight(80)

        # usuario 
        self.lb_usuario = QLabel('Usuario:')
        self.le_usuario = QLineEdit()
        layout_meio.addWidget(self.lb_usuario, 0, 0)
        layout_meio.addWidget(self.le_usuario, 0, 1)

        # senha
        self.lb_senha = QLabel('Senha:')
        self.le_senha = QLineEdit()
        self.le_senha.setEchoMode(QLineEdit.EchoMode.Password) # Para esconder a senha
        layout_meio.addWidget(self.lb_senha, 1, 0)
        layout_meio.addWidget(self.le_senha, 1, 1)

        # botoes
        self.bt_entrar = QPushButton('Entrar')
        self.bt_fechar = QPushButton('Fechar')
        
        self.bt_entrar.setObjectName(u.SUCCESS)
        self.bt_fechar.setObjectName(u.DANGER)
        self.bt_entrar.clicked.connect(self.fazer_login)
        self.bt_fechar.clicked.connect(self.close)
        
        
        layout_baixo.addWidget(self.bt_entrar, 0, 0)
        layout_baixo.addWidget(self.bt_fechar, 1, 0)
        
        layout_do_frame = QVBoxLayout()
        layout_do_frame.addLayout(layout_cima)
        layout_do_frame.addStretch()
        layout_do_frame.addLayout(layout_meio)
        layout_do_frame.addStretch()
        
        layout_do_frame.addLayout(layout_baixo)
        layout_do_frame.setContentsMargins(0, 0, 0, 0)
        frame_main.setLayout(layout_do_frame)
        frame_main.setFixedHeight(600)
        frame_main.setFixedWidth(500)

        layout_main.addWidget(frame_main, 0, CENTER)

        self.setLayout(layout_main)
        
    def fazer_login(self):
        usuario = self.le_usuario.text()
        senha = self.le_senha.text()
        print('usuario:', usuario)
        print('senha:', senha)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Escape or event.key() == Qt.Key.Key_Q:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = W_login()
    
    widget.setStyleSheet(u.get_style())
    widget.setGeometry(100, 100, 800, 800)
    widget.show()
    sys.exit(app.exec())
