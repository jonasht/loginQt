from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget, QWidget, QApplication,
    QLabel, QPushButton, QFrame
    
)
from style import *
import sys

class W_stack3(QWidget):
  def __init__(self) -> None:
    super().__init__()

    layout_main = QVBoxLayout()
    
    self.lb_titulo = QLabel('Pagina 3')
    self.lb_titulo.setObjectName(DANGER)

    self.lb_1 = QLabel('pagina 3')
    self.lb_2 = QLabel('aqui eh o stack 3')
    self.lb_3 = QLabel('aqui eh o stack final, n 3')

    layout_main.addWidget(self.lb_titulo)
    layout_main.addWidget(self.lb_1)
    layout_main.addWidget(self.lb_2)
    layout_main.addWidget(self.lb_3)

    self.setLayout(layout_main)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = W_stack3()
  window.setStyleSheet(get_style())
  window.show()
  sys.exit(app.exec())