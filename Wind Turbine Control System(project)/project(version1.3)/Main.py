# @Wind turbine control system
# @ 
# @author:  NTOU Systems Engineering & Naval Architecture
# @         NCU Promming & Software Lab 
# @ 
# @version: 2017 A.D version 1.1
# @
# @import OpenWindSpeedFile
# @input file:  WindSpeed.txt
# @parameter Number      : It is  number of data .
# @parameter TimeSeries
# @parameter WindSpeed   : It is WindSpeed. unit: m/s( Meters per second).
#==============================================================================


import OpenFile
import Parameter
import Formula
import Paint
import time
import CompileBlock
import ExportData

start = time.time()


OpenFile.ReadWindSpeepData()
OpenFile.ReadData_ThreePhaseShortCircuit()
OpenFile.ReadData_MaxPower()
OpenFile.ReadData_MaxTorqueCurrent()


Parameter.RPM.append(0.0001)
Parameter.Power.append(0)

list=[
        ["Start", 1],                                        #0
        ["Mode_ThreePhaseShortCircuit", 2],                  #1
        ["Check_MaxMagBrake", 12, 3],                        #2
        ["Check_MaxWindSpeed_ThreePhaseShortCircuit", 4, 1], #3
        ["Loop", 5, 1, 200, 0],                              #4
        ["Mode_MaxPower", 6],                                #5 
        ["Check_CutOut", 7, 5],                              #6
        ["Mode_MaxTorqueCurrent", 8],                        #7
        ["Check_MaxMagBrake", 9, 1],                         #8
        ["Check_RPM_Increase", 10, 7],                       #9 
        ["Mode_MaxTorqueCurrent", 11],                       #10
        ["Loop", 12, 10, 8, 0],                              #11
        ["Mode_MaxTorqueCurrent_MagBrake", 13],              #12
        ["Check_MaxMagBrake", 12, 14],                       #13  
        ["Mode_ThreePhaseShortCircuit_MagBrake", 15],        #14 
        ["Loop", 1, 14, 2080, 0]                             #15
    ]

                
CompileBlock.execBlockChart(list)

Parameter.TimeSeries.pop(0)
Parameter.WindSpeed.pop(0)
Parameter.RPM.pop(0)
Parameter.Power.pop(0)

Mode  = []
Mode.append("default value")
Mode = Mode + Parameter.listMode
speed = Parameter.WindSpeed                
rpm   = Parameter.RPM
power = Parameter.Power 



TsrStack     = Parameter.TsrStack
CpStack      = Parameter.CpStack
TbStack      = Parameter.TbStack
TgStack      = Parameter.TgStack
TmStack      = Parameter.TmStack
TtotalStack  = Parameter.TtotalStack
eff_gStack   = Parameter.eff_gStack
eff_eStack   = Parameter.eff_eStack


Paint.PaintDiagram("Speed-Time Diagram", "WindSpeed", Parameter.TimeSeries, Parameter.WindSpeed)
Paint.PaintDiagram("RPM-Time Diagram", "RPM", Parameter.TimeSeries, Parameter.RPM)
Paint.PaintDiagram("Power-Time Diagram", "Power", Parameter.TimeSeries, Parameter.Power)

ExportData.ExportExcelData(Parameter.TimeSeries, Parameter.WindSpeed, Parameter.RPM, CpStack, eff_gStack, Parameter.Power, Mode)


end = time.time()
print("execution time(s) = %f "%(end-start))
