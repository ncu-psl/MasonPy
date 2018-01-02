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
    while 1:
            line=file.readline()
            if line=="":
                    break
            line=line[:len(line)-1].split(",")
            for i in range(0,100):     
                Parameter.TimeSeries.append(int(line[0])*100+i)
                Parameter.WindSpeed.append(float(line[1]))
    file.close()
    return size(Parameter.WindSpeed), Parameter.TimeSeries, Parameter.WindSpeed



def ReadData_ThreePhaseShortCircuit():        
    file=open("dataThreePhaseShortCircuit.txt")
    next(file)        # skip comment out (first row )
    Clear_ThreePhaseShortCircuit()
    for line in file:
        line=line[:len(line)-1].split(",")    
        Parameter.WindSpeed_ThreePhaseShortCircuit.append(float(line[0]))
        Parameter.eff_g_ThreePhaseShortCircuit.append(float(line[1]))
        Parameter.eff_e_ThreePhaseShortCircuit.append(float(line[2]))
        
        Parameter.RPM_ThreePhaseShortCircuit.append(float(line[3]))
        Parameter.Tg_ThreePhaseShortCircuit.append(float(line[4]))
    file.close()
    Parameter.Tsr_ThreePhaseShortCircuit, Parameter.Cp_ThreePhaseShortCircuit = ReadData_MaxTorqueCurrent()
    return Parameter.WindSpeed_ThreePhaseShortCircuit, Parameter.eff_g_ThreePhaseShortCircuit, Parameter.eff_e_ThreePhaseShortCircuit,  Parameter.RPM_ThreePhaseShortCircuit, Parameter.Tg_ThreePhaseShortCircuit, Parameter.Tsr_ThreePhaseShortCircuit, Parameter.Cp_ThreePhaseShortCircuit



def ReadData_MaxPower():        
    file=open("dataMaxPower.txt")
    next(file)        # skip comment out (first row )
    Clear__MaxPower()
    for line in file:
        line=line[:len(line)-1].split(",")    
        Parameter.WindSpeed_MaxPower.append(float(line[0]))
        Parameter.eff_g_MaxPower.append(float(line[1]))
        Parameter.eff_e_MaxPower.append(float(line[2]))
        
        Parameter.RPM_MaxPower.append(float(line[3]))
        Parameter.Tg_MaxPower.append(float(line[4]))
    file.close()
    Parameter.Tsr_MaxPower, Parameter.Cp_MaxPower = ReadData_MaxTorqueCurrent()
    return Parameter.WindSpeed_MaxPower, Parameter.eff_g_MaxPower, Parameter.eff_e_MaxPower,Parameter.RPM_MaxPower, Parameter.Tg_MaxPower,Parameter.Tsr_MaxPower, Parameter.Cp_MaxPower



def ReadData_MaxTorqueCurrent():        
    file=open("dataMaxTorqueCurrent.txt")
    next(file)        # skip comment out (first row )
    Clear__MaxTorqueCurrent()
    for line in file:
        line=line[:len(line)-1].split(",")    
        Parameter.Tsr__MaxTorqueCurrent.append(float(line[0]))
        Parameter.Cp_MaxTorqueCurrent.append(float(line[1]))
        
    file.close()
    return Parameter.Tsr__MaxTorqueCurrent, Parameter.Cp_MaxTorqueCurrent


def Clear_ThreePhaseShortCircuit():
    Parameter.WindSpeed_ThreePhaseShortCircuit = []
    Parameter.eff_g_ThreePhaseShortCircuit     = []
    Parameter.eff_e_ThreePhaseShortCircuit     = []        
    Parameter.RPM_ThreePhaseShortCircuit       = []
    Parameter.Tg_ThreePhaseShortCircuit        = []
    
def Clear__MaxPower():  
    Parameter.WindSpeed_MaxPower = []
    Parameter.RPM_MaxPower       = []
    Parameter.Cp_MaxPower        = []
    Parameter.eff_g_MaxPower     = []
    Parameter.eff_e_MaxPower     = []
    Parameter.Tg_MaxPower        = []

def Clear__MaxTorqueCurrent():
    Parameter.Tsr__MaxTorqueCurrent = []
    Parameter.Cp_MaxTorqueCurrent   = []

if __name__=='__main__':
    
#==============================================================================
#     # ReadWindSpeepData
#     TimeSeries = [] 
#     WindSpeed = []
#     Number, TimeSeries, WindSpeed = ReadWindSpeepData()
#     print('資料數',Number,'筆')   # print Number of data
#     print("TimeSeries")
#     print(TimeSeries)
#     print("WindSpeed")
#     print(WindSpeed)
#==============================================================================



    # ReadData_ThreePhaseShortCircuit    
    WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit, eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit = ReadData_ThreePhaseShortCircuit()
    
    print("WindSpeed_ThreePhaseShortCircuit")
    print(WindSpeed_ThreePhaseShortCircuit)
    print("eff_g_ThreePhaseShortCircuit")
    print(eff_g_ThreePhaseShortCircuit)
    print("eff_e_ThreePhaseShortCircuit")
    print(eff_e_ThreePhaseShortCircuit)
    
    print("RPM_ThreePhaseShortCircuit")
    print(RPM_ThreePhaseShortCircuit)
    print("Tg_ThreePhaseShortCircuit")
    print(Tg_ThreePhaseShortCircuit)
    
    print("Tsr_ThreePhaseShortCircuit")
    print(Tsr_ThreePhaseShortCircuit)
    print("Cp_ThreePhaseShortCircuit")
    print(Cp_ThreePhaseShortCircuit)
    
    
    
    # ReadData_MaxPower   
    Wind_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPM_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower = ReadData_MaxPower()
    
    print("Wind_MaxPower")
    print(Wind_MaxPower)
    print("eff_g_MaxPower")
    print(eff_g_MaxPower)
    print("eff_e_MaxPower")
    print(eff_e_MaxPower)
    
    print("RPM_MaxPower")
    print(RPM_MaxPower)
    print("Tg_MaxPower")
    print(Tg_MaxPower)
    
    
    print("Tsr_MaxPower")
    print(Tsr_MaxPower)
    print("Cp_MaxPower")
    print(Cp_MaxPower)
    
    #ReadData_MaxTorqueCurrent    
    Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent = ReadData_MaxTorqueCurrent()
    
    print("Tsr__MaxTorqueCurrent")
    print(Tsr__MaxTorqueCurrent)
    print("Cp_MaxTorqueCurrent")
    print(Cp_MaxTorqueCurrent)
