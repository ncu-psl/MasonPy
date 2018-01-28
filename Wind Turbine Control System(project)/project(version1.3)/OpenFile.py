#==============================================================================
# @Read the files
# 
# @input file:  WindSpeed.txt
# @parameter TimeSeries
# @parameter WindSpeed   : It is WindSpeed.unit: m/s(Meters per second).
#
# @input file:  threephaseshortcircuit.txt
#==============================================================================

from numpy import*
import Parameter 

def ReadWindSpeepData():        
    file=open("1speed.txt")
    #file=open("testWindSpeed.txt")
    
    OriginalTimeSeries = []
    OriginalWindSpeed  = []
    
    while 1:
        line=file.readline()
        if line=="":
                break
        line=line[:len(line)-1].split(",")   
        OriginalTimeSeries.append(int(line[0]))
        OriginalWindSpeed.append(float(line[1]))
    file.close()        
    
    
    extendTimeSeries, extendWindSpeed  = extentWindSpeepData(size(OriginalTimeSeries), OriginalTimeSeries, OriginalWindSpeed)          
    
#==============================================================================
#     # 1s
#     Parameter.TimeSeries =  Parameter.TimeSeries + OriginalTimeSeries
#     Parameter.WindSpeed  =  Parameter.WindSpeed + OriginalWindSpeed
#==============================================================================
                    
    # 1ms
    Parameter.TimeSeries =  Parameter.TimeSeries + extendTimeSeries
    Parameter.WindSpeed  =  Parameter.WindSpeed + extendWindSpeed
    
    
    return size(Parameter.TimeSeries), Parameter.TimeSeries, Parameter.WindSpeed



def extentWindSpeepData(number, OriginalTimeSeries, OriginalWindSpeed):
    extendTimeSeries = []
    extendWindSpeed  = []
    extendTimeSeries.append(OriginalTimeSeries[0]*100)
    extendWindSpeed.append(OriginalWindSpeed[0])
    
    for i in range(0, number-1):
        detaWindSpeed = OriginalWindSpeed[i+1] - OriginalWindSpeed[i]
        for j in range(1,101):
            extendTimeSeries.append(OriginalTimeSeries[i]*100 + j)
        for k in range(1,101):  # extendWindSpeed
            extendWindSpeed.append(OriginalWindSpeed[i] + detaWindSpeed*k/100)
    return extendTimeSeries, extendWindSpeed    
            
            
        
    

def readData(filename):
    file=open(filename)
    next(file)        # skip comment out (first row )
    domainlist = []
    rangelist  = []
    for line in file:
        line=line[:len(line)-1].split(",")    
        domainlist.append(float(line[0]))
        rangelist.append(float(line[1]))
    file.close()
    return domainlist, rangelist



def ReadData_ThreePhaseShortCircuit():        
    Parameter.WindSpeed_ThreePhaseShortCircuit, Parameter.eff_g_ThreePhaseShortCircuit =  readData("data_WindspeedToEff_g.txt")
    # Parameter.eff_e__ThreePhaseShortCircuit setting in Parameter.py
    Parameter.RPM_ThreePhaseShortCircuit, Parameter.Tg_ThreePhaseShortCircuit          =  readData("dataThreePhaseShortCircuit_RPMToTg.txt")
    Parameter.Tsr_ThreePhaseShortCircuit, Parameter.Cp_ThreePhaseShortCircuit          =  readData("data_TsrToCp.txt") 
    return Parameter.WindSpeed_ThreePhaseShortCircuit, Parameter.eff_g_ThreePhaseShortCircuit,  Parameter.eff_e_ThreePhaseShortCircuit, Parameter.RPM_ThreePhaseShortCircuit, Parameter.Tg_ThreePhaseShortCircuit, Parameter.Tsr_ThreePhaseShortCircuit, Parameter.Cp_ThreePhaseShortCircuit



