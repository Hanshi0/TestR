# напиши здесь код для второго экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

class second_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_hello)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        pass
    def connects(self):
        pass
    def next_click(self):
        pass

