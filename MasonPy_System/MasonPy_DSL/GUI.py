# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:01:40 2017

@author: Administrator
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import importlib.util
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QScrollArea, QMessageBox, QAction, QMenu, QLineEdit, QComboBox, QDialogButtonBox, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QCheckBox, QWidget, QApplication, QInputDialog, QVBoxLayout, QFormLayout, QHBoxLayout, QGraphicsLineItem, QStyleOptionGraphicsItem, QDialog, QSizePolicy
from PyQt5.QtCore import QSize, Qt, QMimeData, QRect, QPoint, QPointF, QLineF, QLine
from PyQt5.QtGui import QDrag, QPen, QPainter, QPixmap, QColor, QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import random
import CompileList, SetModule, FrameworkDebugger

AllFile = SetModule.getFile()
for i in AllFile:
    exec('from '+ i + ' import*')

leftwidget = QWidget()
rightwidget = QWidget()
errorlabel = QLabel()
label = QLabel()
linemode = 0
paintarray = []
linearray = []                                          #(startbutton, endbutton, linetype, linename)
linetype = 'true'
linenum = 0
figure = plt.figure()
errormsg = ''
scrollarealayout = QVBoxLayout()
buttonlist = []
buttoncount = 0
painted_top = {}
painted_bot = {}


class Process_Button(QPushButton):
    global buttonlist
    
    inputline = []
    dragable = 0
    string = 'a'
    next_index = 'null'
    nodenum = 0
    position = QPoint()
    mode = 'process'
    ExtremePoint = 0
    parameter_name = []
    parameter_value = []
    
    def __init__(self, title, parent):
        super().__init__(title, parent)
        
        self.parameter_name = []
        self.parameter_value = []
        if title != 'Start' and title != 'End':
            if(title.startswith("Mode_")):
                title = title[5:]
            t = eval(title + '()')
            self.parameter_name = t.AllVariables
            for i in range(len(self.parameter_name)):
                self.parameter_value.append(eval('t.' + self.parameter_name[i]))
            
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
            if e.buttons() == Qt.LeftButton:
                paintarray.append(self)
            
            #print(self.position)
        else :
            if e.buttons() == Qt.RightButton:
                for button in buttonlist:
                    if button.dragable == 1:
                        button.dragable = 0
                self.dragable = 1
            else:
                pos = e.pos()
 
                topRight = self.rect().topRight()
                bottomRight = self.rect().bottomRight()
     
                hotspotTopLeft = QtCore.QPoint(topRight.x()-25, topRight.y())
     
                hotspotRect = QtCore.QRect(hotspotTopLeft, bottomRight)
                
                if hotspotRect.contains(pos):
                    QtWidgets.QPushButton.mousePressEvent(self, e)
                else:
                    self.blockSignals(True)
                    self.showdialog()
            
                    self.blockSignals(False)
    
    def showdialog(self):
        inputlist, result = ProcessDialog(self.parameter_name, self.parameter_value).getdata(self.parameter_name, self.parameter_value)
        if result == 1:
            self.parameter_value = inputlist
        
class Decision_Button(QPushButton):
    global buttonlist
   
    inputline = []
    dragable = 0
    string = 'b'
    true_index = 'null'
    false_index = 'null'
    nodenum = 0
    position = QPoint()
    mode = 'Decision'
    compare_num = 0.0
    compare_stuff = " "
    compare_symbol = " "
    parameter = []
  
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
        global linearray
        
        if linemode == 1:
            if e.buttons() == Qt.LeftButton:
                paintarray.append(self)
        else :
            if e.buttons() == Qt.RightButton:
                for button in buttonlist:
                    if button.dragable == 1:
                        button.dragable = 0
                self.dragable = 1
                
            else:
                for i in linearray:
                    if i[1].string == self.string and i[1].nodenum == self.nodenum:
                        if not self.parameter:
                            if hasattr(i[0], 'parameter_name'):
                                self.parameter = i[0].parameter_name
                            else:
                                self.parameter = i[0].parameter
                        else:
                            if hasattr(i[0], 'parameter_name'):
                                self.parameter = list(set(self.parameter) & set(i[0].parameter_name))
                            else:
                                self.parameter = list(set(self.parameter) & set(i[0].parameter))
                
                if not self.parameter:
                    self.errordialog()
                else:
                    self.showdialog()
      
            QPushButton.mousePressEvent(self, e)
    
    def showdialog(self):
        dia = DecisionDialog(self.parameter)
        mod, compare, num, result = dia.getdata(self.parameter)
        if result == 1:
            self.compare_num = float(num)
            self.compare_stuff = mod
            self.compare_symbol = compare
            self.setText(self.compare_stuff + '  '+ self.compare_symbol + ' ' + str(self.compare_num))
            self.string = "Decision_" + self.compare_stuff
    
    def errordialog(self):
        dia = QMessageBox.warning(self, "error", "Require a fuction connected ahead.", QMessageBox.Close) 
        
