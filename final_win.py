# напиши здесь код третьего экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
class Thirdwin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.result()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.result())
        self.index_text = QLabel(txt_index + str(self.index))
        self.line = QVBoxLayout()
        self.line.addWidget(self.index_text)
        self.line.addWidget(self.work_text)
        self.setLayout(self.line)
    def result(self):
        self.index = (4*(self.exp.t1+self.exp.t2+self.exp.t3)-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11 and self.index < 15:
                return txt_res2
            elif self.index >=6 and self.index < 11:
                return txt_res3
            elif self.index >=0.5 and self.index < 6:
                return txt_res4
            elif self.index < 0.5:
                return txt_res5
        elif self.exp.age < 15 and self.exp.age >= 13:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >=12.5 and self.index < 16.5:
                return txt_res2
            elif self.index >=7.5 and self.index < 12.5:
                return txt_res3
            elif self.index >=2 and self.index < 7.5:
                return txt_res4
            elif self.index < 2:
                return txt_res5
        elif self.exp.age < 13 and self.exp.age >= 11:
            if self.index >= 18:
                return txt_res1
            elif self.index >=14 and self.index < 18:
                return txt_res2
            elif self.index >=9 and self.index < 14:
                return txt_res3
            elif self.index >=3.5 and self.index < 9:
                return txt_res4
            elif self.index < 3.5:
                return txt_res5
        elif self.exp.age < 11 and self.exp.age >= 9:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >=15.5 and self.index < 19.5:
                return txt_res2
            elif self.index >= 10.5 and self.index < 15.5:
                return txt_res3
            elif self.index >=5 and self.index < 10.5:
                return txt_res4
            elif self.index < 5:
                return txt_res5
        elif self.exp.age < 9 and self.exp.age >= 7:
            if self.index >= 21:
                return txt_res1
            elif self.index >=17 and self.index < 21:
                return txt_res2
            elif self.index >=12 and self.index < 17:
                return txt_res3
            elif self.index >=6.5 and self.index < 12:
                return txt_res4
            elif self.index < 6.5:
                return txt_res5
            else:
                return 'такой возраст не обрабатывается'
