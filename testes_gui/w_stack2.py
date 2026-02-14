from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget, QWidget, QApplication,
    QLabel, QPushButton, QFrame
    
)
from style import *
import sys

class W_stack2(QWidget):
  def __init__(self) -> None:
    super().__init__()

    layout_main = QVBoxLayout()
    
    self.lb_titulo = QLabel('Pagina 2')
    self.lb_titulo.setObjectName(INFO)


    self.lb_1 = QLabel('stack 2')
    self.lb_2 = QLabel('aqui eh o pagina 2')

    layout_main.addWidget(self.lb_titulo)
    layout_main.addWidget(self.lb_1)
    layout_main.addWidget(self.lb_2)
    
    self.setLayout(layout_main)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = W_stack2()
  window.setStyleSheet(get_style())
  window.show()
  sys.exit(app.exec())