from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget, QWidget, QApplication,
    QLabel, QPushButton, QFrame
    
)
from style import *
import sys

from w_stack1 import W_stack1
from w_stack2 import W_stack2
from w_stack3 import W_stack3


class W_stack0(QWidget):
  def __init__(self) -> None:
    super().__init__()

    layout_main = QVBoxLayout()
    
    w_inicio = QWidget()
    layout_widget = QVBoxLayout()
    w_inicio.setLayout(layout_widget)

    self.bt_inicio = QPushButton('inicio')
    self.bt_inicio.setObjectName(PRIMARY)

    self.bt_1 = QPushButton('stack 1')
    self.bt_2 = QPushButton('stack 2')
    self.bt_3 = QPushButton('stack 3')
    layout_widget.addWidget(self.bt_1)
    layout_widget.addWidget(self.bt_2)
    layout_widget.addWidget(self.bt_3)
    # =========================================
    stack = QStackedWidget()
    w_page1 = W_stack1()
    w_page2 = W_stack2()
    w_page3 = W_stack3()
    stack.addWidget(w_inicio)
    stack.addWidget(w_page1)
    stack.addWidget(w_page2)
    stack.addWidget(w_page3)



    layout_main.addWidget(stack)
    layout_main.addWidget(self.bt_inicio)
    self.bt_1.clicked.connect(lambda:stack.setCurrentIndex(1))
    self.bt_2.clicked.connect(lambda:stack.setCurrentIndex(2))
    self.bt_3.clicked.connect(lambda:stack.setCurrentIndex(3))
    self.bt_inicio.clicked.connect(lambda:stack.setCurrentIndex(0))

    self.setLayout(layout_main)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = W_stack0()
  window.setStyleSheet(get_style())
  window.setGeometry(800, 800, 800, 800)
  window.show()
  sys.exit(app.exec())