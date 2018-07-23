from numba import jit
import OpenFile

import BlockMode
import BlockCheck
import BlockLoop

import Mode

import initMode
import ThreePhaseShortCircuit
import ThreePhaseShortCircuit_MagBrake
import MaxPower
import MaxTorqueCurrent
import MaxTorqueCurrent_MagBrake
        
        
        

def execProcess(string, LastMoed, WindspeedList, database_dic):
    if string == 'Mode_ThreePhaseShortCircuit':
        tempMode = ThreePhaseShortCircuit.Mode_ThreePhaseShortCircuit(LastMoed, database_dic['ThreePhaseShortCircuit'], WindspeedList)
    if string == 'Mode_MaxPower':
        tempMode = MaxPower.Mode_MaxPower(LastMoed, database_dic['MaxPower'], WindspeedList)
    if string == 'Mode_MaxTorqueCurrent':
        tempMode = MaxTorqueCurrent.Mode_MaxTorqueCurrent(LastMoed, database_dic['MaxTorqueCurrent'], WindspeedList)
    if string == 'Mode_MaxTorqueCurrent_MagBrake':
        tempMode = MaxTorqueCurrent_MagBrake.Mode_MaxTorqueCurrent_MagBrake(LastMoed, database_dic['MaxTorqueCurrent'], WindspeedList)
    if string == 'Mode_ThreePhaseShortCircuit_MagBrake':
        tempMode = ThreePhaseShortCircuit_MagBrake.Mode_ThreePhaseShortCircuit_MagBrake(LastMoed, database_dic['ThreePhaseShortCircuit'], WindspeedList)
    return tempMode
        
def evalDecision(string):
    return eval("Formula."+string+"()")


def evalComparison(string, parameter, value): 
    return eval("Formula." + string + "(" +'\''+ parameter + '\'' + "," + str(value)  + ")")


@jit
def resetLoopCounter(list):
     for i in range(len(list)):
         string = list[i][1]      #  outputlist
         if string.find("Loop") != -1:
             list[i][4] = 0   #  current time counter


def FindNextBlock(list, Connectionline):
    index = -1
    for i in range(len(list)):
        if Connectionline in list[i][2]: # intputlist          
            index = i
            break;
    if index == -1:
        print("Error: Some lines are missing!")    
    return index
            
        
            
@jit
def execBlockChart(list, WindspeedList, database_dic):
    Process  = 0
    Decision = 0
    Loop     = 0
    
    for i in range(len(list)):
        string = list[i][1]
        if string.find("Mode")!= -1:
            Process += 1
        if string.find("Check")!= -1:
            Decision += 1 
        if string.find("Loop")!= -1:
            Loop += 1
    print("Process", Process)    
    print("Decision", Decision)
    print("Loop", Loop)



#==============================================================================
# list=[
#         ['Start0', 'Start', [], ['line_0']],
# ['Mode_ThreePhaseShortCircuit0', 'Mode_ThreePhaseShortCircuit', ['line_0', 'line_16', 'line_17', 'line_19', 'line_24'], ['line_1']],
# ['Check_MaxMagBrake0', 'Check_MaxMagBrake', ['line_1'], ['line_2', 'line_15']],
# ['Check_MaxWindSpeed_ThreePhaseShortCircuit0', 'Check_MaxWindSpeed_ThreePhaseShortCircuit', ['line_15'], ['line_3', 'line_16']],
# ['Loop0', 'Loop', ['line_3'], ['line_4', 'line_17'], 0, 200],
# ['Mode_MaxPower0', 'Mode_MaxPower', ['line_4', 'line_18'], ['line_5']],
# ['Check_CutOut0', 'Check_CutOut', ['line_5'], ['line_6', 'line_18']],
# ['Mode_MaxTorqueCurrent0', 'Mode_MaxTorqueCurrent', ['line_6', 'line_20'], ['line_7']],
# ['Check_MaxMagBrake1', 'Check_MaxMagBrake', ['line_7'], ['line_8', 'line_19']],
# ['Check_RPM_Increase0', 'Check_RPM_Increase', ['line_8'], ['line_9', 'line_20']],
# ['Mode_MaxTorqueCurrent1', 'Mode_MaxTorqueCurrent', ['line_9', 'line_21'], ['line_10']],
# ['Loop1', 'Loop', ['line_10'], ['line_11', 'line_21'], 0, 8],
# ['Mode_MaxTorqueCurrent_MagBrake0', 'Mode_MaxTorqueCurrent_MagBrake', ['line_2', 'line_11', 'line_14'], ['line_12']],
# ['Check_MaxMagBrake2', 'Check_MaxMagBrake', ['line_12'], ['line_14', 'line_22']],
# ['Mode_ThreePhaseShortCircuit_MagBrake0', 'Mode_ThreePhaseShortCircuit_MagBrake', ['line_22', 'line_23'], ['line_13']],
# ['Loop2', 'Loop', ['line_13'], ['line_24', 'line_23'], 0, 200]                         #15  
#     ]
#==============================================================================


    


    datalist=[]
 
    flag = -1
    lastBlock =""
    if list[0][1] == "Start":
        tempMode = initMode.Mode_init()
        datalist.append(tempMode)
        Connectionline = list[0][3][0]
        flag = FindNextBlock(list, Connectionline)
        lastBlock = list[1][0]    
        string = list[flag][1]
    
        
    while 1:
        
         
        string = list[flag][1]
   
        if string.find("Mode") != -1:
            if (datalist[-1].CurrentTime == (len(WindspeedList)-1)):
                break
            
            if lastBlock != "Loop":
               resetLoopCounter(list)
            
            print('XXXXXXXXXXXXXXX')
            tempMode = execProcess(string, datalist[-1], WindspeedList, database_dic)
            datalist.append(tempMode)
            lastBlock = string
            Connectionline = list[flag][3][0]
            flag = FindNextBlock(list, Connectionline)
            print('Flag=', flag)

            
            
            
        if string.find("Comparison") != -1:
            if evalComparison(string, list[flag][4], list[flag][5]):
                Connectionline = list[flag][3][0]
                flag = FindNextBlock(list, Connectionline)
            else:
                Connectionline = list[flag][3][1]
                flag = FindNextBlock(list, Connectionline)        
            lastBlock = string    
                #resetLoopCounter(list, string)
                
        if string.find("Check") != -1:
            if evalDecision(string):
                Connectionline = list[flag][3][0]
                flag = FindNextBlock(list, Connectionline)
            else:
                Connectionline = list[flag][3][1]
                flag = FindNextBlock(list, Connectionline)        
            lastBlock = string    
 
                
             
                
        if string.find("Loop") != -1:
            if list[flag][4] == list[flag][5]:
                list[flag][4] = 0
                Connectionline = list[flag][3][0]
                flag = FindNextBlock(list, Connectionline)
            else:  
 
                list[flag][4] += 1
                Connectionline = list[flag][3][1]
                flag = FindNextBlock(list, Connectionline)
                lastBlock = string

        if flag == -1:   
            break
        
        
        return datalist
        
        # 計算所有資料完畢
        #len(Parameter.TimeSeries)-1)
    
    
    
