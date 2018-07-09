from numba import jit
import OpenFile
import Block

import initMode
import ThreePhaseShortCircuit
import ThreePhaseShortCircuit_MagBrake
import MaxPower
import MaxTorqueCurrent
import MaxTorqueCurrent_MagBrake
        
        
        

def execProcess(string):
    exec("Formula."+string+"()")
    
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
def execBlockChart(list, WindspeedList, number):
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

    BlockList = []
    for i in range(len(list)):
        string = list[i][1]
        if string.find("Start")!= -1:
            tempMode  = initMode.Mode_init()
            tempBlock = Block.block(tempMode, list[i][2], list[i][3])
            BlockList.append(tempBlock)
        if string.find("Mode")!= -1:
            ModeName = list[i][1]
            if ModeName == 'Mode_ThreePhaseShortCircuit':
                tempMode  = ThreePhaseShortCircuit.Mode_ThreePhaseShortCircuit()
                tempBlock = Block.block(tempMode, list[i][2], list[i][3])
                BlockList.append(tempBlock)
            if ModeName == 'Mode_ThreePhaseShortCircuit_MagBrake':
                tempMode  = ThreePhaseShortCircuit_MagBrake.Mode_ThreePhaseShortCircuit_MagBrake()
                tempBlock = Block.block(tempMode, list[i][2], list[i][3]) 
                BlockList.append(tempBlock)
            if ModeName == 'Mode_MaxPower':
                tempMode = MaxPower.Mode_MaxPower()
                tempBlock = Block.block(tempMode, list[i][2], list[i][3])
                BlockList.append(tempBlock)
            if ModeName == 'Mode_MaxTorqueCurrent':
                tempMode = MaxTorqueCurrent.Mode_MaxTorqueCurrent()
                tempBlock = Block.block(tempMode, list[i][2], list[i][3])
                BlockList.append(tempBlock)
            if ModeName == 'Mode_MaxTorqueCurrent_MagBrake':
                tempMode  = MaxTorqueCurrent_MagBrake.Mode_MaxTorqueCurrent_MagBrake()
                tempBlock = Block.block(tempMode, list[i][2], list[i][3])
                BlockList.append(tempBlock)
        if string.find("Check")!= -1:
            tempBlock = Block.block(, list[i][2], list[i][3])
        if string.find("Loop")!= -1:
            tempBlock = Block.block(None, list[i][2], list[i][3])
    



 
    flag = -1
    lastBlock =""
    if list[0][1] == "Start":
        tempMode  = initMode.Mode_init(None, None, 0)
        tempBlock = Block.block(tempMode, list[0][2], list[0][3])
        flag = FindNextBlock(list, Connectionline)
        lastBlock = list[1][0]    
        string = list[flag][1]
    
        
    while 1:
        
         
        string = list[flag][1]
   
        if string.find("Mode") != -1:
            if (Parameter.CurrentTime == (len(Parameter.TimeSeries)-1)):
                break
         
            Parameter.ModeStack.append(string)
            Parameter.CurrentTime += 1
            
            if lastBlock != "Loop":
               resetLoopCounter(list)
               
            execProcess(string)
            lastBlock = string
            Connectionline = list[flag][3][0]
            flag = FindNextBlock(list, Connectionline)


            
            
            
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
        
        # 計算所有資料完畢
        #len(Parameter.TimeSeries)-1)