import GUI
import sys
import OpenFile
# =============================================================================
# 
# OpenFile.ReadWindSpeepData()
# OpenFile.ReadData_ThreePhaseShortCircuit()
# OpenFile.ReadData_MaxPower()
# OpenFile.ReadData_MaxTorqueCurrent()
# =============================================================================
app = GUI.QApplication(sys.argv)
mainWin = GUI.HelloWindow()
mainWin.setMinimumWidth(500)
mainWin.setMinimumHeight(500)
mainWin.show()
sys.exit(app.exec_())