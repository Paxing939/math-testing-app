from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt6.QtWidgets import QTabWidget

from tabs import *


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'РОМА УЧИТСЯ МАТЕМАТИКЕ'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MainWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MainWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs_widget = QTabWidget()

        self.protocol_gen_widget = ProtocolGenTab()

        self.tabs_widget.addTab(self.protocol_gen_widget, 'Решение примеров со скобками')
        self.layout.addWidget(self.tabs_widget)
        self.setLayout(self.layout)
