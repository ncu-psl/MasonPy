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
linearray = []                                          #(startbutton, endbutton, linetype, linename)
linetype = 'true'
linenum = 0

windspeed = np.ones(100)

buttonlist = []

class Process_Button(QPushButton):
    
    inputline = []
    dragable = 0
    string = 'a'
    next_index = 'null'
    nodenum = 0
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
   
    inputline = []
    dragable = 0
    string = 'b'
    true_index = 'null'
    false_index = 'null'
    nodenum = 0
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
    
    inputline = []
    dragable = 0
    string = 'a'
    cont_index = 'null'
    break_index = 'null'
    nodenum = 0
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
        self.button.next_index = 'a'
        self.button.move(100, 65)

        buttonlist.append(self.button)
    
        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)
        
    def paintEvent(self, event):
        global linemode
        global paintarray
        global linearray
        global linetype
        global linenum
        
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
                linename = 'line_' + str(linenum)
                linearray.append([paintarray[0], paintarray[1], linetype,linename])
                linenum = linenum + 1
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
        finallayout.addWidget(rightwidget)
        
        centralWidget.setLayout(finallayout)                                   #set final layout
        
        toolbarBox = QtWidgets.QToolBar(self)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbarBox)
        
        add_ThreePhaseShortCircuit_action = toolbarBox.addAction('ThreePhaseShortCircuit')
        add_ThreePhaseShortCircuit_action.triggered.connect(self.add_ThreePhaseShortCircuit)
        
        add_MaxMagBreak_action = toolbarBox.addAction('MaxMagBreak')
        add_MaxMagBreak_action.triggered.connect(self.add_MaxMagBreak)
        
        add_MaxWindSpeed_ThreePhaseShortCircuit_action = toolbarBox.addAction('MaxWindSpeed_ThreePhaseShortCircuit')
        add_MaxWindSpeed_ThreePhaseShortCircuit_action.triggered.connect(self.add_MaxWindSpeed_ThreePhaseShortCircuit)
        
        add_MaxPower_action = toolbarBox.addAction('MaxPower')
        add_MaxPower_action.triggered.connect(self.add_MaxPower)
        
        add_MaxWindSpeed_ThreePhaseShortCircuit_action = toolbarBox.addAction('MaxWindSpeed_ThreePhaseShortCircuit')
        add_MaxWindSpeed_ThreePhaseShortCircuit_action.triggered.connect(self.add_MaxWindSpeed_ThreePhaseShortCircuit)
        
        add_CutOut_action = toolbarBox.addAction('CutOut')
        add_CutOut_action.triggered.connect(self.add_CutOut)
        
        add_MaxTorqueCurrent_action = toolbarBox.addAction('MaxTorqueCurrent')
        add_MaxTorqueCurrent_action.triggered.connect(self.add_MaxTorqueCurrent)
        
        add_RPM_Increase_action = toolbarBox.addAction('RPM_Increase')
        add_RPM_Increase_action.triggered.connect(self.add_RPM_Increase)
        
        add_MaxTorqueCurrent_MagBreak_action = toolbarBox.addAction('MaxTorqueCurrent_MagBreak')
        add_MaxTorqueCurrent_MagBreak_action.triggered.connect(self.add_MaxTorqueCurrent_MagBreak)
        
        add_ThreePhaseShortCircuit_MagBreak_action = toolbarBox.addAction('ThreePhaseShortCircuit_MagBreak')
        add_ThreePhaseShortCircuit_MagBreak_action.triggered.connect(self.add_ThreePhaseShortCircuit_MagBreak)
        
        add_line_action = toolbarBox.addAction('true line')
        add_line_action.triggered.connect(self.add_line)
        
        add_fline_action = toolbarBox.addAction('false line')
        add_fline_action.triggered.connect(self.add_false_line)
        
        menu = self.menuBar().addMenu('File')
        write_action = menu.addAction('Write File')
        write_action.triggered.connect(self.Write_File)
        read_action = menu.addAction('Read File')
        read_action.triggered.connect(self.Read_File)
        
        add_button_menu = self.menuBar().addMenu('Button')
        
        add_line_menu = self.menuBar().addMenu('Line')
        
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
        
    def Write_File(self):
        global buttonlist
        
        self.start_draw()
        f = open('windele.txt', 'w')
        for i in buttonlist:
            f.write(i.string+' ')
            f.write(i.mode+' ')
            f.write(str(i.position)+' ')
            if i.mode == 'process':
                f.write(i.next_index+' ')
                f.write('[')
                for j in i.inputline:
                    f.write(j+',')
                f.write(']')
            if i.mode == 'decision':
                f.write(i.true_index+' ')
                f.write(i.false_index+' ')
                f.write('[')
                for j in i.inputline:
                    f.write(j+',')
                f.write(']')
            if i.mode == 'roop':
                f.write(i.cont_index+' ')
                f.write(i.break_index+' ')
                f.write('[')
                for j in i.inputline:
                    f.write(j+',')
                f.write(']')
            f.write('\n')
            
    def Read_File(self):
        global linearray
        global buttonlist
        
        linearray = []
        buttonlist = []
        count = 1                                   #number of line
        true_line_added = 'false'                   #check if line is in linearray
        false_line_added = 'false'
        
        null_button = Process_Button('123', self)
        
        f = open('windele.txt', 'r')    
        for line in f:
            temp = line.strip().split(' ')
            print(temp)
            if(temp[0] == 'Start'):
                print(temp)
                exec("self.add_"+temp[0]+"()")
                buttonlist[0].string = temp[0]
                buttonlist[0].next_index = temp[4]
                linearray.append([buttonlist[0],null_button,'true',temp[4]])
                
                if(len(temp[5]) != 2):
                    input_line = temp[5][1:-2].split(',')
                    for j in input_line:
                        for i in linearray:
                            if j == i[3]:
                                i[1] = buttonlist[0]
                                true_line_added = 'true'
                        if(true_line_added == 'false'):
                            linearray.append([null_button,buttonlist[0],'null',j])
                        true_line_added = 'false'
                                    
                        
            else:
                name = temp[0].split('_')
                exe_name = ''
                for i in name:
                    if(i!='Check'):
                        if(i!='Mode'):
                            exe_name = exe_name + '_' + i
                print(exe_name)
                exec("self.add"+exe_name+"()")
                
                if(temp[1] == 'process'):
                    buttonlist[count].string = temp[0]
                    buttonlist[count].next_index = temp[4]
                    
                    for i in linearray:
                        if temp[4] == i[3]:
                            i[0] = buttonlist[count]
                            i[3] = 'true'
                            true_line_added = 'true'
                    if(true_line_added == 'false'):
                        if(temp[4] != 'a'):
                            linearray.append([buttonlist[count],null_button,'true',temp[4]])
                    true_line_added = 'false'
                    
                    if(len(temp[5]) != 2):
                        input_line = temp[5][1:-2].split(',')
                        for j in input_line:
                            for i in linearray:
                                if j == i[3]:
                                    i[1] = buttonlist[count]
                                    true_line_added = 'true'
                            if(true_line_added == 'false'):
                                linearray.append([null_button,buttonlist[count],'null',j])
                            true_line_added = 'false'
                        
                    count += 1
                    
                if(temp[1] == 'decision'):
                    buttonlist[count].string = temp[0]
                    buttonlist[count].true_index = temp[4]
                    buttonlist[count].false_index = temp[5]
                    
                    for i in linearray:
                        if temp[4] == i[3]:
                            i[0] = buttonlist[count]
                            i[2] = 'true'
                            true_line_added = 'true'
                        if temp[5] == i[3]:
                            i[0] = buttonlist[count]
                            i[2] = 'false'
                            false_line_added = 'true'
                    if(true_line_added == 'false'):
                        if(temp[4] != 'a'):
                            linearray.append([buttonlist[count],null_button,'true',temp[4]])
                    if(false_line_added == 'false'):
                        if(temp[5] != 'a'):
                            linearray.append([buttonlist[count],null_button,'false',temp[5]])
                    true_line_added = 'false'
                    false_line_added = 'false'
                    
                    if(len(temp[6]) != 2):
                        input_line = temp[6][1:-2].split(',')
                        for j in input_line:
                            for i in linearray:
                                if j == i[3]:
                                    i[1] = buttonlist[count]
                                    true_line_added = 'true'
                            if(true_line_added == 'false'):
                                linearray.append([null_button,buttonlist[count],'null',j])
                            true_line_added = 'false'
                        
                    count += 1
                    
                if(temp[1] == 'roop'):
                    buttonlist[count].string = temp[0]
                    buttonlist[count].cont_index = temp[4]
                    buttonlist[count].break_index = temp[5]
                    
                    for i in linearray:
                        if temp[4] == i[3]:
                            i[0] = buttonlist[count]
                            i[3] = 'true'
                            true_line_added = 'true'
                        if temp[5] == i[3]:
                            i[0] = buttonlist[count]
                            i[3] = 'false'
                            false_line_added = 'true'
                    if(true_line_added == 'false'):
                        linearray.append([buttonlist[count],null_button,'true',temp[4]])
                    if(false_line_added == 'false'):
                        linearray.append([buttonlist[count],null_button,'false',temp[4]])
                    true_line_added = 'false'
                    false_line_added = 'false'
                    
                    if(len(temp[6]) != 2):
                        input_line = temp[6][1:-2].split(',')
                        for j in input_line:
                            for i in linearray:
                                if j == i[3]:
                                    i[1] = buttonlist[count]
                                    true_line_added = 'true'
                            if(true_line_added == 'false'):
                                linearray.append([null_button,buttonlist[count],'null',j])
                            true_line_added = 'false'
                        
                    count += 1
        print(linearray)
        
    def add_button(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button0 = Process_Button('123', self)
        buttonlist.append(leftwidget.button0)
        
        leftlayout.addWidget(leftwidget.button0)
    
    def add_Start(self):
        global leftlayout
        global leftwidget
        global buttonlist
        
        leftwidget.button0 = Process_Button('Start', self)
        buttonlist.append(leftwidget.button0)
        leftlayout.addWidget(leftwidget.button0)
        
    def add_ThreePhaseShortCircuit(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Process_Button('ThreePhaseShortCircuit', self)
        leftwidget.button.string = 'Mode_ThreePhaseShortCircuit'
        for i in buttonlist:
            if i.string == 'Mode_ThreePhaseShortCircuit':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        leftlayout.addWidget(leftwidget.button)
        
    def add_MaxMagBreak(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Decision_Button('MaxMagBreak', self)
        leftwidget.button.string = 'Check_MaxMagBreak'
        for i in buttonlist:
            if i.string == 'Check_MaxMagBreak':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        leftlayout.addWidget(leftwidget.button)
    
    def add_MaxWindSpeed_ThreePhaseShortCircuit(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Decision_Button('MaxWindSpeed_ThreePhaseShortCircuit', self)
        leftwidget.button.string = 'Check_MaxWindSpeed_ThreePhaseShortCircuit'
        for i in buttonlist:
            if i.string == 'Check_MaxWindSpeed_ThreePhaseShortCircuit':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        leftlayout.addWidget(leftwidget.button)
        
    def add_MaxPower(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Process_Button('MaxPower', self)
        leftwidget.button.string = 'Mode_MaxPower'
        for i in buttonlist:
            if i.string == 'Mode_MaxPower':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        leftlayout.addWidget(leftwidget.button)
        
    def add_CutOut(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Decision_Button('CutOut', self)
        leftwidget.button.string = 'Check_CutOut'
        for i in buttonlist:
            if i.string == 'Check_CutOut':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        leftlayout.addWidget(leftwidget.button)
    
    def add_MaxTorqueCurrent(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Process_Button('MaxTorqueCurrent', self)
        leftwidget.button.string = 'Mode_MaxTorqueCurrent'
        for i in buttonlist:
            if i.string == 'Mode_MaxTorqueCurrent':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        leftlayout.addWidget(leftwidget.button)
        
    def add_RPM_Increase(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Decision_Button('RPM_Increase', self)
        leftwidget.button.string = 'Check_RPM_Increase'
        for i in buttonlist:
            if i.string == 'Check_RPM_Increase':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        leftlayout.addWidget(leftwidget.button)
        
    def add_MaxTorqueCurrent_MagBreak(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Process_Button('MaxTorqueCurrent_MagBreak', self)
        leftwidget.button.string = 'Mode_MaxTorqueCurrent_MagBreak'
        for i in buttonlist:
            if i.string == 'Mode_MaxTorqueCurrent_MagBreak':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        leftlayout.addWidget(leftwidget.button)
    
    def add_ThreePhaseShortCircuit_MagBreak(self):
        global leftlayout
        global leftwidget
        global buttonlist
        count = 0
        
        leftwidget.button = Process_Button('ThreePhaseShortCircuit_MagBreak', self)
        leftwidget.button.string = 'Mode_ThreePhaseShortCircuit_MagBreak'
        for i in buttonlist:
            if i.string == 'Mode_ThreePhaseShortCircuit_MagBreak':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
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
        
        for i in buttonlist:
            a = []
            if i.mode == 'process': 
                for j in range(len(linearray)):
                    if linearray[j][1].string == i.string and linearray[j][1].nodenum == i.nodenum:
                        a.append(linearray[j][3])
                    if linearray[j][0].string == i.string and linearray[j][0].nodenum == i.nodenum:           #找線
                        i.next_index = linearray[j][3]
    
            if i.mode == 'decision': 
                for j in range(len(linearray)):
                    if linearray[j][1].string == i.string and linearray[j][1].nodenum == i.nodenum:
                        a.append(linearray[j][3])
                    if linearray[j][0].string == i.string and linearray[j][0].nodenum == i.nodenum:           #找線
                        
                        if linearray[j][2] == 'true':
                            i.true_index = linearray[j][3]
                                
                        else:
                            i.false_index = linearray[j][3]
                            
            if i.mode == 'roop': 
                for j in range(len(linearray)):
                    if linearray[j][1].string == i.string and linearray[j][1].nodenum == i.nodenum:
                        a.append(linearray[j][3])
                    if linearray[j][0].string == i.string and linearray[j][0].nodenum == i.nodenum:           #找線
                        
                        if linearray[j][2] == 'true':
                            i.cont_index = linearray[j][3]
                                
                        else:
                            i.break_index = linearray[j][3]
            i.inputline = a
        for i in buttonlist:
            if i.mode == 'process':
                pac = [i.string, i.inputline, i.next_index]
            if i.mode == 'decision': 
                pac = [i.string, i.inputline, [i.true_index, i.false_index]]
            if i.mode == 'roop':
                pac = [i.string, i.inputline, [i.cont_index, i.break_index]]
            finallist.append(pac)
            
        
        for i in finallist:
            print(i)
            
 
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = HelloWindow()
        mainWin.setMinimumWidth(500)
        mainWin.setMinimumHeight(500)
        mainWin.show()
        sys.exit(app.exec_())
    run_app()
    