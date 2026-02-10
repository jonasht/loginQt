from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QFrame, QCheckBox, 
)
from PyQt6.QtGui import QPixmap

import sys
from PyQt6.QtCore import Qt
import util as u
from style import *
import bancoDeDados as bd


CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
RIGHT = Qt.AlignmentFlag.AlignRight
RIGHT_CENTER = RIGHT|CENTER

class W_homePicture (QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        frame_container = QFrame()
        layout_container = QVBoxLayout()
        
        layout_meio = QVBoxLayout()
        


        
        # id =======================================
        self.lb_id = QLabel('ID:')
        layout_meio.addWidget(self.lb_id)
        
        # profile picture ====================================
        frame_containerPicture = QFrame()
        layout_containerPicture = QVBoxLayout()
        frame_containerPicture.setLayout(layout_containerPicture)
        frame_containerPicture.setObjectName(INFO_FILL)

        self.pixmap = QPixmap('./profilePictures/vaca.jpg')
        self.pixmap = self.pixmap.scaled(200, 200)
        self.lb_pic = QLabel()
        self.lb_pic.setPixmap(self.pixmap)
        layout_containerPicture.addWidget(self.lb_pic)
        layout_meio.addWidget(frame_containerPicture)

        # nome =============================================
        self.lb_nome = QLabel('Nome:')
        self.lb_nome.setObjectName(INFO)
        self.lb_nome.setAlignment(CENTER)
        layout_meio.addWidget(self.lb_nome)
        
        
        
        # colocando frames e layouts ====================
        frame_container.setLayout(layout_container)
        
        # layout_container.setContentsMargins(12, 0, 12, 12)
        
        layout_container.addStretch()
        layout_meio.addLayout(layout_meio)
        layout_meio.addStretch()
        layout_meio.addLayout(layout_meio)
        
        frame_container.setFixedSize(200, 350)
        layout_container.addLayout(layout_meio)
        # layout_container.addLayout(layout_bts)
        layout_container.addStretch()

        layout_main.addWidget(frame_container)
        self.setLayout(layout_main)
        frame_container.setObjectName(SECONDARY)
        
        
        
    
    def start(self, id):
        dados_dict = bd.get_usuarioByID(id)
        
        id = str(dados_dict['id'])
        nome = dados_dict['nome']
        email = dados_dict['email']
        usuario = dados_dict['usuario']
        senha = dados_dict['senha']

        self.lb_id.setText(f'id: {id}')
        self.lb_nome.setText(nome)

        print('dados:')
        print(dados_dict)
        

            
        
    
    def keyPressEvent(self, event): #type:ignore
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_homePicture()
    window.setGeometry(100, 100, 1200, 1000)
    window.show()
    window.start(2)

    app.setStyleSheet(get_style())
    sys.exit(app.exec())
