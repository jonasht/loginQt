from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QFrame
)
import sys
from PyQt6.QtCore import Qt
import util as u

CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
class Wcadastro (QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        layout_cima = QVBoxLayout()
        layout_meio = QGridLayout()
        layout_baixo = QGridLayout()

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
        layout_meio.addWidget(self.lb_nome, 0, 0)
        layout_meio.addWidget(self.le_nome, 0, 1)

        # senha
        self.lb_senha = QLabel('Senha:')
        self.le_senha = QLineEdit()
        layout_meio.addWidget(self.lb_senha, 1, 0)
        layout_meio.addWidget(self.le_senha, 1, 1)

        # reSenha 
        self.lb_reSenha = QLabel('Novamente a Senha:')
        self.le_reSenha = QLineEdit()
        layout_meio.addWidget(self.lb_reSenha, 2, 0)
        layout_meio.addWidget(self.le_reSenha, 2, 1)        

        # botoes
        self.bt_cadastrar = QPushButton('Cadastrar')
        self.bt_resetar = QPushButton('Resetar')
        self.bt_voltar = QPushButton('Voltar')
        self.bt_cadastrar.setObjectName(u.SUCCESS)
        self.bt_resetar.setObjectName(u.DANGER)
        self.bt_voltar.setObjectName(u.PRIMARY)
        
        layout_baixo.addWidget(self.bt_resetar, 0, 0)
        layout_baixo.addWidget(self.bt_cadastrar, 0, 1)
        layout_baixo.addWidget(self.bt_voltar, 1, 0, 1, 2)
        
        layout_main.addLayout(layout_cima)
        layout_main.addStretch()

        layout_main.addLayout(layout_meio)
        layout_main.addStretch()
        layout_main.addLayout(layout_baixo)

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
