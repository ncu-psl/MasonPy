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

def ReadWindSpeepData():        
    file=open("./TurbineData/1speed.txt")
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
#     TimeSeries =  TimeSeries + OriginalTimeSeries
#     WindSpeed  =  WindSpeed + OriginalWindSpeed
#==============================================================================

                
    # 1ms
    TimeSeries =  extendTimeSeries
    WindSpeed  =  extendWindSpeed
    
    
    return size(TimeSeries), TimeSeries, WindSpeed



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
    
    # eff_g_ThreePhaseShortCircuit and eff_e_ThreePhaseShortCircuit setting in py
    eff_g_ThreePhaseShortCircuit  = 0
    eff_e_ThreePhaseShortCircuit = 0.9
    WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit =  readData("./TurbineData/data_WindspeedToEff_g.txt")
    RPM_ThreePhaseShortCircuit, Tg_ThreePhaseShortCircuit          =  readData("./TurbineData/dataThreePhaseShortCircuit_RPMToTg.txt")
    Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit          =  readData("./TurbineData/data_TsrToCp.txt") 
    return WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit,  eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit, Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit



def ReadData_MaxPower():        
    RPMtoEffg_MaxPower, eff_g_MaxPower   =  readData("./TurbineData/dataMaxPower_RPMToEff_g.txt")
    # eff_e_MaxPower setting in py
    eff_e_MaxPower = 0.9
    RPMtoTG_MaxPower, Tg_MaxPower            =  readData("./TurbineData/dataMaxPower_RPMToTg.txt")
    Tsr_MaxPower, Cp_MaxPower                      =  readData("./TurbineData/data_TsrToCp.txt") 
    return RPMtoEffg_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPMtoTG_MaxPower, Tg_MaxPower,Tsr_MaxPower, Cp_MaxPower



def ReadData_MaxTorqueCurrent():        
    RPM_MaxTorqueCurrent, eff_g_MaxTorqueCurrent =  readData("./TurbineData/dataMaxTorqueCurrent_RPMToEff_g.txt")
    #  setting in py
    # eff_e_MaxTorqueCurrent setting in py
    eff_e_MaxTorqueCurrent = 0.9
    TorqueGenerator_MaxTorqueCurrent = 110
    Tsr_MaxTorqueCurrent, Cp_MaxTorqueCurrent = readData("./TurbineData/data_TsrToCp.txt")
    return RPM_MaxTorqueCurrent, eff_g_MaxTorqueCurrent, eff_e_MaxTorqueCurrent, TorqueGenerator_MaxTorqueCurrent, Tsr_MaxTorqueCurrent, Cp_MaxTorqueCurrent


if __name__=='__main__':
    
    # ReadWindSpeepData
    TimeSeries = [] 
    WindSpeed = []
    Number, TimeSeries, WindSpeed = ReadWindSpeepData()
    print('資料數',Number,'筆')   # print Number of data
    print("TimeSeries")
    print(TimeSeries)
    print("WindSpeed")
    print(WindSpeed)



#==============================================================================
#     # ReadData_ThreePhaseShortCircuit    
#     WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit, eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit = ReadData_ThreePhaseShortCircuit()
#     
#     print("WindSpeed_ThreePhaseShortCircuit")
#     print(WindSpeed_ThreePhaseShortCircuit)
#     
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
#     # ReadData_MaxPower   
#     
#     RPMtoEffg_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower = ReadData_MaxPower()
#     
#     print("RPMtoEffg_MaxPower")
#     print(RPMtoEffg_MaxPower)
#     print("eff_g_MaxPower")
#     print(eff_g_MaxPower)
#     print("eff_e_MaxPower")
#     print(eff_e_MaxPower)
#     
#     print("RPMtoTG_MaxPower")
#     print(RPMtoTG_MaxPower)
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
#     RPM__MaxTorqueCurrent, eff_g_MaxTorqueCurrent, eff_e_MaxTorqueCurrent, Tg_MaxTorqueCurrent, Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent = ReadData_MaxTorqueCurrent()
#     print("RPM__MaxTorqueCurrent")
#     print(RPM__MaxTorqueCurrent)
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

