# напиши здесь код основного приложения и первого экрана
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from second_win import *
class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn = QPushButton(txt_next)
        self.hello_label = QLabel(txt_hello)
        self.instr = QLabel(txt_instruction)

        self.line = QVBoxLayout()
        self.line.addWidget(self.hello_label, alignment=Qt.AlignLeft)
        self.line.addWidget(self.instr, alignment=Qt.AlignLeft)
        self.line.addWidget(self.btn, alignment=Qt.AlignCenter)
        self.setLayout(self.line)
    def connects(self):
        self.btn.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.sw = Second_win()
app = QApplication([])
main_win = Mainwin()
app.exec_()
