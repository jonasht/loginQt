from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QFrame, QCheckBox,
)
import sys
from PyQt6.QtCore import Qt
import util as u
from style import *
import bancoDeDados as bd


CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
RIGHT = Qt.AlignmentFlag.AlignRight
RIGHT_CENTER = RIGHT|CENTER

class W_home (QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        frame_container = QFrame()
        layout_container = QVBoxLayout()
        
        layout_cima = QVBoxLayout()
        layout_meio = QVBoxLayout()
        
        layout_meio1 = QGridLayout()
        layout_meio2 = QGridLayout()

        layout_bts = QHBoxLayout()
        layout_baixo = QVBoxLayout()

        
        # id =======================================
        self.lb_id = QLabel('ID:')
        self.lb_idShow = QLabel('')
        self.lb_idShow.setObjectName(INFO)
        layout_meio1.addWidget(self.lb_id,0,0)
        layout_meio1.addWidget(self.lb_idShow,0,1)
        
        # nome ====================================
        self.lb_nome = QLabel('Nome:')
        self.le_nome = QLineEdit()
        layout_meio1.addWidget(self.lb_nome, 1, 0)
        layout_meio1.addWidget(self.le_nome, 1, 1)
        
        # email =======================================
        self.lb_email = QLabel('Email:')
        self.le_email = QLineEdit()
        layout_meio1.addWidget(self.lb_email, 2, 0)
        layout_meio1.addWidget(self.le_email, 2, 1)

        # usuario / login =============================
        self.lb_usuario = QLabel('Usuario:')
        self.le_usuario = QLineEdit()
        layout_meio2.addWidget(self.lb_usuario,1,0)
        layout_meio2.addWidget(self.le_usuario, 1, 1)

        # senha
        self.lb_senha = QLabel('Senha:')
        self.le_senha = QLineEdit()
        self.cb_senha = QCheckBox()
        self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.cb_senha.stateChanged.connect(self.show_password)

        layout_meio2.addWidget(self.lb_senha, 2, 0)
        layout_meio2.addWidget(self.le_senha, 2, 1)
        layout_meio2.addWidget(self.cb_senha, 2, 3)


        # botoes ---------------------------------------
        self.bt_editar = QPushButton('Editar')
        self.bt_editar.setObjectName(PRIMARY)
        
        layout_bts.addWidget(self.bt_editar)
        # botao voltar --------------------------------
        self.bt_voltar = QPushButton('Voltar')
        self.bt_voltar.setObjectName(PRIMARY)
        layout_baixo.addWidget(self.bt_voltar)
        
        # colocando frames e layouts
        frame_container.setLayout(layout_container)
        layout_container.setContentsMargins(12, 0, 12, 12)
        layout_container.addLayout(layout_cima)
        layout_container.addStretch()
        layout_meio.addLayout(layout_meio1)
        layout_meio.addStretch()
        layout_meio.addLayout(layout_meio2)
        layout_meio.addLayout(layout_bts)
        
        layout_container.addLayout(layout_meio)
        # layout_container.addLayout(layout_bts)
        layout_container.addStretch()
        layout_container.addLayout(layout_baixo)

        layout_main.addWidget(frame_container)
        self.setLayout(layout_main)
        
        self.bt_editar.clicked.connect(self.change_les)
        
        self.set_aligment_labels()
        
    def set_aligment_labels(self):
        
        self.lb_id.setAlignment(RIGHT_CENTER)
        self.lb_email.setAlignment(RIGHT_CENTER)
        self.lb_nome.setAlignment(RIGHT_CENTER)
        self.lb_usuario.setAlignment(RIGHT_CENTER)
        self.lb_senha.setAlignment(RIGHT_CENTER)
    
    def start(self, id):
        dados_dict = bd.get_usuarioByID(id)
        
        id = str(dados_dict['id'])
        nome = dados_dict['nome']
        email = dados_dict['email']
        usuario = dados_dict['usuario']
        senha = dados_dict['senha']

        self.lb_idShow.setText(id)
        self.le_nome.setText(nome)
        self.le_email.setText(email)
        self.le_usuario.setText(usuario)
        self.le_senha.setText(senha)

        print('dados:')
        print(dados_dict)
        self.le_nome.setDisabled(True)
        self.le_email.setDisabled(True)
        self.le_senha.setDisabled(True)
        self.le_usuario.setDisabled(True)
        

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
            self.bt_editar.style().polish(self.bt_editar) #type:ignore
        else:
            self.le_nome.setEnabled(True)
            self.le_email.setEnabled(True)
            self.le_senha.setEnabled(True)
            self.bt_editar.setText('Confirmar')
            self.bt_editar.setObjectName(SUCCESS)
            # self.bt_editar.style().unpolish(self.bt_editar)
            self.bt_editar.style().polish(self.bt_editar) #type:ignore


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
    window = W_home()
    window.setGeometry(100, 100, 1200, 1000)
    window.show()
    window.start(2)

    app.setStyleSheet(get_style())
    sys.exit(app.exec())
