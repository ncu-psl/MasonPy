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




#==============================================================================
# list=[
#         ["Start", 1],                                        #0
#         ["Mode_ThreePhaseShortCircuit", 2],                  #1
#         ["Check_MaxMagBrake", 12, 3],                        #2
#         
#         ["Check_MaxWindSpeed_ThreePhaseShortCircuit", 4, 1], #3
#         ["Loop", 5, 1, 200, 0],                              #4
#         
#         ["Mode_MaxPower", 6],                                #5 
#         ["Check_CutOut", 7, 5],                              #6
#         ["Mode_MaxTorqueCurrent", 8],                        #7
#         ["Check_MaxMagBrake", 9, 1],                         #8
#         ["Check_RPM_Increase", 10, 7],                       #9 
#         
#         ["Mode_MaxTorqueCurrent", 11],                       #10
#         ["Loop", 12, 10, 8, 0],                              #11   # 持續8秒
#         
#         ["Mode_MaxTorqueCurrent_MagBrake", 13],              #12
#         ["Check_MaxMagBrake", 12, 14],                       #13  
#         ["Mode_ThreePhaseShortCircuit_MagBrake", 15],        #14 
#         
#         ["Loop", 1, 14, 2080, 0]                             #15
#     
#     ]
#==============================================================================











#==============================================================================
# [Modename  , functionname,, inputlinelist[] ,outputline[]]
# [Checkname , functionname, inputlinelist[] ,outputlinelist[ture,false]]
# [Loopname  , functionname, inputlinelist[] ,outputline[]]
#==============================================================================



list=[
        ["Start", "Start",["Null"] ,["L1"]],                                        #0
        ["Mode1", "Mode_ThreePhaseShortCircuit",["L1", "L5", "L7", "L25"], ["L2"]],                  #1
        ["Check1", "Check_MaxMagBrake", ["L2"], ["L3", "L4"]],                        #2     
        ["Check2", "Check_MaxWindSpeed_ThreePhaseShortCircuit", ["L4"], ["L6", "L5"]], #3
        ["Loop1","Loop", ["L6"], ["L7", "L8"], 0, 200],                              #4     
        ["Mode2", "Mode_MaxPower",["L8", "L11"],["L9"]],                                #5 
        ["Check3", "Check_CutOut",["L9"], ["L10", "L11"]],                              #6
        ["Mode3", "Mode_MaxTorqueCurrent",["L10", "L15"], ["L12"]],                        #7
        ["Check4", "Check_MaxMagBrake",["L12"], ["L14", "L13"]],                         #8
        ["Check5", "Check_RPM_Increase",["L14"], ["L16", "L15"]],                       #9      
        ["Mode4", "Mode_MaxTorqueCurrent",["L16", "L18"], ["L17"]],                       #10     
        ["Loop2", "Loop", ["L17"], ["L19", "L18"], 0, 8],                              #11   # 持續8秒
        ["Mode5", "Mode_MaxTorqueCurrent_MagBrake",["L3", "L19", "L22"], ["L20"]],              #12     
        ["Check6", "Check_MaxMagBrake", ["L20"], ["L22", "L21"]],                       #13  
        ["Mode6", "Mode_ThreePhaseShortCircuit_MagBrake", ["L21", "L24"], ["L23"]],        #14      
        ["Loop3", "Loop", ["L23"], ["L25", "L24"], 0, 2080]                             #15  
    ]






#==============================================================================
# list=[
#         ["Start", "Start", ["Null"], ["L1"]],                                        #0
#         ["Mode1", "Mode_ThreePhaseShortCircuit",["L1" , "L3"], ["L2"]],                  #1  
#         ["Loop3", "Loop", ["L2"], ["L3", "L3"], 0, 200000]                             #15  
#     ]
#==============================================================================




                
CompileBlock.execBlockChart(list)




Parameter.RemoveDefaultValue()


Mode  = Parameter.ModeStack
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


isPaintWindSpeed = True
isPaintRPM       = True
isPaintPower     = True  
Paint.PaintDiagram("name", "WindSpeed (m/s)", "RPM", "Power  (W)", Parameter.TimeSeries,  isPaintWindSpeed, Parameter.WindSpeed, isPaintRPM, Parameter.RPM, isPaintPower, Parameter.Power)

ExportData.ExportExcelData(Parameter.TimeSeries, Parameter.WindSpeed, Parameter.RPM, Parameter.Power, Parameter.CpStack, Parameter.eff_gStack, Mode)


end = time.time()
print("execution time(s) = %f "%(end-start))
