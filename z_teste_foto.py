from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QFrame, QCheckBox
)
from PyQt6.QtGui import QPixmap, QPainter, QRegion, QPainterPath

import sys
from PyQt6.QtCore import Qt, QRect

from style import *


CENTER = Qt.AlignmentFlag.AlignCenter
CENTER_TOP = Qt.AlignmentFlag.AlignTop | CENTER
RIGHT = Qt.AlignmentFlag.AlignRight
RIGHT_CENTER = RIGHT|CENTER

def round_corners(pixmap, radii=None):
    '''
    radii: dict com chaves 'top-left', 'top-right', 'bottom-left', 'bottom-right'
           e valores inteiros para o raio de cada canto.
           Exemplo: {"top-left": 30, "bottom-right": 50}
    '''
    if radii is None:
        radii = {}

    w, h = pixmap.width(), pixmap.height()
    rounded = QPixmap(w, h)
    rounded.fill(Qt.GlobalColor.transparent)

    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    path = QPainterPath()
    # Começa no canto superior esquerdo
    path.moveTo(0, radii.get('top-left', 0))

    # Top-left
    if 'top-left' in radii:
        path.quadTo(0, 0, radii['top-left'], 0)
    else:
        path.lineTo(0, 0)
        path.lineTo(radii.get('top-left', 0), 0)

    # Top edge até top-right
    path.lineTo(w - radii.get('top-right', 0), 0)

    # Top-right
    if 'top-right' in radii:
        path.quadTo(w, 0, w, radii['top-right'])
    else:
        path.lineTo(w, 0)
        path.lineTo(w, radii.get('top-right', 0))

    # Right edge até bottom-right
    path.lineTo(w, h - radii.get('bottom-right', 0))

    # Bottom-right
    if 'bottom-right' in radii:
        path.quadTo(w, h, w - radii['bottom-right'], h)
    else:
        path.lineTo(w, h)
        path.lineTo(w - radii.get('bottom-right', 0), h)

    # Bottom edge até bottom-left
    path.lineTo(radii.get('bottom-left', 0), h)

    # Bottom-left
    if 'bottom-left' in radii:
        path.quadTo(0, h, 0, h - radii['bottom-left'])
    else:
        path.lineTo(0, h)
        path.lineTo(0, h - radii.get('bottom-left', 0))

    path.closeSubpath()

    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()

    return rounded




class W_homePicture (QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        frame_container = QFrame()
        layout_container = QVBoxLayout()
        
        layout_meio = QVBoxLayout()
        
        
        
        # profile picture ====================================
        frame_containerPicture = QFrame()
        layout_containerPicture = QVBoxLayout()
        frame_containerPicture.setLayout(layout_containerPicture)

        self.pixmap = QPixmap('./profilePictures/vaca.jpg')
        # self.pixmap = self.pixmap.scaled(700, 700)
        self.pixmap = self.pixmap.scaled(700, 700, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.lb_pic = QLabel()
        # self.pixmap = self.make_round_pixmap(self.pixmap)
        self.pixmap = round_corners(self.pixmap, {'top-right': 60, 'bottom-right': -60})
        self.lb_pic.setPixmap(self.pixmap)
        self.lb_pic.setAlignment(CENTER)
        jc = Jcode()
        style = jc.fr(jc.radiusAll60)
        frame_container.setStyleSheet(style)

        # frame_container.setObjectName(INFO_FILL)
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
        
        frame_container.setFixedSize(900, 1050)
        layout_container.addLayout(layout_meio)
        # layout_container.addLayout(layout_bts)
        layout_container.addStretch()

        layout_main.addWidget(frame_container)
        self.setLayout(layout_main)
        frame_container.setObjectName(SECONDARY)
        

    def make_round_pixmap(self, pixmap, radius=None):
    # Se não passar radius, usa o menor lado da imagem
        size = min(pixmap.width(), pixmap.height())
        if radius is None:
            radius = size

        rounded = QPixmap(radius, radius)
        rounded.fill(Qt.GlobalColor.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Cria região circular com base no radius
        path = QRegion(QRect(0, 0, radius, radius), QRegion.RegionType.Ellipse)
        painter.setClipRegion(path)

        # Centraliza a imagem dentro do círculo
        x = (radius - pixmap.width()) // 2
        y = (radius - pixmap.height()) // 2
        painter.drawPixmap(x, y, pixmap)

        painter.end()
        return rounded


    def start(self):
        
        nome = 'Jon Coder'

        self.lb_nome.setText(nome)

        

            
        
    
    def keyPressEvent(self, event): #type:ignore
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_homePicture()
    window.setGeometry(100, 100, 1200, 1000)
    window.show()
    window.start()

    app.setStyleSheet(get_style())
    sys.exit(app.exec())
