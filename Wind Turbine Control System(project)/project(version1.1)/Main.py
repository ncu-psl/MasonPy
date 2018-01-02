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
start = time.time()


OpenFile.ReadWindSpeepData()
OpenFile.ReadData_ThreePhaseShortCircuit()
OpenFile.ReadData_MaxPower()
OpenFile.ReadData_MaxTorqueCurrent()


list=[
        ["Start", 1], 
        ["Mode_ThreePhaseShortCircuit", 2],
        ["Check_MaxMagBrake", 10, 3],   
        ["Check_MaxWindSpeed_ThreePhaseShortCircuit", 4, 1],
        ["Loop", 5, 1, 200, 0],
        ["Mode_MaxPower", 6],
        ["Check_CutOut", 7, 5],
        ["Mode_MaxTorqueCurrent", 8],
        ["Check_MaxMagBrake", 9, 1],
        ["Check_RPM_Increase", 10, 7],
        ["Mode_MaxTorqueCurrent_MagBrake", 11],
        ["Check_MaxMagBrake", 10, 12],
        ["Mode_ThreePhaseShortCircuit_MagBrake", 13],
        ["Loop", 1, 12, 2080, 0]
    ]

                
CompileBlock.execBlockChart(list)

Parameter.TimeSeries.pop(0)
Parameter.WindSpeed.pop(0)
Parameter.RPM.pop(0)
Parameter.Power.pop(0)

Mode  = Parameter.listMode
speed = Parameter.WindSpeed                
rpm   = Parameter.RPM
power = Parameter.Power 


Paint.PaintDiagram("Speed-Time Diagram", "WindSpeed", Parameter.TimeSeries, Parameter.WindSpeed)
Paint.PaintDiagram("RPM-Time Diagram", "RPM", Parameter.TimeSeries, Parameter.RPM)
Paint.PaintDiagram("Power-Time Diagram", "Power", Parameter.TimeSeries, Parameter.Power)

end = time.time()
print("execution time(s) = %f "%(end-start))