class Loop_Button(QPushButton):
    global buttonlist
    
    inputline = []
    dragable = 0
    string = 'a'
    cont_index = 'null'
    break_index = 'null'
    nodenum = 0
    loop_time = 0
    position = QPoint()
    mode = 'Loop'
    compare_num = None
    compare_stuff = None
    compare_symbol = None
    parameter = []
    
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
            if e.buttons() == Qt.LeftButton:
                paintarray.append(self)
        else :
            if e.buttons() == Qt.RightButton:
                for button in buttonlist:
                    if button.dragable == 1:
                        button.dragable = 0
                self.dragable = 1
                
            else:
                pos = e.pos()
 
                topRight = self.rect().topRight()
                bottomRight = self.rect().bottomRight()
     
                hotspotTopLeft = QtCore.QPoint(topRight.x()-25, topRight.y())
     
                hotspotRect = QtCore.QRect(hotspotTopLeft, bottomRight)
                
                if hotspotRect.contains(pos):
                    QtWidgets.QPushButton.mousePressEvent(self, e)
                else:
                    self.blockSignals(True)
                    
                    for i in linearray:
                        if i[1].string == self.string and i[1].nodenum == self.nodenum:
                            if not self.parameter:
                                if hasattr(i[0], 'parameter_name'):
                                    self.parameter = i[0].parameter_name
                                else:
                                    self.parameter = i[0].parameter
                            else:
                                if hasattr(i[0], 'parameter_name'):
                                    self.parameter = list(set(self.parameter) & set(i[0].parameter_name))
                                else:
                                    self.parameter = list(set(self.parameter) & set(i[0].parameter))
                
                    if not self.parameter:
                        self.showdialog()
                    else:
                        self.showdecisiondialog()
                    
                    self.blockSignals(False)
    
    def showdialog(self):
        temp, result = QInputDialog.getInt(self, 'Loop Time', 'Loop Time:')
        if result == True:
            self.loop_time = temp
            self.setText('Loop ' + str(self.loop_time) + ' times')
    def showdecisiondialog(self):
        dia = loopdialog(self.parameter)
        mod, compare, num, times, result = dia.getdata(self.parameter)
        if result == 1:
            if times.strip() == '':
                if mod != 'Parameter..' and compare != 'Symbal..' and num.strip() != '':
                    try:
                        self.compare_num = float(num.strip())
                        self.compare_stuff = mod
                        self.compare_symbol = compare
                        self.setText(self.compare_stuff + ' '+ self.compare_symbol + ' ' + str(self.compare_num))
                    except ValueError:
                        self.errordialog4()
                else:
                    self.errordialog()
            else:
                if mod != 'Parameter..' and compare != 'Symbal..' and num.strip() != '':
                    try:
                        self.compare_num = float(num.strip())
                        self.compare_stuff = mod
                        self.compare_symbol = compare
                    except ValueError:
                        self.errordialog4()
                        return
                    try:
                        self.loop_time = int(times.strip())
                    except ValueError:
                        self.errordialog3()
                        return
                    self.setText(self.compare_stuff + ' '+ self.compare_symbol + ' ' + str(self.compare_num) + ' or ' + 'Loop ' + str(self.loop_time) + ' times.')
                else:
                    try:
                        self.loop_time = int(times.strip())
                    except ValueError:
                        self.errordialog3()
                        return
                    self.setText('Loop ' + str(self.loop_time) + ' times.')
    def errordialog(self):
        dia = QMessageBox.warning(self, "error", "At least complete one statement.", QMessageBox.Close) 
    def errordialog2(self):
        dia = QMessageBox.warning(self, "error", "Loop times can't less then 0.", QMessageBox.Close)
    def errordialog3(self):
        dia = QMessageBox.warning(self, "error", "Please input int for loop times.", QMessageBox.Close)  
    def errordialog4(self):
        dia = QMessageBox.warning(self, "error", "Please input float for compare value.", QMessageBox.Close)           

class Loop_end(QPushButton):
    global buttonlist
    
    inputline = []
    dragable = 0
    string = 'a'
    next_index = 'null'
    nodenum = 0
    position = QPoint()
    mode = 'Loop_end'
    ExtremePoint = 0
    
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
            if e.buttons() == Qt.LeftButton:
                paintarray.append(self)
            
         
        else :
            if e.buttons() == Qt.RightButton:
                for button in buttonlist:
                    if button.dragable == 1:
                        button.dragable = 0
                self.dragable = 1
            
            QPushButton.mousePressEvent(self, e)

class ProcessDialog(QDialog):
    def __init__(self, paremeter_name, parameter_value, parent = None):
        super().__init__()
        
        self.layout = QVBoxLayout(self)
        self.label_layout = QVBoxLayout(self)
        self.edit_layout = QVBoxLayout(self)
        self.upside_layout = QHBoxLayout(self)
        self.input_edit_list = []
        
        for i in range(len(paremeter_name)):
            self.label = QLabel(paremeter_name[i], self)
            self.label_layout.addWidget(self.label)
            self.input = QLineEdit(str(parameter_value[i]), self)
            self.input_edit_list.append(self.input)
            self.edit_layout.addWidget(self.input)
        self.upside_layout.addLayout(self.label_layout)
        self.upside_layout.addLayout(self.edit_layout)
        
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        
        self.layout.addLayout(self.upside_layout)
        self.layout.addWidget(self.buttons)
        self.setLayout(self.label_layout)
       
    def getdata(parent = None, paremeter_name = [], parameter_value = []):
        dialog = ProcessDialog(paremeter_name, parameter_value, parent)
        inputlist = []
        result = dialog.exec_()
        for i in range(len(paremeter_name)):
            inputlist.append(dialog.input_edit_list[i].text())
        return (inputlist, result)
        
class DecisionDialog(QDialog):
    def __init__(self, parameter, parent = None):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.layout2 = QHBoxLayout(self)
        
        self.combo = QComboBox()
        
        for i in range(len(parameter)):
            self.combo.addItem(parameter[i])
        
        self.combo2 = QComboBox()
        self.combo2.addItem(">")
        self.combo2.addItem(">=")
        self.combo2.addItem("=")
        self.combo2.addItem("<=")
        self.combo2.addItem("<")
        
        self.inputnum = QLineEdit()
        
        self.layout2.addWidget(self.combo)
        self.layout2.addWidget(self.combo2)
        self.layout2.addWidget(self.inputnum)
        
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        
        self.layout.addLayout(self.layout2)
        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)

    def getdata(parent = None, parameter = []):
        dialog = DecisionDialog(parameter, parent)
        result = dialog.exec_()
        mode = dialog.combo.currentText()
        compare = dialog.combo2.currentText()
        num = dialog.inputnum.text()
        return (mode, compare, num, result)

