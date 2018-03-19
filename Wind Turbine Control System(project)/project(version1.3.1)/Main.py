import GUI
import sys

app = GUI.QApplication(sys.argv)
mainWin = GUI.HelloWindow()
mainWin.setMinimumWidth(500)
mainWin.setMinimumHeight(500)
mainWin.show()
sys.exit(app.exec_())