def Comparisongreaterorequal(LastMode, variable, value, Operator):
    if variable == 'WindSpeed':
        Authenticity = LastMode.WindSpeed >= value
    if variable == 'RPM':
        Authenticity = LastMode.RPM >= value
    if variable == 'Power':
        Authenticity = LastMode.power >= value
    return Authenticity

def Comparisongreater(variable, value, Operator):
    if variable == 'WindSpeed':
        Authenticity = variable > value
    if variable == 'RPM':
        Authenticity = variable > value
    if variable == 'Power':
        Authenticity = variable > value
    return Authenticity
    

if __name__=='__main__':
    from Databaseformat import*
    
    Number, TimeSeries, WindSpeed = OpenFile.ReadWindSpeepData()
    WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit, eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit = OpenFile.ReadData_ThreePhaseShortCircuit()
    database_ThreePhaseShortCircuit = referencedata(WindSpeed_ThreePhaseShortCircuit, None, eff_g_ThreePhaseShortCircuit, None, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit)
          
    RPMtoEffg_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower = OpenFile.ReadData_MaxPower()
    database_MaxPower = referencedata(None, RPMtoEffg_MaxPower, eff_g_MaxPower, None, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower)
          
    RPM__MaxTorqueCurrent, eff_g_MaxTorqueCurrent, eff_e_MaxTorqueCurrent, Tg_MaxTorqueCurrent, Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent = OpenFile.ReadData_MaxTorqueCurrent()
    database_MaxTorqueCurrent = referencedata(None, RPM__MaxTorqueCurrent, eff_g_MaxTorqueCurrent, None, None, None, Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent)
    
    database_dic = {'ThreePhaseShortCircuit':database_ThreePhaseShortCircuit, 'MaxPower':database_MaxPower, 'MaxTorqueCurrent':database_MaxTorqueCurrent}
    
    
    list_1=[
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
    ['Loop1', 'Loop', ['line_10'], ['line_11', 'line_21'], 0, 8],
    ['Mode_MaxTorqueCurrent_MagBrake0', 'Mode_MaxTorqueCurrent_MagBrake', ['line_2', 'line_11', 'line_14'], ['line_12']],
    ['Check_MaxMagBrake2', 'Check_MaxMagBrake', ['line_12'], ['line_14', 'line_22']],
    ['Mode_ThreePhaseShortCircuit_MagBrake0', 'Mode_ThreePhaseShortCircuit_MagBrake', ['line_22', 'line_23'], ['line_13']],
    ['Loop2', 'Loop', ['line_13'], ['line_24', 'line_23'], 0, 200]                         #15  
        ]
    
    print(len(WindSpeed))
    BlockList = execBlockChart(list_1, WindSpeed, database_dic)
    print(len(BlockList))

#==============================================================================
#     strlist = [str(type(i)) for i in BlockList]
#     print(strlist)
#==============================================================================
