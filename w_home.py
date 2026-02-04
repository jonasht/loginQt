from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QFrame, QCheckBox,
)
import sys
from PyQt6.QtCore import Qt
import util as u
from style import *
import bd


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
        layout_bts = QHBoxLayout()
        layout_baixo = QVBoxLayout()

        # titulo
        frame_titulo = QFrame()
        layout_titulo = QVBoxLayout()
        
        self.lb_titulo = QLabel('Cadastro')
        layout_titulo.addWidget(self.lb_titulo, 0, CENTER)
        frame_titulo.setLayout(layout_titulo)
        layout_cima.addWidget(frame_titulo, 0, CENTER_TOP)
        frame_titulo.setObjectName(INFO)
        frame_titulo.setStyleSheet(u.TopTitle.frame)
        self.lb_titulo.setStyleSheet(u.TopTitle.label)
        frame_titulo.setFixedWidth(250)
        frame_titulo.setFixedHeight(80)
        
        # id =
        self.lb_id = QLabel('ID:')
        self.lb_idShow = QLabel('001')
        layout_meio.addWidget(self.lb_id,0,0)
        layout_meio.addWidget(self.lb_idShow,0,1)
        
        # nome
        self.lb_nome = QLabel('Nome:')
        self.le_nome = QLineEdit()
        self.lb_nome.setAlignment(RIGHT|CENTER)
        layout_meio.addWidget(self.lb_nome, 1, 0)
        layout_meio.addWidget(self.le_nome, 1, 1)
        
        # email
        self.lb_email = QLabel('Email:')
        self.le_email = QLineEdit()
        self.lb_email.setAlignment(RIGHT|CENTER)
        layout_meio.addWidget(self.lb_email, 2, 0)
        layout_meio.addWidget(self.le_email, 2, 1)

        # usuario / login
        self.lb_usuario = QLabel('Usuario:')
        self.le_usuario = QLineEdit()
        layout_meio.addWidget(self.lb_usuario,3,0)
        layout_meio.addWidget(self.le_usuario, 3, 1)

        # senha
        self.lb_senha = QLabel('Senha:')
        self.le_senha = QLineEdit()
        self.cb_senha = QCheckBox()
        self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.cb_senha.stateChanged.connect(self.show_password)
        self.lb_senha.setAlignment(RIGHT|CENTER)

        layout_meio.addWidget(self.lb_senha, 4, 0)
        layout_meio.addWidget(self.le_senha, 4, 1)
        layout_meio.addWidget(self.cb_senha, 4, 3)


        # botoes ---------------------------------------
        
        self.bt_editar = QPushButton('Editar')
        self.bt_editar.setObjectName(PRIMARY)
        
        layout_bts.addWidget(self.bt_editar)
        layout_meio.addLayout(layout_bts, 5, 1)
        # botao voltar --------------------------------
        self.bt_voltar = QPushButton('Voltar')
        self.bt_voltar.setObjectName(PRIMARY)
        layout_baixo.addWidget(self.bt_voltar)
        
        # colocando frames e layouts
        frame_container.setLayout(layout_container)
        layout_container.setContentsMargins(12, 0, 12, 12)
        layout_container.addLayout(layout_cima)
        layout_container.addStretch()
        layout_container.addLayout(layout_meio)
        # layout_container.addLayout(layout_bts)
        layout_container.addStretch()
        layout_container.addLayout(layout_baixo)

        layout_main.addWidget(frame_container)
        self.setLayout(layout_main)
        
        self.bt_editar.clicked.connect(self.change_les)
        
        self.start()
        
    def start(self):
        self.le_nome.setText(bd.NOME)
        self.le_email.setText(bd.EMAIL)
        self.le_senha.setText(bd.SENHA)

        self.le_nome.setDisabled(True)
        self.le_email.setDisabled(True)
        self.le_senha.setDisabled(True)
        

    def change_les(self):
        print('mudar')
        print(self.le_nome.isEnabled())
        if self.le_nome.isEnabled():
            self.le_nome.setEnabled(False)
            self.le_email.setEnabled(False)
            self.le_senha.setEnabled(False)
            self.bt_editar.setText('Editar')
            self.bt_editar.setObjectName(PRIMARY)
            # self.bt_editar.style().unpolish(self.bt_editar)
            self.bt_editar.style().polish(self.bt_editar)
        else:
            self.le_nome.setEnabled(True)
            self.le_email.setEnabled(True)
            self.le_senha.setEnabled(True)
            self.bt_editar.setText('Confirmar')
            self.bt_editar.setObjectName(SUCCESS)
            # self.bt_editar.style().unpolish(self.bt_editar)
            self.bt_editar.style().polish(self.bt_editar)


    def show_password(self):
        if self.cb_senha.isChecked():
            self.le_senha.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)
            
        
    
    def keyPressEvent(self, event): #type:ignore
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Wcadastro()
    window.setGeometry(100, 100, 1200, 1000)
    window.show()
    app.setStyleSheet(get_style())
    sys.exit(app.exec())