class loopdialog(QDialog):
    def __init__(self, parameter, parent = None):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.decision_layout = QHBoxLayout(self)
        self.times_layout = QHBoxLayout(self)
        
        self.label = QLabel('At least choose one statement:', self)
        self.label2 = QLabel('and/or', self)
        self.combo = QComboBox()
        
        self.combo.addItem("Parameter..")
        for i in range(len(parameter)):
            self.combo.addItem(parameter[i])
        
        self.combo2 = QComboBox()
        self.combo2.addItem("Symbal..")
        self.combo2.addItem(">")
        self.combo2.addItem(">=")
        self.combo2.addItem("=")
        self.combo2.addItem("<=")
        self.combo2.addItem("<")
        
        self.inputnum = QLineEdit()
        self.decision_layout.addWidget(self.combo)
        self.decision_layout.addWidget(self.combo2)
        self.decision_layout.addWidget(self.inputnum)
        
        self.time_label = QLabel('Loop Time:', self)
        self.timeinput = QLineEdit()
        self.times_layout.addWidget(self.time_label)
        self.times_layout.addWidget(self.timeinput)
        
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.decision_layout)
        self.layout.addWidget(self.label2)
        self.layout.addLayout(self.times_layout)
        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)
    
    def getdata(parent = None, parameter = []):
        dialog = loopdialog(parameter, parent)
        result = dialog.exec_()
        mode = dialog.combo.currentText()
        compare = dialog.combo2.currentText()
        num = dialog.inputnum.text()
        times = dialog.timeinput.text()
        return (mode, compare, num, times, result)    
    
class rightcanvas(QWidget):
    
    def __init__(self):
        super().__init__()
    
        global figure
        global scrollarealayout
        self.setStyleSheet("background: lightgray")

        
        self.canvas = FigureCanvas(figure)
        self.scrollarea = QScrollArea(self)
        self.scrollarea.setWidgetResizable(True)
        self.scrollareacontents = QWidget(self.scrollarea)
        self.scrollarea.setWidget(self.scrollareacontents)        
        
        self.scrollareacontents.setLayout(scrollarealayout)
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.scrollarea, 0 , 0, 20, 1)
        layout.setContentsMargins(0,0,0,0)
        
        self.setLayout(layout)
        
    def paintEvent(self, e):
        self.canvas.draw()
        
    def mouseReleaseEvent(self, e):
        self.repaint()
    
        
class setleftwidget(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setStyleSheet("background: white")
        
        
    def initUI(self):

        self.setAcceptDrops(True)
        
        global buttonlist
        

        self.setGeometry(240, 100, 210, 30)
    def paintEvent(self, e):
        global linemode
        global paintarray
        global linearray
        global linetype
        global linenum
        global painted_top
        global painted_bot
        
        painter = QPainter(self)
        spaceline = 0
        
        if linetype == 'true':
            pen = QPen(Qt.black, 3)
            pen.setColor(QColor(34, 140, 34))
            
        if linetype == 'false':
            pen = QPen(Qt.black, 3)
            pen.setColor(QColor(240, 128, 128))
            
            
        painter.setPen(pen)
        
        for i in range(len(linearray)) :
            #if linearray[i][2] == 'true':
            if linearray[i][2] == 'true':
                
                pen = QPen(Qt.black, 3)
                pen.setColor(QColor(34, 140, 34))
                painter.setPen(pen)
                s = linearray[i][1].position.x()
                sx = linearray[i][0].position.x() +5
                sy = linearray[i][0].position.y() +5
                ex = linearray[i][1].position.x() +5
                ey = linearray[i][1].position.y() +5
                he = linearray[i][0].height()
                wi = linearray[i][0].width()
            if linearray[i][2] == 'false':
                pen = QPen(Qt.black, 3)
                pen.setColor(QColor(240, 128, 128))
                painter.setPen(pen)
                s = linearray[i][1].position.x()
                sx = linearray[i][0].position.x() -5
                sy = linearray[i][0].position.y() +5
                ex = linearray[i][1].position.x() -5
                ey = linearray[i][1].position.y() +5
                he = linearray[i][0].height()
                wi = linearray[i][0].width()
                
            if(True):                                  
                if(ey>sy):
                    if linearray[i][1] in painted_top:
                        painted_top[linearray[i][1]] += 1
                    else:
                        painted_top.setdefault(linearray[i][1],1)
                    if linearray[i][0] in painted_bot:
                        painted_bot[linearray[i][0]] += 1
                    else:
                        painted_bot.setdefault(linearray[i][0],1)
                        
                    startpos = QPoint(sx+wi/2,sy+he)
                    endpos = QPoint(ex+wi/2,ey)
                    bbsx = sx+wi/2
                    bbex = ex+wi/2
                    bbsy = sy+he
                    bbey = ey
                else:
                    if linearray[i][0] in painted_top:
                        painted_top[linearray[i][0]] += 1
                    else:
                        painted_top.setdefault(linearray[i][0],1)
                    if linearray[i][1] in painted_bot:
                        painted_bot[linearray[i][1]] += 1
                    else:
                        painted_bot.setdefault(linearray[i][1],1)
                    
                    startpos = QPoint(sx+wi/2,sy)
                    endpos = QPoint(ex+wi/2,ey+he)
                    bbsx = sx+wi/2
                    bbex = ex+wi/2
                    bbsy = sy
                    bbey = ey+he
                                   
                #if(bbsx==bbex):
                if(bbsx-bbex < wi/2 and bbsx-bbex >-wi/2):
                    painter.drawLine(startpos, endpos)
                    x = QLineF(endpos, startpos)
                #elif(linearray[i][0].position.y()==linearray[i][1].position.y()):
                elif(sy-ey <3 and sy-ey >-3):
                    yy=linearray[i][0].position.y() + linearray[i][0].height()/2
                    if(bbsx<bbex):                       
                        endpos = QPoint(s, yy)
                        startpos = QPoint(linearray[i][0].position.x() + linearray[i][0].width()- 5,yy) 
                        painter.drawLine(startpos, endpos)
                        x = QLineF(endpos, startpos)
                    else:
                        endpos = QPoint(s+wi, yy)
                        startpos = QPoint(linearray[i][0].position.x(),yy) 
                        painter.drawLine(startpos, endpos)
                        x = QLineF(endpos, startpos)
                        
                else:
                    medipos = QPoint(bbsx,bbey)
                    if(bbsx>bbex+wi/2):
                            endpos = QPoint(ex+wi,bbey)
                    elif(bbsx<bbex-wi/2):
                            endpos = QPoint(ex,bbey)
                    else:
                            endpos =endpos
                        
                    painter.drawLine(startpos, medipos)
                    painter.drawLine(medipos, endpos)
                    x = QLineF(endpos, medipos)
                
                #x = QLineF(endpos, startpos)
                x.setLength(15)
                y = QLineF(x.p2(), endpos)
                x1 = y.normalVector()
                x1.setLength(x1.length() * 0.5)
                x2 = x1.normalVector().normalVector()
                p1 = y.p2()
                p2 = x1.p2()
                p3 = x2.p2()
                painter.drawLine(p2, p1)
                painter.drawLine(p3, p1)
                
                #endpos = QPoint(s + linearray[i][1].width()/2 - 5, linearray[i][1].position.y() + 5)
                #startpos = QPoint(linearray[i][0].position.x() + linearray[i][0].width()/2 - 5, linearray[i][0].position.y() + linearray[i][0].height() + 5) 
                """
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
                endpos = QPoint(s + linearray[i][1].width()/2 - 5, linearray[i][1].position.y() + 5)
                startpos = QPoint(linearray[i][0].position.x() + linearray[i][0].width()/2 - 5, linearray[i][0].position.y() + linearray[i][0].height() + 5) 
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
                """
        if linemode == 1:
            if len(paintarray) == 2:
                linename = 'line_' + str(linenum)
                linearray.append([paintarray[0], paintarray[1], linetype, linename])
                linenum = linenum + 1
                x = painter.drawLine(paintarray[0].position, paintarray[1].position)
                paintarray = []
                self.repaint()

    def dragEnterEvent(self, e):
      
        e.accept()
        
    def dragMoveEvent(self, e):

        global buttonlist
        position = e.pos()
        x = position.x()+110
        y = position.y()+77
        position2 = QPoint(x, y)
        
        for button in buttonlist:
            if button.dragable == 1:
                button.move(position2)
                button.position = position
        
        e.setDropAction(Qt.MoveAction)
        e.accept()
        self.repaint()

    def mouseReleaseEvent(self, e):
        self.repaint()
    
class HelloWindow(QMainWindow):
    isPaintWindSpeed = True
    isPaintRPM       = True
    isPaintPower     = True 
    def __init__(self):
        super().__init__()
        
        
        QMainWindow.__init__(self)
  
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)  
        
        self.setWindowTitle("MasonPy Visual Editor") 
        self.setStyleSheet("QMainWindow {background: lightgray}")
        
        
        self.setleftwidget()
        self.setrightwidget()
        
        finallayout = QGridLayout()
        finallayout.setSpacing(0)
        finallayout.addWidget(leftwidget, 0, 0, 1, 40)
        finallayout.addWidget(rightwidget, 0, 41, 1, 30)
        
        centralWidget.setLayout(finallayout)                                   #set final layout
        
        toolbarBox = QtWidgets.QToolBar(self)
        toolbarBox.setFixedWidth(100)
        toolbarBox.setMovable(False)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbarBox)
        toolbarBox.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f5f5f5, stop: 0.4 #dcdcdc,stop: 0.5 #d3d3d3, stop: 1.0 #c0c0c0);\
                                border-radius: 6px; color: black; font:14px Impact; width:100; height:35;")
        endpoint_button = QPushButton('Start/End')
        endpoint_button.setStyleSheet("padding-left:10px")
        endpoint_menu = QMenu()
        add_Start_action = endpoint_menu.addAction('Start')
        add_Start_action.triggered.connect(self.add_Start)
        add_End_action = endpoint_menu.addAction('End')
        add_End_action.triggered.connect(self.add_End)
        endpoint_button.setMenu(endpoint_menu)
        #endpoint_button.setIcon('Start/End')
        
        process_button = QPushButton('Module')
        process_button.setStyleSheet("padding-left:10px")
        process_menu = QMenu()
