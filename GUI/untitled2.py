# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:01:40 2017

@author: Administrator
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QWidget, QApplication, QVBoxLayout, QFormLayout, QHBoxLayout, QGraphicsLineItem, QStyleOptionGraphicsItem
from PyQt5.QtCore import QSize, Qt, QMimeData, QRect, QPoint, QPointF, QLineF, QLine
from PyQt5.QtGui import QDrag, QPen, QPainter, QPixmap

leftwidget = QWidget()
leftlayout = QVBoxLayout()
rightwidget = QWidget()
label = QLabel()
linemode = 0
paintarray = []
linearray = []                                          #(startbutton, endbutton, linetype)
linetype = 'true'

windspeed = np.ones(100)

buttonlist = []

class Process_Button(QPushButton):
    
    dragable = 0
    string = 'a'
    next_index = 1
    position = QPoint()
    mode = 'process'
    
    def __init__(self, title, parent):
        super().__init__(title, parent)
        

    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() + self.rect().topLeft())
        
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        global linemode
        global paintarray
        
        if linemode == 1:
            paintarray.append(self)
            
            print(self.position)
        else :
            if e.buttons() == Qt.RightButton:
                self.dragable = 1
      
            QPushButton.mousePressEvent(self, e)
        
            print(self.string)
        
    def mouseReleaseEvent(self, e):
        self.dragable = 0
        
        print('r')
        
class Decision_Button(QPushButton):
   
    dragable = 0
    string = 'b'
    true_index = 1
    false_index = 1
    position = QPoint()
    mode = 'decision'
    
  
    def __init__(self, title, parent):
        super().__init__(title, parent)
        

    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() + self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)
        

    def mousePressEvent(self, e):
        global linemode
        global paintarray
        
        if linemode == 1:
            paintarray.append(self)
        else :
            if e.buttons() == Qt.RightButton:
                self.dragable = 1
      
            QPushButton.mousePressEvent(self, e)
        
            print(self.string)
        
    def mouseReleaseEvent(self, e):
        self.dragable = 0
        
        print('r')
        
class Roop_Button(QPushButton):
    
    dragable = 0
    string = 'a'
    cont_index = 1
    break_index = 1
    roop_time = 0
    position = QPoint()
    mode = 'roop'
    
    def __init__(self, title, parent):
        super().__init__(title, parent)
        

    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() + self.rect().topLeft())
        
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        global linemode
        global paintarray
        
        if linemode == 1:
            paintarray.append(self)
        else :
            if e.buttons() == Qt.RightButton:
                self.dragable = 1
      
            QPushButton.mousePressEvent(self, e)
        
            print(self.string)
        
    def mouseReleaseEvent(self, e):
        self.dragable = 0
        
        print('r')
        
