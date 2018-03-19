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
<<<<<<< HEAD
        ['Start0', 'Start', [], ['line_0']],
['Mode_ThreePhaseShortCircuit0', 'Mode_ThreePhaseShortCircuit', ['line_0', 'line_16', 'line_17', 'line_19', 'line_24'], ['line_1']],
['Check_MaxMagBrake0', 'Check_MaxMagBrake', ['line_1'], ['line_2', 'line_15']],
['Check_MaxWindSpeed_ThreePhaseShortCircuit0', 'Check_MaxWindSpeed_ThreePhaseShortCircuit', ['line_15'], ['line_3', 'line_16']],
['Loop0', 'Loop', ['line_3'], ['line_4', 'line_17'], 0, 200],
['Mode_MaxPower0', 'Mode_MaxPower', ['line_4', 'line_18'], ['line_5']],
['Check_CutOut0', 'Check_CutOut', ['line_5'], ['line_6', 'line_18']],
['Mode_MaxTorqueCurrent0', 'Mode_MaxTorqueCurrent', ['line_6', 'line_20'], ['line_7']],
['Check_MaxMagBrake1', 'Check_MaxMagBrake', ['line_7'], ['line_8', 'line_19']],
['Check_RPM_Increase0', 'Check_RPM_Increase', ['line_8'], ['line_9', 'line_20']],
['Mode_MaxTorqueCurrent1', 'Mode_MaxTorqueCurrent', ['line_9', 'line_21'], ['line_10']],
['Loop1', 'Loop', ['line_10'], ['line_11', 'line_21'], 0, 200],
['Mode_MaxTorqueCurrent_MagBrake0', 'Mode_MaxTorqueCurrent_MagBrake', ['line_2', 'line_11', 'line_14'], ['line_12']],
['Check_MaxMagBrake2', 'Check_MaxMagBrake', ['line_12'], ['line_14', 'line_22']],
['Mode_ThreePhaseShortCircuit_MagBrake0', 'Mode_ThreePhaseShortCircuit_MagBrake', ['line_22', 'line_23'], ['line_13']],
['Loop2', 'Loop', ['line_13'], ['line_24', 'line_23'], 0, 200]                         #15  
=======
        ["Start", "Start",["Null"] ,["L1"]],                                             #0
        ["Mode1", "Mode_ThreePhaseShortCircuit",["L1", "L5", "L7", "L25"], ["L2"]],      #1
        ["Check1", "Check_MaxMagBrake", ["L2"], ["L3", "L4"]],                           #2     
        ["Check2", "Check_MaxWindSpeed_ThreePhaseShortCircuit", ["L4"], ["L6", "L5"]],   #3
        ["Loop1","Loop", ["L6"], ["L7", "L8"], 0, 200],                                  #4     
        ["Mode2", "Mode_MaxPower",["L8", "L11"],["L9"]],                                 #5 
        ["Check3", "Check_CutOut",["L9"], ["L10", "L11"]],                               #6
        ["Mode3", "Mode_MaxTorqueCurrent",["L10", "L15"], ["L12"]],                      #7
        ["Check4", "Check_MaxMagBrake",["L12"], ["L14", "L13"]],                         #8
        ["Check5", "Check_RPM_Increase",["L14"], ["L16", "L15"]],                        #9      
        ["Mode4", "Mode_MaxTorqueCurrent",["L16", "L18"], ["L17"]],                      #10     
        ["Loop2", "Loop", ["L17"], ["L19", "L18"], 0, 8],                                #11   # 持續8秒
        ["Mode5", "Mode_MaxTorqueCurrent_MagBrake",["L3", "L19", "L22"], ["L20"]],       #12     
        ["Check6", "Check_MaxMagBrake", ["L20"], ["L22", "L21"]],                        #13  
        ["Mode6", "Mode_ThreePhaseShortCircuit_MagBrake", ["L21", "L24"], ["L23"]],      #14      
        ["Loop3", "Loop", ["L23"], ["L25", "L24"], 0, 2080]                              #15  
>>>>>>> 23bf9c636b9260579d259e73b2250b3cd4868c7d
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
Paint.PaintDiagram("Wind Turbine Control System", "Time (s)", "WindSpeed  (m/s)", "RPM", "Power   ( W )", Parameter.TimeSeries,  isPaintWindSpeed, Parameter.WindSpeed, isPaintRPM, Parameter.RPM, isPaintPower, Parameter.Power)

#ExportData.ExportExcelData(Parameter.TimeSeries, Parameter.WindSpeed, Parameter.RPM, Parameter.Power, Parameter.CpStack, Parameter.eff_gStack, ModeStack)


end = time.time()
print("execution time(s) = %f "%(end-start))
