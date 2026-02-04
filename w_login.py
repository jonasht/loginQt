from PyQt6.QtWidgets import (
    QWidget, QApplication,
    QLabel, QLineEdit, QPushButton, 
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame,
    
)
from PyQt6.QtCore import Qt
import sys
import util as u
from style import *
import bd

CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
RIGHT =  Qt.AlignmentFlag.AlignRight
CENTER_V = Qt.AlignmentFlag.AlignVCenter


class W_login (QWidget):
  def __init__(self) -> None:
      super().__init__()
      
      layout_main = QVBoxLayout()

      layout_cima = QHBoxLayout()
      layout_meio = QGridLayout()
      layout_baixo = QGridLayout()

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
      self.lb_usuario = QLabel('Usuário:')
      self.le_usuario = QLineEdit()
      layout_meio.addWidget(self.lb_usuario, 0, 0)
      layout_meio.addWidget(self.le_usuario, 0, 1)

      # senha
      self.lb_senha = QLabel('Senha:')
      self.le_senha = QLineEdit()
      self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)
      layout_meio.addWidget(self.lb_senha, 1, 0)
      layout_meio.addWidget(self.le_senha, 1, 1)

      self.le_usuario.setFixedWidth(300)
      self.le_senha.setFixedWidth(300)
      
      self.le_usuario.setAlignment(CENTER)
      self.le_senha.setAlignment(CENTER)
      self.lb_usuario.setAlignment(RIGHT | CENTER_V)
      self.lb_senha.setAlignment(RIGHT | CENTER_V)
      # botao link esqueceu a senha
      self.bt_esqueceuSenha = QPushButton('Esqueceu a senha?')
      self.bt_esqueceuSenha.setObjectName(LINK)
      layout_meio.addWidget(self.bt_esqueceuSenha, 2, 1)
      self.bt_esqueceuSenha.setStyleSheet('''text-align: right;''')

      # label aviso
      self.lb_aviso = QLabel('')
      self.lb_aviso.setAlignment(CENTER)

      layout_meio.addWidget(self.lb_aviso, 3, 1)

      # botoes
      layout_bts = QGridLayout()
      self.bt_entrar = QPushButton('Entrar')
      self.bt_cadastrar = QPushButton('Cadastrar')

      self.bt_entrar.setObjectName(SUCCESS)
      self.bt_cadastrar.setObjectName(INFO)
      self.bt_entrar.clicked.connect(self.fazer_login)
      
      
      layout_bts.addWidget(self.bt_entrar, 0, 0)
      layout_bts.addWidget(self.bt_cadastrar, 1, 0)
      

      # colocando layouts e frame
      layout_centro_h = QHBoxLayout()
      layout_centro_h.addStretch()
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
      frame_main.setFixedHeight(800)
      frame_main.setFixedWidth(700)

      layout_main.addWidget(frame_main, 0, CENTER)

      self.setLayout(layout_main)
      
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
        conta_valida = bd.validar_conta(usuario, senha)
        print('==========================================================================')
        print('login feito com sucesso' if conta_valida else 'login invalido')
        print(f'usario:', usuario)
        print(f'senha:', senha)
      

  def keyPressEvent(self, event): # type:ignore

      if event.key() == Qt.Key.Key_Escape or event.key() == Qt.Key.Key_Q:
          self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_login()
    window.setStyleSheet(get_style())
    
    window.setGeometry(100, 100, 1200, 1000)
    window.show()
    sys.exit(app.exec())
