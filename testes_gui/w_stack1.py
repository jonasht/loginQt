from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget, QWidget, QApplication,
    QLabel, QPushButton, QFrame
    
)
from style import *
import sys



class W_stack1(QWidget):
  def __init__(self) -> None:
    super().__init__()

    layout_main = QVBoxLayout()
    self.lb_titulo = QLabel('Pagina 1')
    self.lb_titulo.setObjectName(INFO)

    self.bt_1 = QPushButton('botao 1')
    self.bt_2 = QPushButton('botao 2')
    self.bt_3 = QPushButton('botao 3')

    layout_main.addWidget(self.lb_titulo)
    layout_main.addWidget(self.bt_1)
    layout_main.addWidget(self.bt_2)
    layout_main.addWidget(self.bt_3)

    self.setLayout(layout_main)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = W_stack1()
  window.setStyleSheet(get_style())
  window.show()
  sys.exit(app.exec())