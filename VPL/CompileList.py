ModuleandClass = [['ExtremePoint', 'ExtremePointMode'], ['Mode', 'originalMode'], ['Decision', 'Decide']]  # [file.py, class]


for i in ModuleandClass:
    exec('from '+ i[0] + ' import*')

global AllModule
AllModule = [ i[1] for i in ModuleandClass ]



def buildObj(string):
    global AllModule
    
    if string in AllModule:
        buildobject = eval(string+'()')
#        return  obj
    else:
        print('Not found!')
        buildobject = False   
#==============================================================================
#         msg = 'Not found!'
#         return msg
#==============================================================================
    return  buildobject



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


def execBlockChart(list):
    number_Process  = 0
    number_Decision = 0
    number_Loop     = 0
    
    for i in range(len(list)):
        string = list[i][1]
        if string.find("Mode")!= -1:
            number_Process += 1
        if string.find("Check")!= -1:
            number_Decision += 1 
        if string.find("Loop")!= -1:
            number_Loop += 1
    print("Process", number_Process)    
    print("Decision", number_Decision)
    print("Loop", number_Loop)
 
    
#==============================================================================
#     flag = -1
#     if list[0][1] == "Start":
#         Connectionline = list[0][3][0]
#         flag = FindNextBlock(list, Connectionline)
#         lastBlock = list[1][0]    
#         string = list[flag][1]
#     
#         
#     while 1:
#         
#          
#         string = list[flag][1]
#    
#         if string.find("Mode") != -1:
#             if lastBlock != "Loop":
#                resetLoopCounter(list)
#                
#             execProcess(string)
#             lastBlock = string
#             Connectionline = list[flag][3][0]
#             flag = FindNextBlock(list, Connectionline)
# 
# 
#             
#                 
#         elif string.find("Check") != -1:
#             if evalDecision(string):
#                 Connectionline = list[flag][3][0]
#                 flag = FindNextBlock(list, Connectionline)
#             else:
#                 Connectionline = list[flag][3][1]
#                 flag = FindNextBlock(list, Connectionline)        
#             lastBlock = string    
#  
#                 
#              
#                 
#         elif string.find("Loop") != -1:
#             if list[flag][4] == list[flag][5]:
#                 list[flag][4] = 0
#                 Connectionline = list[flag][3][0]
#                 flag = FindNextBlock(list, Connectionline)
#             else:  
#  
#                 list[flag][4] += 1
#                 Connectionline = list[flag][3][1]
#                 flag = FindNextBlock(list, Connectionline)
#                 lastBlock = string
# 
#         else:
#             if flag == -1:   
#                 break
#==============================================================================
            
            
            
if __name__=='__main__':
    
#==============================================================================
#     list=[
#         ['Start0', 'Start', [], ['line_0']],
# ['Mode_ThreePhaseShortCircuit0', 'Mode_ThreePhaseShortCircuit', ['line_0', 'line_16', 'line_17', 'line_19', 'line_24'], ['line_1']],
# ['Check_MaxMagBrake0', 'Check_MaxMagBrake', ['line_1'], ['line_2', 'line_15']],
# ['Check_MaxWindSpeed_ThreePhaseShortCircuit0', 'Check_MaxWindSpeed_ThreePhaseShortCircuit', ['line_15'], ['line_3', 'line_16']],
# ['Loop0', 'Loop', ['line_3'], ['line_4', 'line_17'], 0, 2000],
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
    
     list=[
        ['Start0', 'Start', [], ['line_0']],
['Mode_A', 'testMode', ['line_0', 'line_16',], ['line_1']],
['Check_MaxMagBrake0', 'Check_MaxMagBrake', ['line_1'], ['line_A', 'line_B']],
['End0', 'End', ['line_A', 'line_B'], []],  
    ]
     execBlockChart(list)
     