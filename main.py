import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLabel, QPushButton, QGridLayout
)
from w_login import W_login
import util as u


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(200, 200, 700, 500)

        widget_central = QWidget()
        
        layout = QGridLayout()
        self.w_login = W_login()
        layout.addWidget(self.w_login)
        widget_central.setLayout(layout)



        self.setCentralWidget(widget_central)


        # self.w_login.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 800)
    app.setStyleSheet(u.get_style())
    window.show()
    sys.exit(app.exec())

