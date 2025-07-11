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
        # self.setWindowTitle("Aplicação Principal")
        self.setGeometry(200, 200, 700, 500)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        
        layout = QGridLayout()
        widget_central.setLayout(layout)



class AppController:

    def __init__(self, app):
        self.app = app
        self.main_win = None
        self.w_login = W_login()

        self.w_login.setStyleSheet(u.get_style())
        self.w_login.setGeometry(100, 100, 800, 800)
        self.w_login.show()

    def show_main_window(self):
        self.main_win = MainWindow()
        self.main_win.show()
        self.w_login.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = AppController(app)
    sys.exit(app.exec())

