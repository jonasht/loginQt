import textwrap
from style import Color
from PyQt6.QtGui import QPainter, QPainterPath, QPixmap
from PyQt6.QtCore import Qt

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



class TopTitle:
        # background-color: #9933cc;
    # label
    label = textwrap.dedent("""
        color: #ffffff;
        font-weight: 400;
        font-size: 24px;
    """).strip()
    
    # frame
    frame = textwrap.dedent(f'''
        background-color: {Color.INFO};
        border-bottom-right-radius: 50px;
        border-bottom-left-radius: 50px;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
          ''').strip()

if __name__ == '__main__':
    pass 