def ReadData_MaxPower():        
    Parameter.WindSpeed_MaxPower, Parameter.eff_g_MaxPower   =  readData("data_WindspeedToEff_g.txt")
    # Parameter.eff_e_MaxPower setting in Parameter.py
    Parameter.RPM_MaxPower, Parameter.Tg_MaxPower            =  readData("dataMaxPower_RPMToTg.txt")
    Parameter.Tsr_MaxPower, Parameter.Cp_MaxPower                      =  readData("data_TsrToCp.txt") 
    return Parameter.WindSpeed_MaxPower, Parameter.eff_g_MaxPower, Parameter.eff_e_MaxPower, Parameter.RPM_MaxPower, Parameter.Tg_MaxPower,Parameter.Tsr_MaxPower, Parameter.Cp_MaxPower



def ReadData_MaxTorqueCurrent():        
    # Parameter.eff_g_MaxTorqueCurrent setting in Parameter.py
    # Parameter.eff_e_MaxTorqueCurrent setting in Parameter.py
    Parameter.Tsr__MaxTorqueCurrent, Parameter.Cp_MaxTorqueCurrent = readData("data_TsrToCp.txt")
    return Parameter.eff_g_MaxTorqueCurrent, Parameter.eff_e_MaxTorqueCurrent, Parameter.TorqueGenerator_MaxTorqueCurrent, Parameter.Tsr__MaxTorqueCurrent, Parameter.Cp_MaxTorqueCurrent


if __name__=='__main__':
    
    # ReadWindSpeepData
    TimeSeries = [] 
    WindSpeed = []
    Number, TimeSeries, WindSpeed = ReadWindSpeepData()
    print('資料數',Number,'筆')   # print Number of data
#==============================================================================
#     print("TimeSeries")
#     print(TimeSeries)
#==============================================================================
#==============================================================================
#     print("WindSpeed")
#     print(WindSpeed)
# 
#==============================================================================


#==============================================================================
#     # ReadData_ThreePhaseShortCircuit    
#     WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit, eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit = ReadData_ThreePhaseShortCircuit()
#     
#     print("WindSpeed_ThreePhaseShortCircuit")
#     print(WindSpeed_ThreePhaseShortCircuit)
#     print("eff_g_ThreePhaseShortCircuit")
#     print(eff_g_ThreePhaseShortCircuit)
#     print("eff_e_ThreePhaseShortCircuit")
#     print(eff_e_ThreePhaseShortCircuit)
#     
#     print("RPM_ThreePhaseShortCircuit")
#     print(RPM_ThreePhaseShortCircuit)
#     print("Tg_ThreePhaseShortCircuit")
#     print(Tg_ThreePhaseShortCircuit)
#     
#     print("Tsr_ThreePhaseShortCircuit")
#     print(Tsr_ThreePhaseShortCircuit)
#     print("Cp_ThreePhaseShortCircuit")
#     print(Cp_ThreePhaseShortCircuit)
#==============================================================================
    
    
#==============================================================================
#     
#     # ReadData_MaxPower   
#     
#     WindSpeed_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPM_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower = ReadData_MaxPower()
#     
#     print("WindSpeed_MaxPower")
#     print(WindSpeed_MaxPower)
#     print("eff_g_MaxPower")
#     print(eff_g_MaxPower)
#     print("eff_e_MaxPower")
#     print(eff_e_MaxPower)
#     
#     print("RPM_MaxPower")
#     print(RPM_MaxPower)
#     print("Tg_MaxPower")
#     print(Tg_MaxPower)
#     
#     
#     print("Tsr_MaxPower")
#     print(Tsr_MaxPower)
#     print("Cp_MaxPower")
#     print(Cp_MaxPower)
#==============================================================================
    
#==============================================================================
#     #ReadData_MaxTorqueCurrent    
#     eff_g_MaxTorqueCurrent, eff_e_MaxTorqueCurrent, Tg_MaxTorqueCurrent, Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent = ReadData_MaxTorqueCurrent()
#     print("eff_g_MaxTorqueCurrent")
#     print(eff_g_MaxTorqueCurrent)
#     print("eff_e_MaxTorqueCurrent")
#     print(eff_e_MaxTorqueCurrent)
#     
#     print("Tg_MaxTorqueCurrent")
#     print(Tg_MaxTorqueCurrent)
#     
#     print("Tsr__MaxTorqueCurrent")
#     print(Tsr__MaxTorqueCurrent)
#     print("Cp_MaxTorqueCurrent")
#     print(Cp_MaxTorqueCurrent)
#==============================================================================

