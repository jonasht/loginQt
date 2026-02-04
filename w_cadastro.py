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
        
        # nome
        self.lb_usuario = QLabel('Usuario:')
        self.le_usuario = QLineEdit()
        self.lb_usuario.setAlignment(RIGHT|CENTER)
        layout_meio.addWidget(self.lb_usuario, 0, 0)
        layout_meio.addWidget(self.le_usuario, 0, 1)
        
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
        self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.cb_senha.stateChanged.connect(self.show_password)
        self.lb_senha.setAlignment(RIGHT|CENTER)

        layout_meio.addWidget(self.lb_senha, 2, 0)
        layout_meio.addWidget(self.le_senha, 2, 1)
        layout_meio.addWidget(self.cb_senha, 2, 3)

        # reSenha 
        self.lb_reSenha = QLabel('Redigite a Senha:')
        self.le_reSenha = QLineEdit()
        self.le_reSenha.setEchoMode(QLineEdit.EchoMode.Password)
        self.lb_reSenha.setAlignment(RIGHT|CENTER)
        
        layout_meio.addWidget(self.lb_reSenha, 3, 0)
        layout_meio.addWidget(self.le_reSenha, 3, 1)        

        # botoes ---------------------------------------
        
        self.bt_cadastrar = QPushButton('Cadastrar')
        self.bt_resetar = QPushButton('Resetar')
        self.bt_cadastrar.setObjectName(SUCCESS)
        self.bt_resetar.setObjectName(WARNING)
        
        layout_bts.addWidget(self.bt_resetar)
        layout_bts.addWidget(self.bt_cadastrar)
        layout_meio.addLayout(layout_bts, 4, 1)
        
        # label aviso --------------------------------------
        self.lb_aviso = QLabel('aviso....')
        layout_meio.addWidget(self.lb_aviso, 5, 1, 1, 3)
        self.lb_aviso.setAlignment(CENTER)

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
        
        self.setsys_style()
        
        # botao comando
        self.bt_cadastrar.clicked.connect(self.cadastrar)
    
    def setsys_style(self):
        self.le_usuario.setObjectName(SECONDARY)
        self.le_senha.setObjectName(SECONDARY)
        self.le_reSenha.setObjectName(SECONDARY)
        self.le_email.setObjectName(SECONDARY)
        self.cb_senha.setObjectName(SECONDARY)
        
    def cadastrar(self):
        usuario = self.le_usuario.text()
        email = self.le_email.text()
        senha1 = self.le_senha.text()
        senha2 = self.le_reSenha.text()

        preencharTdCamposQ = False
        if not usuario:
            self.le_usuario.setObjectName(DANGER)
            self.le_usuario.style().polish(self.le_usuario) #type:ignore
            # self.le_usuario.style().unpolish(self.le_usuario)
            preencharTdCamposQ = True
        if not email:
            self.le_email.setObjectName(DANGER)
            self.le_email.style().polish(self.le_email) #type:ignore
            preencharTdCamposQ = True
        if not senha1:
            self.le_senha.setObjectName(DANGER)
            self.le_senha.style().polish(self.le_senha) # type:ignore
            preencharTdCamposQ = True
        if not senha2:
            self.le_reSenha.setObjectName(DANGER)
            self.le_reSenha.style().polish(self.le_reSenha) #type:ignore
            preencharTdCamposQ = True
            
        if preencharTdCamposQ:
            self.lb_aviso.setText('preencha todos os campos')
            self.lb_aviso.setObjectName(DANGER)
            self.lb_aviso.style().polish(self.lb_aviso) #type:ignore
        else:
            self.lb_aviso.setText('Cadastro feito com sucesso')
            self.lb_aviso.setObjectName(SUCCESS)
            self.lb_aviso.style().polish(self.lb_aviso) #type:ignore

            print('cadastro feito com sucesso --------------')
            print('usuario:',usuario)
            print('email:',email)
            print('senha1:',senha1)
            print('senha2:',senha2)
            bd.insert_usuario(usuario=usuario, senha=senha1, email=email)
            

    def show_password(self):
        if self.cb_senha.isChecked():
            self.le_senha.setEchoMode(QLineEdit.EchoMode.Normal)
            self.le_reSenha.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)
            self.le_reSenha.setEchoMode(QLineEdit.EchoMode.Password)
        
    
    def keyPressEvent(self, event): #type:ignore
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Wcadastro()
    window.setGeometry(100, 100, 1200, 1000)
    
    window.le_usuario.setText('jonas')
    window.le_email.setText('jonas@email.com')
    window.le_senha.setText('123')
    window.le_reSenha.setText('123')

    window.show()
    app.setStyleSheet(get_style())
    sys.exit(app.exec())