# =============================================================================
#         with open('PrintTest.py', encoding = 'utf8') as f:                      #import function.py
#             for line in f:
#                 cleanline = line.strip()
#                 if cleanline.find("class ") != -1:
#                     temp = cleanline.split()
#                     temp = temp[1].split('(')
#                     add_function_action = toolbarBox.addAction(temp[0])
#                     add_function_action.triggered.connect(lambda checked, string = temp[0]:self.add_Process(string))
#                     
# =============================================================================
        moduleclass = SetModule.getClass()
        moduleclass.remove('ExtremePointMode')
        moduleclass.remove('originalMode')
        moduleclass.remove('Decide')
        moduleclass.remove('Loop')
        for i in range(len(moduleclass)):
            add_function_action = process_menu.addAction(moduleclass[i])
            add_function_action.triggered.connect(lambda checked, string = moduleclass[i]:self.add_Process(string))
        process_button.setMenu(process_menu)
        #process_button.setIcon('Module')
        
        toolbarBox.addWidget(endpoint_button)
        toolbarBox.addWidget(process_button)
# =============================================================================
#         
#         add_ThreePhaseShortCircuit_action = toolbarBox.addAction('mode_ThreePhaseShortCircuit')
#         add_ThreePhaseShortCircuit_action.triggered.connect(self.add_ThreePhaseShortCircuit)
#                 
#         add_MaxPower_action = toolbarBox.addAction('mode_MaxPower')
#         add_MaxPower_action.triggered.connect(self.add_MaxPower)
#         
#         add_MaxTorqueCurrent_action = toolbarBox.addAction('mode_MaxTorqueCurrent')
#         add_MaxTorqueCurrent_action.triggered.connect(self.add_MaxTorqueCurrent)
#         
#         add_MaxTorqueCurrent_MagBrake_action = toolbarBox.addAction('mode_MaxTorqueCurrent_MagBrake')
#         add_MaxTorqueCurrent_MagBrake_action.triggered.connect(self.add_MaxTorqueCurrent_MagBrake)
#         
#         add_ThreePhaseShortCircuit_MagBrake_action = toolbarBox.addAction('mode_ThreePhaseShortCircuit_MagBrake')
#         add_ThreePhaseShortCircuit_MagBrake_action.triggered.connect(self.add_ThreePhaseShortCircuit_MagBrake)
#         
# =============================================================================
        add_decision_action = toolbarBox.addAction('Decision')
        add_decision_action.triggered.connect(self.add_Decision)
        
        add_Loop_action = toolbarBox.addAction('Loop')
        add_Loop_action.triggered.connect(self.add_Loop)
        
        add_line_action = toolbarBox.addAction('True line')
        add_line_action.triggered.connect(self.add_line)
        
        add_fline_action = toolbarBox.addAction('False line')
        add_fline_action.triggered.connect(self.add_false_line)
        
        menu = self.menuBar().addMenu('File')
        read_action = menu.addAction('Import')
        read_action.triggered.connect(self.Read_File)
        write_action = menu.addAction('Export')
        write_action.triggered.connect(self.Write_File)
        
        add_draw_action = self.menuBar().addAction('Run')
        add_draw_action.triggered.connect(self.start_run)
        
        intro_action = self.menuBar().addAction('Intro')
        intro_action.triggered.connect(self.draw_intro)
        
    
    
    def setleftwidget(self):                                        #set work area layout
        global leftwidget
        global buttonlist
        
        leftlayout = QGridLayout()
        
        label = QLabel('Flowchart')
        
        draw_widget = setleftwidget()
        
        leftlayout.addWidget(label,0,0)
        leftlayout.addWidget(draw_widget,1,0,25,1)
        leftlayout.setContentsMargins(0,0,0,0)
        
        leftwidget.setLayout(leftlayout)
        
        leftwidget.setStyleSheet("background: white")
        label.setStyleSheet("background: lightgray")
        

    
    def setrightwidget(self):                                       #set drow area layout
        global rightwidget
        global label
        global windspeed
        global figure
        global errormsg
        global errorlabel
        global canvas
        
        rightlayout = QGridLayout()
        
        label1 = QLabel('Result')
        
        label2 = QLabel('Console')
        
        canvas = rightcanvas()
        
        errorlabel.setStyleSheet("background: white")
        #rightlowlayout = QVBoxLayout()
        #self.canvas.draw()
        
        #self.toolbar = NavigationToolbar(self.canvas, self)
        #self.toolbar.hide()
        
        #label.setText("1235497")
        #right_low_widget = QWidget()
        #right_low_widget.setLayout(rightlowlayout)
        rightlayout.addWidget(label1,0,0)
        rightlayout.addWidget(canvas,1,0,30,1)
        rightlayout.addWidget(label2,31,0)
        rightlayout.addWidget(errorlabel,32,0,10,1)
        
        rightwidget.setLayout(rightlayout)
        
        
        #rightlayout = QVBoxLayout()
        
        #rightlayout.addWidget(label)
        
        #rightwidget.setLayout(rightlayout)
        
    def Write_File(self):
        global buttonlist
        
        self.full_buttonlist()

        openfile_name, filetype = QFileDialog.getSaveFileName(self,"檔案儲存","./","All Files (*);;Text Files (*.txt)")
        f = open(openfile_name, 'w')
        for i in buttonlist:
            if i.mode == 'process':
                if i.ExtremePoint == 0:                                         #write 'Mode_' + i.string + str(i.nodenum), i.string, i.inputline, [i.next_index]
                    f.write('Mode_' + i.string + str(i.nodenum) + ' ')
                    #f.write(i.string + str(i.nodenum) + ' ')
                    f.write(i.string + str(i.nodenum) + ' ')
                    f.write(i.string+' ')
                    f.write('[')
                    for j in i.inputline:
                        f.write(j+',')
                    f.write('] ')
                    f.write('[' + i.next_index + ']')
                else:
                    if i.string == 'End':                                       #write i.string+str(i.nodenum), 'ExtremePointMode', i.inputline, []
                        f.write(i.string + str(i.nodenum) + ' ')
                        f.write('ExtremePointMode ')
                        f.write('[')
                        for j in i.inputline:
                           f.write(j+',')
                        f.write('] ')
                        f.write('[]')
                    else:                                                       #write i.string, 'ExtremePointMode', i.inputline, [i.next_index]
                        f.write(i.string + ' ')
                        f.write('ExtremePointMode ')
                        f.write('[')
                        for j in i.inputline:
                           f.write(j+', ')
                        f.write('] ')
                        f.write('[')
                        f.write(i.next_index)
                        f.write(']')

            elif i.mode == 'Decision':                                          #write i.string+str(i.nodenum), 'Decide', i.inputline, [i.true_index, i.false_index], [i.compare_stuff, i.compare_num, i.compare_symbol]
                f.write(i.string + str(i.nodenum) + ' ')
                f.write('Decide ')
                f.write('[')
                for j in i.inputline:
                    f.write(j+',')
                f.write('] ')
                f.write('[' + i.true_index + ',' + i.false_index + '] ')
                if i.compare_stuff != None and i.compare_num != None and i.compare_symbol != None:
                    f.write('[' + i.compare_stuff + ',' + str(i.compare_num) +',' + i.compare_symbol + '] ')
                else:
                    f.write('[None,None,None] ')
                
            elif i.mode == 'Loop':                                              #write i.string+str(i.nodenum), i.string, i.inputline, [i.cont_index, i.break_index], [0, i.loop_time]
                f.write(i.string + str(i.nodenum) + ' ')
                f.write(i.string + ' ')
                f.write('[')
                for j in i.inputline:
                    f.write(j+',')
                f.write('] ')
                f.write('[' + i.cont_index + ',' + i.break_index + '] ')
                if i.compare_stuff != None and i.compare_num != None and i.compare_symbol != None:
                    f.write('[' + i.compare_stuff + ',' + str(i.compare_num) +',' + i.compare_symbol + '] ')
                else:
                    f.write('[None,None,None] ')
                f.write(str(i.loop_time))
            f.write('\n')
        f.close()
            
    def Read_File(self):
        global linearray
        global buttonlist
        
        linearray = []
        buttonlist = []
        count = 0                                   #number of string line being imported in file
        true_line_added = 'false'                   #check if line is in linearray
        false_line_added = 'false'
        
        openfile_name, filetype = QFileDialog.getOpenFileName(self,'選擇文件','','Excel files(*.txt)')
        f = open(openfile_name, 'r')    
        for line in f:
            temp = line.strip().split(' ')
            if temp[1] == 'ExtremePointMode':
                if temp[0] == 'Start':
                    exec('self.add_Start()')
                    linearray.append([buttonlist[count],'','true',temp[3][1:-1]])
                    count += 1
                else:
                    exec('self.add_End()')
                    if len(temp[2]) != 2:
                        input_line = temp[2][1:-2].split(',')
                        for j in input_line:
                            for i in linearray:
                                if j == i[3]:
                                    i[1] = buttonlist[count]
                                    true_line_added = 'true'
                            if true_line_added == 'false':
                                linearray.append(['',buttonlist[count],'null',j])
                            true_line_added = 'false'
                    count += 1
            elif temp[1] == 'Decide':
                exec('self.add_Decision()')
                
                element = temp[4][1:-1].split(',')
                buttonlist[count].compare_stuff = element[0]
                buttonlist[count].compare_num = float(element[1])
                buttonlist[count].compare_symbol = element[2]
                buttonlist[count].setText(buttonlist[count].compare_stuff + '  '+ buttonlist[count].compare_symbol + ' ' + str(buttonlist[count].compare_num))
                buttonlist[count].string = "Decision_" + buttonlist[count].compare_stuff
                
                output_line = temp[3][1:-1].split(',')
                for i in linearray:
                    if output_line[0] == i[3]:
                        i[0] = buttonlist[count]
                        i[2] = 'true'
                        true_line_added = 'true'
                    if output_line[1] == i[3]:
                        i[0] = buttonlist[count]
                        i[2] = 'false'
                        false_line_added = 'true'
                if true_line_added == 'false':
                    if output_line[0] != 'null':
                        linearray.append([buttonlist[count],'','true',output_line[0]])
                if false_line_added == 'false':
                    if output_line[1] != 'null':
                        linearray.append([buttonlist[count],'','false',output_line[1]])
                true_line_added = 'false'
                false_line_added = 'false'
                
                if len(temp[2]) != 2:
                    input_line = temp[2][1:-2].split(',')
                    for j in input_line:
                        for i in linearray:
                            if j == i[3]:
                                i[1] = buttonlist[count]
                                true_line_added = 'true'
                        if true_line_added == 'false':
                            linearray.append(['',buttonlist[count],'null',j])
                        true_line_added = 'false'
                count += 1
            
            elif temp[1] == 'Loop':
                exec('self.add_Loop()')
                buttonlist[count].loop_time = int(temp[5])
                
                element = temp[4][1:-1].split(',')
                if element[0] != 'None':
                    buttonlist[count].compare_stuff = element[0]
                if element[1] != 'None':
                    buttonlist[count].compare_num = float(element[1])
                if element[2] != 'None':
                    buttonlist[count].compare_symbol = element[2]
                
                if buttonlist[count].loop_time == 0:
                    if buttonlist[count].compare_stuff != None:
                        buttonlist[count].setText(buttonlist[count].compare_stuff + ' '+ buttonlist[count].compare_symbol + ' ' + str(buttonlist[count].compare_num))
                else:
                    if buttonlist[count].compare_stuff != None:
                        buttonlist[count].setText(buttonlist[count].compare_stuff + ' '+ buttonlist[count].compare_symbol + ' ' + str(buttonlist[count].compare_num) + ' or ' + 'Loop ' + str(buttonlist[count].loop_time) + ' times.')
                    else:
                        buttonlist[count].setText('Loop ' + str(buttonlist[count].loop_time) + ' times.')
                        
                output_line = temp[3][1:-1].split(',')
                for i in linearray:
                    if output_line[0] == i[3]:
                        i[0] = buttonlist[count]
                        i[2] = 'true'
                        true_line_added = 'true'
                    if output_line[1] == i[3]:
                        i[0] = buttonlist[count]
                        i[2] = 'false'
                        false_line_added = 'true'
                if true_line_added == 'false':
                    if output_line[0] != 'null':
                        linearray.append([buttonlist[count],'','true',output_line[0]])
                if false_line_added == 'false':
                    if output_line[1] != 'null':
                        linearray.append([buttonlist[count],'','false',output_line[1]])
                true_line_added = 'false'
                false_line_added = 'false'
                
                if len(temp[2]) != 2:
                    input_line = temp[2][1:-2].split(',')
                    for j in input_line:
                        for i in linearray:
                            if j == i[3]:
                                i[1] = buttonlist[count]
                                true_line_added = 'true'
                        if true_line_added == 'false':
                            linearray.append(['',buttonlist[count],'null',j])
                        true_line_added = 'false'
                count += 1
            
            else:
                if temp[1].startswith("Mode_"):
                    temp[1] = temp[1][5:]
                if temp[1].endswith("MagBrake"):
                    temp[1] = temp[1].replace("Mag","Mech")
                exec('self.add_Process(temp[1])')
                
                if len(temp[3]) != 2:
                    for i in linearray:
                        if temp[3][1:-1] == i[3]:
                            i[0] = buttonlist[count]
                            i[2] = 'true'
                            true_line_added = 'true'
                    if true_line_added == 'false':
                        linearray.append([buttonlist[count],'','true',temp[3][1:-1]])
                    true_line_added = 'false'
                
                if len(temp[2]) != 2:
                    input_line = temp[2][1:-2].split(',')
                    for j in input_line:
                        for i in linearray:
                            if j == i[3]:
                                i[1] = buttonlist[count]
                                true_line_added = 'true'
                        if true_line_added == 'false':
                            linearray.append(['',buttonlist[count],'null',j])
                        true_line_added = 'false'
                count += 1
                
        f.close()    
        
    def add_button(self):
        global leftwidget
        global buttonlist
        
        leftwidget.button0 = Process_Button('123', self)
        buttonlist.append(leftwidget.button0)
    
    def add_Start(self):
        global leftlayout
        global leftwidget
        global buttonlist
        global buttoncount
        leftwidget.button0 = Process_Button('Start', self)
        leftwidget.button0.setStyleSheet("background-color: Gray; border-style: outset; border-radius: 10px; color: white; font:Bold")
        leftwidget.button0.string = 'Start'
        leftwidget.button0.ExtremePoint = 1
        buttonlist.append(leftwidget.button0)
        X = 120 + buttoncount // 20 * 210
        Y = 80 + buttoncount % 20 * 35
        leftwidget.button0.setGeometry(X, Y,  210, 30)
        leftwidget.button0.position.setX(X)
        leftwidget.button0.position.setY(Y)
        buttoncount += 1
        leftwidget.button0.show()
        
    def add_End(self):
        global leftwidget
        global buttonlist
        global buttoncount
        count = 0
        
        leftwidget.button = Process_Button('End', self)
        leftwidget.button.setStyleSheet("background-color: Gray; border-style: outset; border-radius: 10px; color: white; font:Bold")
        leftwidget.button.string = 'End'
        leftwidget.button.ExtremePoint = 1
        for i in buttonlist:
            if i.mode == 'process':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        X = 120 + buttoncount // 20 * 210
        Y = 80 + buttoncount % 20 * 35
        leftwidget.button.setGeometry(X, Y,  210, 30)
        leftwidget.button.position.setX(X)
        leftwidget.button.position.setY(Y)
        buttoncount += 1
        leftwidget.button.show()
    
    def add_Process(self, name):
        global leftwidget
        global buttonlist
        global buttoncount
        count = 0
        if name == False:        
            leftwidget.button = Process_Button('Process', self)
            leftwidget.button.string = 'Process'
        else:
            leftwidget.button = Process_Button(name, self)
            leftwidget.button.string = name
        menu = QMenu(self)
        intro_action = QAction(menu)
        intro_action.setText('Introduction')
        menu.addAction(intro_action)
        intro_action.triggered.connect(lambda checked, string = leftwidget.button.string:self.show_intro(string))
        leftwidget.button.setMenu(menu)
        leftwidget.button.setStyleSheet("QPushButton::menu-indicator{image:none;}")
        leftwidget.button.resize(leftwidget.button.sizeHint().width(), leftwidget.button.sizeHint().height())
        leftwidget.button.setStyleSheet("background-color: lightskyblue; border-style: outset; border-radius: 10px; color: black; font:Bold")
        
        for i in buttonlist:
            if i.mode == 'process':
                count = count + 1
        leftwidget.button.nodenum = count
        buttonlist.append(leftwidget.button)
        textlength = max(leftwidget.button.sizeHint().width()+5, 210)
        X = 120 + buttoncount // 20 * 210
        Y = 80 + buttoncount % 20 * 35
        leftwidget.button.setGeometry(X, Y,  textlength, 30)
        leftwidget.button.position.setX(X)
        leftwidget.button.position.setY(Y)
        buttoncount += 1
        leftwidget.button.show()
    
    def add_Decision(self):
        global leftwidget
        global buttonlist
        global buttoncount
        count = 0
        leftwidget.button = Decision_Button('Decision', self)
        leftwidget.button.string = 'Decision'
        for i in buttonlist:
            if i.mode == 'Decision':
                count = count + 1
        leftwidget.button.nodenum = count
        leftwidget.button.setStyleSheet("background-color: beige; border-radius: 10px; border-style: outset; border-radius: 10px; font:Bold")
        buttonlist.append(leftwidget.button)
        X = 120 + buttoncount // 20 * 210
        Y = 80 + buttoncount % 20 * 35
        leftwidget.button.setGeometry(X, Y,  210, 30)
        leftwidget.button.position.setX(X)
        leftwidget.button.position.setY(Y)
        buttoncount += 1
        leftwidget.button.show()
    
    def add_Loop(self):
        global leftwidget
        global buttonlist
        global figure
        global buttoncount
        count = 0
        
        leftwidget.button = Loop_Button('Loop', self)
        leftwidget.button.setText('Loop')
        leftwidget.button.string = 'Loop'
        for i in buttonlist:
            if i.string == 'Loop':
                count = count + 1
        leftwidget.button.nodenum = count
        menu = QMenu(self)
        end_action = QAction(menu)
        end_action.setText("add end point")
        menu.addAction(end_action)
        end_action.triggered.connect(lambda checked, string = leftwidget.button.string + str(leftwidget.button.nodenum):self.add_Loop_end(string))
        leftwidget.button.setMenu(menu)
        leftwidget.button.setStyleSheet("QPushButton::menu-indicator{image:none;}")
        leftwidget.button.setStyleSheet("background-color: Orange; border-style: outset; border-radius: 10px; font:Bold")
        buttonlist.append(leftwidget.button)
        X = 120 + buttoncount // 20 * 210
        Y = 80 + buttoncount % 20 * 35
        leftwidget.button.setGeometry(X, Y,  210, 30)
        leftwidget.button.position.setX(X)
        leftwidget.button.position.setY(Y)
        buttoncount += 1
        leftwidget.button.show()

        
    def add_Loop_end(self, Loop_name):                                                      #insert name of loop will be ended
        global leftwidget
        global buttonlist
        global figure
        global buttoncount
        count = 0
        
        leftwidget.button = Loop_end('Loop End', self)
        leftwidget.button.string = Loop_name + 'end'
        for i in buttonlist:
            if i.mode == 'Loop_end':
                count = count + 1
        leftwidget.button.nodenum = count
        leftwidget.button.setStyleSheet("QPushButton::menu-indicator{image:none;}")
        leftwidget.button.setStyleSheet("background-color: Orange; border-style: outset; border-radius: 10px; font:Bold")
        buttonlist.append(leftwidget.button)
        X = 120 + buttoncount // 20 * 210
        Y = 80 + buttoncount % 20 * 35
        leftwidget.button.setGeometry(X, Y,  210, 30)
        leftwidget.button.position.setX(X)
        leftwidget.button.position.setY(Y)
        buttoncount += 1
        leftwidget.button.show()
        
    def show_intro(self, name):
        t = eval(name + '()')
        block_intro = t.intro_str
        dia = QMessageBox.information(self, "intro", block_intro, QMessageBox.Close)
        
    def add_line(self):
        global linemode
        global paintarray
        global linetype
        global buttonlist
        
        if linemode == 0:
            linemode = 1
            linetype = 'true'
            for i in buttonlist:
                if i.dragable == True:
                    i.dragable = False
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
        global buttonlist
        
        if linemode == 0:
            linemode = 1
            linetype = 'false'
            for i in buttonlist:
                if i.dragable == True:
                    i.dragable = False
        else :
            if linetype == 'true':
                linetype = 'false'
                paintarray = []
            else:
                linemode = 0
                paintarray = []
    
    def show_RPM(self):
        if(self.start_run.isPaintRPM == True):
            self.start_run.isPaintRPM = False
        else:
            self.start_run.isPaintRPM = True
    def show_WindSpeed(self):
        if(self.start_run.isPaintWindSpeed == True):
            self.start_run.isPaintWindSpeed = False
        else:
            self.start_run.isPaintWindSpeed = True
    def show_Power(self):
        if(self.start_run.isPaintPower == True):
            self.start_run.isPaintPower = False
        else:
            self.start_run.isPaintPower = True
    def draw_intro(self):
        dia = QMessageBox()
        dia.setIconPixmap(QPixmap("picture/123.png"))
        dia.setStandardButtons(QMessageBox.Close)
        dia.setWindowTitle('Intro')
        dia.exec()
    def full_buttonlist(self):
        global buttonlist
        global linearray
        
        for i in buttonlist:
            a = []
            if i.mode == 'process': 
                for j in range(len(linearray)):
                    if linearray[j][1].string == i.string and linearray[j][1].nodenum == i.nodenum:
                        a.append(linearray[j][3])
                    if linearray[j][0].string == i.string and linearray[j][0].nodenum == i.nodenum:           #找線
                        i.next_index = linearray[j][3]
    
            if i.mode == 'Decision': 
                for j in range(len(linearray)):
                    if linearray[j][1].string == i.string and linearray[j][1].nodenum == i.nodenum:
                        a.append(linearray[j][3])
                    if linearray[j][0].string == i.string and linearray[j][0].nodenum == i.nodenum:           #找線
                        
                        if linearray[j][2] == 'true':
                            i.true_index = linearray[j][3]
                                
                        else:
                            i.false_index = linearray[j][3]
                            
            if i.mode == 'Loop': 
                for j in range(len(linearray)):
                    if linearray[j][1].string == i.string and linearray[j][1].nodenum == i.nodenum:
                        a.append(linearray[j][3])
                    if linearray[j][0].string == i.string and linearray[j][0].nodenum == i.nodenum:           #找線
                        
                        if linearray[j][2] == 'true':
                            i.cont_index = linearray[j][3]
                                
                        else:
                            i.break_index = linearray[j][3]
            i.inputline = a
            
    def start_run(self):
        global buttonlist
        global linearray
        global figure
        global errorlabel
        global scrollarealayout
        
        
        finallist = []
     
        self.full_buttonlist()
        for i in buttonlist:
            if i.mode == 'process':
                if i.ExtremePoint == 0:
                    if i.next_index == 'null':
                        i.next_index = ''
                    pac = ["Mode_" + i.string + str(i.nodenum), i.string, i.inputline, [i.next_index]]
                    #pac = [i.string + str(i.nodenum), i.string, i.inputline, [i.next_index]]
                
                else:
                    if i.string == 'End':
                        pac = [i.string+str(i.nodenum), 'ExtremePointMode', i.inputline, []]
                    else:
                        if i.next_index == 'null':
                            i.next_index = ''
                        pac = [i.string, 'ExtremePointMode', i.inputline, [i.next_index]]
            if i.mode == 'Decision': 
                if i.true_index == 'null':
                    i.true_index = ''
                if i.false_index == 'null':
                    i.false_index = ''
                pac = [i.string+str(i.nodenum), 'Decide', i.inputline, [i.true_index, i.false_index], [i.compare_stuff, i.compare_num, i.compare_symbol]]
            if i.mode == 'Loop':
                if i.cont_index == 'null':
                    i.cont_index = ''
                if i.break_index =='null':
                    i.break_index = ''
                pac = [i.string+str(i.nodenum), i.string, i.inputline, [i.cont_index, i.break_index], [i.compare_stuff, i.compare_num, i.compare_symbol], i.loop_time]
            finallist.append(pac)
        errormsg = ''
        errormsg = FrameworkDebugger.TestErrorRaise(finallist)
        
        if errormsg  != '':
            errorlabel.setText(errormsg)
        else:
            errorlabel.setText(errormsg)
            a = CompileList.execBlockChart(finallist)
            t = eval(a[len(a)-1].__class__.__name__ + '()')
            parameter_name = t.AllVariables
            parameter_value = []
            for i in range(len(parameter_name)):
                parameter_value.append(eval('a[len(a)-1].' + parameter_name[i]))
            
            templayout = QVBoxLayout()
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(QLabel('Name'))
            layout.addWidget(QLabel('Value'))
            templayout.addWidget(widget)
            
            for i in range(len(parameter_name)):
                widget = QWidget()
                layout = QHBoxLayout(widget)
                layout.addWidget(QLabel(parameter_name[i]))
                layout.addWidget(QLabel(str(parameter_value[i])))
                templayout.addWidget(widget)
            scrollarealayout = templayout
            

            
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = HelloWindow()
        mainWin.setMinimumWidth(1200)
        mainWin.setMinimumHeight(500)
        mainWin.show()
        sys.exit(app.exec_())
    run_app()
    