class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        
        
    def initUI(self):

        self.setAcceptDrops(True)
        
        global buttonlist
        
        self.button = Process_Button('Start', self)
        self.button.string = 'Start'
        self.button.next_index = 1
        self.button.move(100, 65)

        buttonlist.append(self.button)
    
        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)
        
    def paintEvent(self, event):
        global linemode
        global paintarray
        global linearray
        global linetype
        
        painter = QPainter(self)
        
        if linetype == 'true':
            pen = QPen(Qt.green, 3)
        if linetype == 'false':
            pen = QPen(Qt.red, 3)
            
        painter.setPen(pen)
        
        for i in range(len(linearray)) :
            if linearray[i][2] == 'true':
                pen=QPen(Qt.green, 3)
                painter.setPen(pen)
                s = linearray[i][1].position.x()
                endpos = QPoint(s + linearray[i][1].width()/2, linearray[i][1].position.y())
                startpos = QPoint(linearray[i][0].position.x() + linearray[i][0].width()/2, linearray[i][0].position.y() + linearray[i][0].height()) 
                painter.drawLine(startpos, endpos)
                x = QLineF(endpos, startpos)
                x.setLength(10)
                y = QLineF(x.p2(), endpos)
                x1 = y.normalVector()
                x1.setLength(x1.length() * 0.5)
                x2 = x1.normalVector().normalVector()
                p1 = y.p2()
                p2 = x1.p2()
                p3 = x2.p2()
                painter.drawLine(p2, p1)
                painter.drawLine(p3, p1)
                
            if linearray[i][2] == 'false':
                pen = QPen(Qt.red, 3)
                painter.setPen(pen)
                s = linearray[i][1].position.x()
                endpos = QPoint(s + linearray[i][1].width()/2, linearray[i][1].position.y())
                startpos = QPoint(linearray[i][0].position.x() + linearray[i][0].width()/2, linearray[i][0].position.y() + linearray[i][0].height()) 
                painter.drawLine(startpos, endpos)
                x = QLineF(endpos, startpos)
                x.setLength(10)
                y = QLineF(x.p2(), endpos)
                x1 = y.normalVector()
                x1.setLength(x1.length() * 0.5)
                x2 = x1.normalVector().normalVector()
                p1 = y.p2()
                p2 = x1.p2()
                p3 = x2.p2()
                painter.drawLine(p2, p1)
                painter.drawLine(p3, p1)
        
        if linemode == 1:
            if len(paintarray) == 2:
                linearray.append([paintarray[0], paintarray[1], linetype])
                x = painter.drawLine(paintarray[0].position, paintarray[1].position)
                paintarray = []

    def dragEnterEvent(self, e):
      
        e.accept()
        
    def dragMoveEvent(self, e):

        global buttonlist
        position = e.pos()
        
        for button in buttonlist:
            if button.dragable == 1:
                button.move(position)
                button.resize(210,30)
                button.position = position
        
        e.setDropAction(Qt.MoveAction)
        e.accept()
        self.repaint()
        
    def dropEvent(self, e):

        global buttonlist
        
        for button in buttonlist:
            if button.dragable == 1:
                button.dragable = 0
        
        e.setDropAction(Qt.MoveAction)
        e.accept()
        
    def mouseReleaseEvent(self, e):
        self.repaint()
    
