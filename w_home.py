from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QFrame, QCheckBox, QTextEdit
)
import sys
from PyQt6.QtCore import Qt
import util as u
from style import *
import bancoDeDados as bd



CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
RIGHT = Qt.AlignmentFlag.AlignRight
from w_homePicture import W_homePicture

class W_home (QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        frame_container = QFrame()
        layout_container = QVBoxLayout()
        layout_cima = QVBoxLayout()
        layout_meio = QHBoxLayout()
        layout_bts = QHBoxLayout()
        layout_baixo = QVBoxLayout()

        # titulo
        frame_titulo = QFrame()
        layout_titulo = QVBoxLayout()
        
        self.lb_titulo = QLabel('HOME')
        layout_titulo.addWidget(self.lb_titulo, 0, CENTER)
        frame_titulo.setLayout(layout_titulo)
        layout_cima.addWidget(frame_titulo, 0, CENTER_TOP)
        frame_titulo.setObjectName(INFO)
        frame_titulo.setStyleSheet(u.TopTitle.frame)
        self.lb_titulo.setStyleSheet(u.TopTitle.label)
        frame_titulo.setFixedWidth(250)
        frame_titulo.setFixedHeight(80)
        
        # widget profile picture ------------------------------
        layout_esquerdo = QVBoxLayout()
        self.w_picture = W_homePicture()
        layout_esquerdo.addWidget(self.w_picture)
        layout_meio.addLayout(layout_esquerdo)

        
        # mensagem =================================
        layout_direito = QVBoxLayout()
        self.lb_te = QLabel('Mensagem:')
        self.te_mensagem = QTextEdit()
        layout_direito.addWidget(self.lb_te)
        layout_direito.addWidget(self.te_mensagem)


        # botoes ---------------------------------------
        
        self.bt_editar = QPushButton('Editar')
        self.bt_editar.setObjectName(PRIMARY)
        
        layout_bts.addWidget(self.bt_editar)
        layout_direito.addLayout(layout_bts)
        layout_meio.addLayout(layout_direito)
        
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
        
        
    def start(self, id):
        # set start home picture, picture e nome
        self.w_picture.start(id)
        
        dados_dict = bd.get_usuarioByID(id)
        self.id = id

        nome = dados_dict['nome']
        email = dados_dict['email']
        senha = dados_dict['senha']
        self.mensagem = dados_dict['mensagem']

        self.te_mensagem.setText(self.mensagem)
        

        print('dados:')
        print(dados_dict)
        self.te_mensagem.setDisabled(True)

    def change_les(self):
        print('mudar')
        if self.te_mensagem.isEnabled():
            self.te_mensagem.setEnabled(False)

            self.bt_editar.setText('Editar')
            self.bt_editar.setObjectName(PRIMARY)
            # self.bt_editar.style().unpolish(self.bt_editar)
            self.bt_editar.style().polish(self.bt_editar) #type:ignore
        else:
            self.te_mensagem.setEnabled(True)
            
            self.bt_editar.setText('Confirmar')
            self.bt_editar.setObjectName(SUCCESS)
            # self.bt_editar.style().unpolish(self.bt_editar)
            self.bt_editar.style().polish(self.bt_editar) #type:ignore
            
        mensagem_nova = self.te_mensagem.toPlainText()
        print('mensagem nova')
        print(mensagem_nova)
        if mensagem_nova != self.mensagem:
            bd.update_mensagem(self.id, mensagem_nova)


            
        
    
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
