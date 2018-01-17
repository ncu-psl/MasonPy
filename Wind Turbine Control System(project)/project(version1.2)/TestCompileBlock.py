import Parameter
import Formula
import OpenFile

def evalProcess(str):
    return eval("Formula."+str+"(Reg_Time, Reg_WinsSpeed, Reg_RPM, Reg_Power)")
    
def PrintParameter():
    global Reg_Time
    global Reg_WinsSpeed
    global Reg_RPM
    global Reg_Power
    print('CurrentTime', Reg_Time, 'CurrentWinsSpeed', Reg_WinsSpeed,'CurrentRPM', Reg_RPM, 'CurrentPower', Reg_Power )

def evalDecision(str):
    return eval("Formula."+str+"(Reg_Time, Reg_WinsSpeed, Reg_RPM, Reg_Power)")
    
def execProcess(str,value):
    exec(str +"(" + "value" +")")
    
OpenFile.ReadWindSpeepData()
OpenFile.ReadData_ThreePhaseShortCircuit()
OpenFile.ReadData_MaxPower()
OpenFile.ReadData_MaxTorqueCurrent()

Reg_Time = 0
Reg_WinsSpeed = 0
Reg_RPM = 0.0000001
Reg_Power = 0

PrintParameter()

for i in range(9):
    str = 'Mode_ThreePhaseShortCircuit'
    Reg_Time, Reg_WinsSpeed, Reg_RPM, Reg_Power = evalProcess(str) 
    PrintParameter()

