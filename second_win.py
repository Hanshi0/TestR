# напиши здесь код для второго экрана приложения
from instr import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

class Second_win(QWidget):
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
    #интерфейс
    def initUI(self):
        #кнопки
        self.btn_test1=QPushButton(txt_starttest1)
        self.btn_test2=QPushButton(txt_starttest2)
        self.btn_test3=QPushButton(txt_starttest3)
        self.btn_nextscr=QPushButton(txt_sendresults)
        #надписи
        self.name=QLabel(txt_name)
        self.age=QLabel(txt_age)
        self.test1=QLabel(txt_test1)
        self.test2=QLabel(txt_test2)
        self.test3=QLabel(txt_test3)
        self.timer=QLabel('00:00')
        #поле ввода
        self.name_line=QLineEdit(txt_hintname)
        self.age_line=QLineEdit(txt_hintage)
        self.test1_line=QLineEdit(txt_hinttest1)
        self.test2_line=QLineEdit(txt_hinttest2)
        self.test3_line=QLineEdit(txt_hinttest3)
        #расположение
        self.layoutL=QVBoxLayout()
        self.layoutR=QVBoxLayout()
        self.main_layout=QHBoxLayout()
        #левая сторона
        self.layoutL.addWidget(self.name)
        self.layoutL.addWidget(self.name_line)
        self.layoutL.addWidget(self.age)
        self.layoutL.addWidget(self.age_line)
        self.layoutL.addWidget(self.test1)
        self.layoutL.addWidget(self.btn_test1)
        self.layoutL.addWidget(self.test1_line)
        self.layoutL.addWidget(self.test2)
        self.layoutL.addWidget(self.btn_test2)       
        self.layoutL.addWidget(self.test3)
        self.layoutL.addWidget(self.btn_test3)
        self.layoutL.addWidget(self.test2_line)
        self.layoutL.addWidget(self.test3_line)
        self.layoutL.addWidget(self.btn_nextscr)
        #правая сторона
        self.layoutR.addWidget(self.timer)
        #расположение 2 сторон по горизонтали
        self.main_layout.addLayout(self.layoutL)
        self.main_layout.addLayout(self.layoutR)
        self.setLayout(self.main_layout)

    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)
        #self.btn_nextscr.clicked.connects(self.next_click)
    #первый таймер
    def timer_test(self):
        global time 
        time=QTime(0,1,0)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time=time.addSecs(-1)
        self.timer.addSecs(time.toString("hh:mm:ss"))
        if self.timer=="00:00:00":
            self.timer.stop()
    #второй таймер
    def timer_sits(self):
        global time
        time=QTime(0,0,30)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time=time.addSecs(-1)
        self.timer.addSecs(time.toString("hh:mm:ss")[6,8])
        if self.timer=="00:00:00":
            self.timer.stop()
    #третий таймер
    def timer_final(self):
        global time
        time=QTime(0,0,45)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def timer3Event(self):
        global time
        time=time.addSecs(-1)
        if int(time.toString("hh,mm,ss")[6,8])>=45:
            self.timer.setStyleSheet("color: rgb(0,145,0)")
        elif int(time.toString("hh,mm,ss")[6,8])<=15:
            self.timer.setStyleSheet("color: rgb(0,145,0)")
        else:
            self.timer.setStyleSheet("color: rgb(0,0,0)")

    def next_click(self):
        pass
app=QApplication([])
screen2=Second_win()
app.exec_()

