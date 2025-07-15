from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QFrame, QCheckBox,
)
import sys
from PyQt6.QtCore import Qt
import util as u

CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
RIGHT = Qt.AlignmentFlag.AlignRight

class Wcadastro (QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        frame_container = QFrame()
        layout_container = QVBoxLayout()
        
        layout_cima = QVBoxLayout()
        layout_meio = QGridLayout()
        layout_bts = QGridLayout()
        layout_baixo = QVBoxLayout()

        # titulo
        frame_titulo = QFrame()
        layout_titulo = QVBoxLayout()
        
        self.lb_titulo = QLabel('Cadastro')
        layout_titulo.addWidget(self.lb_titulo, 0, CENTER)
        frame_titulo.setLayout(layout_titulo)
        layout_cima.addWidget(frame_titulo, 0, CENTER_TOP)
        frame_titulo.setObjectName(u.INFO)
        frame_titulo.setStyleSheet(u.TopTitle.frame)
        self.lb_titulo.setStyleSheet(u.TopTitle.label)
        frame_titulo.setFixedWidth(250)
        frame_titulo.setFixedHeight(80)
        
        # nome
        self.lb_nome = QLabel('Nome:')
        self.le_nome = QLineEdit()
        self.lb_nome.setAlignment(RIGHT|CENTER)
        layout_meio.addWidget(self.lb_nome, 0, 0)
        layout_meio.addWidget(self.le_nome, 0, 1)
        
        # email
        self.lb_email = QLabel('Email:')
        self.le_email = QLineEdit()
        self.lb_email.setAlignment(RIGHT|CENTER)
        layout_meio.addWidget(self.lb_email, 1, 0)
        layout_meio.addWidget(self.le_email, 1, 1)

        # senha
        self.lb_senha = QLabel('Senha:')
        self.le_senha = QLineEdit()
        self.cb_senha = QCheckBox()
        self.lb_senha.setAlignment(RIGHT|CENTER)

        layout_meio.addWidget(self.lb_senha, 2, 0)
        layout_meio.addWidget(self.le_senha, 2, 1)
        layout_meio.addWidget(self.cb_senha, 2, 3)

        # reSenha 
        self.lb_reSenha = QLabel('Redigite a Senha:')
        self.le_reSenha = QLineEdit()
        self.lb_reSenha.setAlignment(RIGHT|CENTER)
        
        layout_meio.addWidget(self.lb_reSenha, 3, 0)
        layout_meio.addWidget(self.le_reSenha, 3, 1)        

        # botoes
        self.bt_cadastrar = QPushButton('Cadastrar')
        self.bt_resetar = QPushButton('Resetar')
        self.bt_cadastrar.setObjectName(u.SUCCESS)
        self.bt_resetar.setObjectName(u.WARNING)
        
        layout_bts.addWidget(self.bt_resetar, 0, 0)
        layout_bts.addWidget(self.bt_cadastrar, 0, 1)

        # botao voltar
        self.bt_voltar = QPushButton('Voltar')
        self.bt_voltar.setObjectName(u.PRIMARY)
        layout_baixo.addWidget(self.bt_voltar)
        
        # colocando frames e layouts
        frame_container.setLayout(layout_container)
        layout_container.setContentsMargins(12, 0, 12, 12)
        layout_container.addLayout(layout_cima)
        layout_container.addStretch()
        layout_container.addLayout(layout_meio)
        layout_container.addLayout(layout_bts)
        layout_container.addStretch()
        layout_container.addLayout(layout_baixo)

        layout_main.addWidget(frame_container)
        self.setLayout(layout_main)
        
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Wcadastro()
    window.setGeometry(100, 100, 800, 800)

    window.show()
    app.setStyleSheet(u.get_style())
    sys.exit(app.exec())
