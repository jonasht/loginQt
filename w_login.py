from PyQt6.QtWidgets import (
    QWidget, QApplication,
    QLabel, QLineEdit, QPushButton, 
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame, QStackedWidget,
    
)

from PyQt6.QtGui import QPixmap

from PyQt6.QtCore import Qt
import sys
import util as u
from style import *
import bancoDeDados as bd

from w_recuperarConta import W_recuperarConta
from w_home import W_home
from w_cadastro import W_cadastro


CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
RIGHT =  Qt.AlignmentFlag.AlignRight
CENTER_V = Qt.AlignmentFlag.AlignVCenter


class W_login (QWidget):
  def __init__(self) -> None:
      super().__init__()
      
      layout_main = QVBoxLayout()
      
    # login ==============================
      layout_cima = QHBoxLayout()
      layout_meio = QHBoxLayout()
      layout_baixo = QGridLayout()

      frame_main = QFrame()
      
      # titulo ===================================================
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
      
      # meio esquerdo imagem ================================
      layout_esquerdo = QVBoxLayout()
      self.lb_pixmap = QLabel()
      self.lb_pixmap.setPixmap(self.get_widgetImage())
      layout_esquerdo.addWidget(self.lb_pixmap)

      # meio direito ==========================================
      layout_direito = QVBoxLayout()
      layout_direitoGrid = QGridLayout()
      # usuario ===
      self.lb_usuario = QLabel('Usuário:')
      self.le_usuario = QLineEdit()
      layout_direitoGrid.addWidget(self.lb_usuario, 0, 0)
      layout_direitoGrid.addWidget(self.le_usuario, 0, 1)

      # senha
      self.lb_senha = QLabel('Senha:')
      self.le_senha = QLineEdit()
      self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)
      layout_direitoGrid.addWidget(self.lb_senha, 1, 0)
      layout_direitoGrid.addWidget(self.le_senha, 1, 1)

      self.le_usuario.setFixedWidth(300)
      self.le_senha.setFixedWidth(300)
      
      self.le_usuario.setAlignment(CENTER)
      self.le_senha.setAlignment(CENTER)
      self.lb_usuario.setAlignment(RIGHT | CENTER_V)
      self.lb_senha.setAlignment(RIGHT | CENTER_V)
      
      # botao link esqueceu a senha
      self.bt_esqueceuSenha = QPushButton('Esqueceu a senha?')
      self.bt_esqueceuSenha.setObjectName(LINK)
      layout_direitoGrid.addWidget(self.bt_esqueceuSenha, 2, 1)
      self.bt_esqueceuSenha.setStyleSheet('''text-align: right;''')

      # label aviso
      self.lb_aviso = QLabel('')
      self.lb_aviso.setAlignment(CENTER)

      layout_direitoGrid.addWidget(self.lb_aviso, 3, 1)
      
      # botoes
      layout_bts = QGridLayout()
      self.bt_entrar = QPushButton('Entrar')
      self.bt_cadastrar = QPushButton('Cadastrar')

      self.bt_entrar.setObjectName(SUCCESS)
      self.bt_cadastrar.setObjectName(INFO)
      self.bt_entrar.clicked.connect(self.fazer_login)
      
      
      layout_bts.addWidget(self.bt_entrar, 0, 0)
      layout_bts.addWidget(self.bt_cadastrar, 1, 0)
      


      # frame_main.setFixedHeight(800)
      # frame_main.setFixedWidth(700)
      
      # fim login ===================================
      self.w_cadastro = W_cadastro()
      self.w_recuperarConta = W_recuperarConta()
      self.w_home = W_home()

      self.stack = QStackedWidget()
      self.stack.addWidget(frame_main)
      self.stack.addWidget(self.w_cadastro)
      self.stack.addWidget(self.w_recuperarConta)
      self.stack.addWidget(self.w_home)

      # layouts principais ===================================
      layout_centro_h = QHBoxLayout()
      layout_centro_h.addLayout(layout_meio)
      layout_centro_h.addStretch()

      layout_do_frame = QVBoxLayout()
      layout_do_frame.addLayout(layout_cima)
      layout_do_frame.addStretch()
      layout_do_frame.addLayout(layout_centro_h) 
      layout_do_frame.addStretch()
      
      layout_do_frame.addLayout(layout_bts)
      layout_do_frame.addLayout(layout_baixo)
      layout_do_frame.setContentsMargins(12,0,12,12)
      frame_main.setLayout(layout_do_frame)
      # layout_main.addWidget(frame_main, 0, CENTER)
      layout_meio.addLayout(layout_esquerdo)
      layout_direito.addStretch()
      layout_direito.addLayout(layout_direitoGrid)
      layout_direito.addStretch()
      layout_meio.addLayout(layout_direito)
      layout_main.addWidget(self.stack, 0, CENTER)
      
      self.setLayout(layout_main)
      
      # events bts 
      self.bt_cadastrar.clicked.connect(self.event_cadastro)
      self.bt_esqueceuSenha.clicked.connect(self.event_recuperarConta)
  def get_widgetImage(self):
      pixmap = QPixmap('./fotos/coruja.jpg')
      rect = pixmap.rect()
      # pixmap = pixmap.copy(rect.x(), rect.y(), rect.width() // 2, rect.height() // 2)
      pixmap = pixmap.copy(130, 200, 1000, 900)
      pixmap = pixmap.scaled(600,600)
      
      return pixmap

  def event_cadastro(self):
    self.stack.setCurrentIndex(1)

  def event_recuperarConta(self):
    
    self.stack.setCurrentIndex(2)

  def fazer_login(self):
      usuario = self.le_usuario.text()
      senha = self.le_senha.text()
      
      if not usuario or not senha:
        print('preecha todos os campos')
        self.lb_aviso.setText('preencha todos os campos')
        self.lb_aviso.setObjectName(DANGER)
        self.le_usuario.setObjectName(DANGER)
        self.le_senha.setObjectName(DANGER)
        self.le_usuario.style().unpolish(self.le_usuario) #type:ignore
        self.le_senha.style().unpolish(self.le_senha) #type:ignore
        self.lb_aviso.style().unpolish(self.lb_aviso) #type:ignore

      else:
        id = bd.validar_conta(usuario, senha)
        print('entrar em conta' if id else 'nao entrar')
        print('==========================================================================')
        print('login feito com sucesso' if id else 'login invalido')
        print(f'usario:', usuario)
        print(f'senha:', senha)
        
        if id:
          self.w_home.start(id)
          self.stack.setCurrentIndex(3)
          
      

  def keyPressEvent(self, event): # type:ignore

      if event.key() == Qt.Key.Key_Escape or event.key() == Qt.Key.Key_Q:
          self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_login()
    window.setStyleSheet(get_style())
    # default preencher campos automaticamente
    window.le_usuario.setText('jonas')
    window.le_senha.setText('123')
    window.setGeometry(100, 100, 1200, 1000)
    window.show()
    sys.exit(app.exec())
