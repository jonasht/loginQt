from PyQt6.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame,
    QLabel, QLineEdit, QPushButton, QCheckBox
    
)

import sys
from PyQt6.QtCore import Qt
import util as u

CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
RIGHT = Qt.AlignmentFlag.AlignRight

class W_recuperarConta(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        
        layout_main = QVBoxLayout()
        layout_container = QVBoxLayout()
        frame_container = QFrame()
        frame_container.setLayout(layout_container)

        layout_cima = QHBoxLayout()
        layout_meio = QGridLayout()
        layout_baixo = QGridLayout()

        # titulo 
        frame_titulo = QFrame()
        layout_titulo = QHBoxLayout()
        
        self.lb_titulo = QLabel('Conta')

        layout_titulo.addWidget(self.lb_titulo)
        frame_titulo.setLayout(layout_titulo)
        self.lb_titulo.setStyleSheet(u.TopTitle.label)
        self.lb_titulo.setAlignment(CENTER)
        frame_titulo.setStyleSheet(u.TopTitle.frame)
        
        layout_container.setContentsMargins(12, 0, 12, 12)
        frame_container.setFixedHeight(600)
        frame_container.setFixedWidth(500)

        layout_cima.addWidget(frame_titulo)
        
        frame_titulo.setFixedHeight(80)
        frame_titulo.setFixedWidth(250)

        # email
        self.lb_email = QLabel('Email:')
        self.le_email = QLineEdit()
        self.lb_email.setAlignment(RIGHT | CENTER)
        
        # botao recuperar senha
        self.bt_recuperarSenha = QPushButton('Recuperar senha')
        self.bt_recuperarSenha.setObjectName(u.SUCCESS)
        
        # senha
        self.lb_senha = QLabel('Senha:')
        self.le_senha = QLineEdit()
        self.lb_senha.setAlignment(CENTER | RIGHT)
        # botao copiar senha
        self.bt_copiar = QPushButton('Copiar')
        self.bt_copiar.setObjectName(u.INFO)

        layout_meio.addWidget(self.lb_email, 0, 0)
        layout_meio.addWidget(self.le_email, 0, 1)
        layout_meio.addWidget(self.bt_recuperarSenha, 1, 0, 1, 2)
        layout_meio.addWidget(self.lb_senha, 2, 0)
        layout_meio.addWidget(self.le_senha, 2, 1)
        layout_meio.addWidget(self.bt_copiar, 3, 1)

        
        # botao voltar
        self.bt_voltar = QPushButton('Voltar')
        self.bt_voltar.setObjectName(u.PRIMARY)
        layout_baixo.addWidget(self.bt_voltar)
        

        # colocando layouts
        layout_container.addLayout(layout_cima)
        layout_container.addStretch()
        layout_container.addLayout(layout_meio)
        layout_container.addStretch()
        layout_container.addLayout(layout_baixo)
        layout_main.addWidget(frame_container, 0, CENTER)
        self.setLayout(layout_main)

    # esc to exit
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close() 
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_recuperarConta()
    window.setGeometry(100, 100, 800, 800)

    window.show()
    app.setStyleSheet(u.get_style())
    sys.exit(app.exec())