class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        QMainWindow.__init__(self)
  
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)  
        
        self.setWindowTitle("風電") 
        
        
        self.setleftwidget()
        self.setrightwidget()
        
        finallayout = QHBoxLayout()
        finallayout.addWidget(leftwidget)
        #finallayout.addWidget(rightwidget)
        
        centralWidget.setLayout(finallayout)                                   #set final layout
        
        toolbarBox = QtWidgets.QToolBar(self)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbarBox)
        
        menu = self.menuBar().addMenu('Action for quit')
        action = menu.addAction('Quit')
        action.triggered.connect(QtWidgets.QApplication.quit)
        
        add_button_menu = self.menuBar().addMenu('Button')
        
        add_ThreePhaseShortCircuit_action = add_button_menu.addAction('ThreePhaseShortCircuit')
        add_ThreePhaseShortCircuit_action.triggered.connect(self.add_ThreePhaseShortCircuit)
        
        add_MaxMagBreak_action = add_button_menu.addAction('MaxMagBreak')
        add_MaxMagBreak_action.triggered.connect(self.add_MaxMagBreak)
        
        add_MaxWindSpeed_ThreePhaseShortCircuit_action = add_button_menu.addAction('MaxWindSpeed_ThreePhaseShortCircuit')
        add_MaxWindSpeed_ThreePhaseShortCircuit_action.triggered.connect(self.add_MaxWindSpeed_ThreePhaseShortCircuit)
        
        add_MaxPower_action = add_button_menu.addAction('MaxPower')
        add_MaxPower_action.triggered.connect(self.add_MaxPower)
        
        add_MaxWindSpeed_ThreePhaseShortCircuit_action = add_button_menu.addAction('MaxWindSpeed_ThreePhaseShortCircuit')
        add_MaxWindSpeed_ThreePhaseShortCircuit_action.triggered.connect(self.add_MaxWindSpeed_ThreePhaseShortCircuit)
        
        add_CutOut_action = add_button_menu.addAction('CutOut')
        add_CutOut_action.triggered.connect(self.add_CutOut)
        
        add_MaxTorqueCurrent_action = add_button_menu.addAction('MaxTorqueCurrent')
        add_MaxTorqueCurrent_action.triggered.connect(self.add_MaxTorqueCurrent)
        
        add_RPM_Increase_action = add_button_menu.addAction('RPM_Increase')
        add_RPM_Increase_action.triggered.connect(self.add_RPM_Increase)
        
        add_MaxTorqueCurrent_MagBreak_action = add_button_menu.addAction('MaxTorqueCurrent_MagBreak')
        add_MaxTorqueCurrent_MagBreak_action.triggered.connect(self.add_MaxTorqueCurrent_MagBreak)
        
        add_ThreePhaseShortCircuit_MagBreak_action = add_button_menu.addAction('ThreePhaseShortCircuit_MagBreak')
        add_ThreePhaseShortCircuit_MagBreak_action.triggered.connect(self.add_ThreePhaseShortCircuit_MagBreak)
        
        add_line_menu = self.menuBar().addMenu('Line')
        
        add_line_action = add_line_menu.addAction('true line')
        add_line_action.triggered.connect(self.add_line)
        
        add_fline_action = add_line_menu.addAction('false line')
        add_fline_action.triggered.connect(self.add_false_line)
        
        add_draw_action = self.menuBar().addAction('draw')
        add_draw_action.triggered.connect(self.start_draw)
        
    
    
    def setleftwidget(self):                                        #set work area layout
        global leftwidget
        global leftlayout
        global buttonlist
        
        leftwidget = Example()
        
        leftwidget.setLayout(leftlayout)
    
    def setrightwidget(self):                                       #set drow area layout
        global rightwidget
        global label
        global windspeed
        
        x = np.arange(0,100)
        y = windspeed[x]

        plt.plot(x,y) 

        plt.xlim(-30,390)
        plt.ylim(-1.5,1.5)

        plt.xlabel("x-axis") 
        plt.ylabel("y-axis") 
        plt.title("The Title") 
        plt.show()

        rightlowlayout = QVBoxLayout()
        rightlowlayout.addWidget(plt.show())
        
        label.setText("1235497")
        right_low_widget = QWidget()
        right_low_widget.setLayout(rightlowlayout)
        
        rightlayout = QVBoxLayout()
        rightlayout.addWidget(label)
        rightlayout.addWidget(right_low_widget)
        
        rightwidget.setLayout(rightlayout)
        
    def add_button(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button0 = Process_Button('123', self)
        buttonlist.append(leftwidget.button0)
        
        leftlayout.addWidget(leftwidget.button0)
        
        
    def add_ThreePhaseShortCircuit(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Process_Button('ThreePhaseShortCircuit', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'Mode_ThreePhaseShortCircuit'
        leftwidget.button.nextindex = 2
        leftlayout.addWidget(leftwidget.button)
        
    def add_MaxMagBreak(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Decision_Button('MaxMagBreak', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'check_MaxMagBreak'
        leftwidget.button.true_index = 9
        leftwidget.button.false_index = 3
        leftlayout.addWidget(leftwidget.button)
    
    def add_MaxWindSpeed_ThreePhaseShortCircuit(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Decision_Button('MaxWindSpeed_ThreePhaseShortCircuit', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'check_MaxWindSpeed_ThreePhaseShortCircuit'
        leftwidget.button.true_index = 4
        leftwidget.button.false_index = 1
        leftlayout.addWidget(leftwidget.button)
        
    def add_MaxPower(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Process_Button('MaxPower', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'Mode_MaxPower'
        leftwidget.button.nextindex = 5
        leftlayout.addWidget(leftwidget.button)
        
    def add_CutOut(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Decision_Button('CutOut', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'check_CutOut'
        leftwidget.button.true_index = 6
        leftwidget.button.false_index = 4
        leftlayout.addWidget(leftwidget.button)
    
    def add_MaxTorqueCurrent(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Process_Button('MaxTorqueCurrent', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'Mode_MaxTorqueCurrent'
        leftwidget.button.nextindex = 7
        leftlayout.addWidget(leftwidget.button)
        
    def add_RPM_Increase(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Decision_Button('RPM_Increase', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'check_RPM_Increase'
        leftwidget.button.true_index = 9
        leftwidget.button.false_index = 6
        leftlayout.addWidget(leftwidget.button)
        
    def add_MaxTorqueCurrent_MagBreak(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Process_Button('MaxTorqueCurrent_MagBreak', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'Mode_MaxTorqueCurrent_MagBreak'
        leftwidget.button.nextindex = 10
        leftlayout.addWidget(leftwidget.button)
    
    def add_ThreePhaseShortCircuit_MagBreak(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button = Process_Button('ThreePhaseShortCircuit_MagBreak', self)
        buttonlist.append(leftwidget.button)
        leftwidget.button.string = 'Mode_ThreePhaseShortCircuit_MagBreak'
        leftwidget.button.nextindex = 1
        leftlayout.addWidget(leftwidget.button)
        
    def add_line(self):
        global linemode
        global paintarray
        global linetype
        
        if linemode == 0:
            linemode = 1
            linetype = 'true'
        else :
            if linetype == 'false':
                linetype = 'true'
                paintarray = []
            else:
                linemode = 0
                paintarray = []
    
    def add_false_line(self):
        global linemode
        global paintarray
        global linetype
        
        if linemode == 0:
            linemode = 1
            linetype = 'false'
        else :
            if linetype == 'true':
                linetype = 'false'
                paintarray = []
            else:
                linemode = 0
                paintarray = []
            
    def start_draw(self):
        global buttonlist
        global linearray
        
        finallist = []
        inlist = 0
        
        finallist.append(buttonlist[0])
        
        for i in range(len(buttonlist)):
            if finallist[i].mode == 'process': 
                for j in range(len(linearray)):
                    if linearray[j][0] == finallist[i]:                              #找線
                        
                        for z in range(len(finallist)):                             #找終點
                            if linearray[j][1] == finallist[z]:
                                finallist[i].next_index = z
                                inlist = 1
                        if(inlist == 0):
                            finallist.append(linearray[j][1])
                            finallist[i].next_index = i+1
                            inlist = 0
                        else:
                            inlist = 0
    
            if finallist[i].mode == 'decision': 
                a = 0                                                               #這動作的append次數
                for j in range(len(linearray)):
                    if linearray[j][0] == finallist[i]:                              #找線
                        
                        if linearray[j][2] == 'true':
                            for z in range(len(finallist)):                             #找終點
                                if linearray[j][1] == finallist[z]:
                                    finallist[i].true_index = z
                                    inlist = 1
                            if(inlist == 0):
                                finallist.append(linearray[j][1])
                                finallist[i].true_index = i+a+1
                                a += 1
                                inlist = 0
                            else:
                                inlist = 0
                        else:
                            for z in range(len(finallist)):                             #找終點
                                if linearray[j][1] == finallist[z]:
                                    finallist[i].false_index = z
                                    inlist = 1
                            if(inlist == 0):
                                finallist.append(linearray[j][1])
                                finallist[i].false_index = i+a+1
                                a += 1
                                inlist = 0
                            else:
                                inlist = 0
            if finallist[i].mode == 'roop': 
                a = 0                                                               #這動作的append次數
                for j in range(len(linearray)):
                    if linearray[j][0] == finallist[i]:                              #找線
                        
                        if linearray[j][2] == 'true':
                            for z in range(len(finallist)):                             #找終點
                                if linearray[j][1] == finallist[z]:
                                    finallist[i].cont_index = z
                                    inlist = 1
                            if(inlist == 0):
                                finallist.append(linearray[j][1])
                                finallist[i].cont_index = i+a+1
                                a += 1
                                inlist = 0
                            else:
                                inlist = 0
                        else:
                            for z in range(len(finallist)):                             #找終點
                                if linearray[j][1] == finallist[z]:
                                    finallist[i].break_index = z
                                    inlist = 1
                            if(inlist == 0):
                                finallist.append(linearray[j][1])
                                finallist[i].break_index = i+a+1
                                a += 1
                                inlist = 0
                            else:
                                inlist = 0
        for i in finallist:
            print(i.string)
        
        
        
        
        
        
 
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = HelloWindow()
        mainWin.setMinimumWidth(500)
        mainWin.setMinimumHeight(500)
        mainWin.show()
        sys.exit(app.exec_())
    run_app()
    