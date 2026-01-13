from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QWidget, QLabel, QPushButton, QLineEdit,
    QCheckBox,
)

import sys
from PyQt6.QtCore import Qt


import util as u
from util import *

class Widget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout = QVBoxLayout()

        # labels =-=-=-=-=-=-=-=-=-=-=-=-=
        layout_lbs = QHBoxLayout()
        
        self.lb_default = QLabel('default')
        self.lb_primary = QLabel('primary')
        self.lb_secondary = QLabel('secondary')
        self.lb_success = QLabel('success')
        self.lb_warning = QLabel('warning')
        self.lb_danger = QLabel('danger')
        self.lb_info = QLabel(INFO)

        self.lb_primary.setObjectName(PRIMARY)
        self.lb_secondary.setObjectName(SECONDARY)
        self.lb_success.setObjectName(SUCCESS)
        self.lb_warning.setObjectName(WARNING)
        self.lb_danger.setObjectName(DANGER)
        self.lb_info.setObjectName(INFO)

        layout_lbs.addWidget(self.lb_default)
        layout_lbs.addWidget(self.lb_primary)
        layout_lbs.addWidget(self.lb_secondary)
        layout_lbs.addWidget(self.lb_success)
        layout_lbs.addWidget(self.lb_warning)
        layout_lbs.addWidget(self.lb_danger)
        layout_lbs.addWidget(self.lb_info)
        
        # label border =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        layout_lbsBorder = QHBoxLayout()
        self.lb_primaryBorder = QLabel('primary border')
        self.lb_secondaryBorder = QLabel('secondary border')
        self.lb_successBorder = QLabel('success border')
        self.lb_warningBorder = QLabel('warning border')
        self.lb_dangerBorder = QLabel('danger border')
        self.lb_infoBorder = QLabel('info border')

        self.lb_primaryBorder.setObjectName(PRIMARY_BORDER)
        self.lb_secondaryBorder.setObjectName(SECONDARY_BORDER)
        self.lb_successBorder.setObjectName(SUCCESS_BORDER)
        self.lb_warningBorder.setObjectName(WARNING_BORDER)
        self.lb_dangerBorder.setObjectName(DANGER_BORDER)
        self.lb_infoBorder.setObjectName(INFO_BORDER)

        layout_lbsBorder.addStretch()
        layout_lbsBorder.addWidget(self.lb_primaryBorder)
        layout_lbsBorder.addWidget(self.lb_secondaryBorder)
        layout_lbsBorder.addWidget(self.lb_successBorder)
        layout_lbsBorder.addWidget(self.lb_warningBorder)
        layout_lbsBorder.addWidget(self.lb_dangerBorder)
        layout_lbsBorder.addWidget(self.lb_infoBorder)
        
        # botaos =-=-=-=-=-=-=-=-=-=-=-=-=
        layout_bts = QHBoxLayout()
        
        self.bt_default = QPushButton('default')
        self.bt_primary = QPushButton(PRIMARY)
        self.bt_secondary = QPushButton(SECONDARY)
        self.bt_success = QPushButton(SUCCESS)
        self.bt_warning = QPushButton(WARNING)
        self.bt_danger = QPushButton(DANGER)
        self.bt_info = QPushButton(INFO)

        self.bt_primary.setObjectName(u.PRIMARY)
        self.bt_secondary.setObjectName(u.SECONDARY)
        self.bt_success.setObjectName(u.SUCCESS)
        self.bt_warning.setObjectName(WARNING)
        self.bt_danger.setObjectName(DANGER)
        self.bt_info.setObjectName(INFO)
        
        layout_bts.addWidget(self.bt_default)
        layout_bts.addWidget(self.bt_primary)
        layout_bts.addWidget(self.bt_secondary)
        layout_bts.addWidget(self.bt_success)
        layout_bts.addWidget(self.bt_warning)
        layout_bts.addWidget(self.bt_danger)
        layout_bts.addWidget(self.bt_info)

        # QLineEdit =-=-=-=-=-=-=-=-=-=-=-=-=
        layout_les = QHBoxLayout()
        
        self.le_default = QLineEdit()
        self.le_primary = QLineEdit()
        self.le_secondary = QLineEdit()
        self.le_success = QLineEdit()
        self.le_warning = QLineEdit()
        self.le_danger = QLineEdit()
        self.le_info = QLineEdit()

        self.le_default.setPlaceholderText('lineEdit default')
        self.le_primary.setPlaceholderText(PRIMARY)
        self.le_secondary.setPlaceholderText(SECONDARY)
        self.le_success.setPlaceholderText(SUCCESS)
        self.le_warning.setPlaceholderText(WARNING)
        self.le_danger.setPlaceholderText(DANGER)
        self.le_info.setPlaceholderText(INFO)
        
        self.le_primary.setObjectName(PRIMARY)
        self.le_secondary.setObjectName(SECONDARY)
        self.le_success.setObjectName(SUCCESS)
        self.le_warning.setObjectName(WARNING)
        self.le_danger.setObjectName(DANGER)
        self.le_info.setObjectName(INFO)
        
        layout_les.addWidget(self.le_default)
        layout_les.addWidget(self.le_primary)
        layout_les.addWidget(self.le_secondary)
        layout_les.addWidget(self.le_success)
        layout_les.addWidget(self.le_warning)
        layout_les.addWidget(self.le_danger)
        layout_les.addWidget(self.le_info)
        # checkbox
        layout_cb = QHBoxLayout()
        self.cb_primary = QCheckBox()
        self.cb_primary.setText('primary')
        layout_cb.addWidget(self.cb_primary)
        self.cb_primary.setChecked(True)
        # colocando layouts
        self.cb_primary.setObjectName('primary')
        layout.addLayout(layout_lbs)
        layout.addLayout(layout_lbsBorder)
        layout.addLayout(layout_bts)
        layout.addLayout(layout_les)
        layout.addLayout(layout_cb)
        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    
    app.setStyleSheet(u.get_style())
    sys.exit(app.exec())