import string
#==============================================================================
# import random
# def id_generator(size=6, chars=string.ascii_uppercase):
#     return ''.join(random.choice(chars) for _ in range(size))
#==============================================================================

ModuleandClass = [['ExtremePoint', 'ExtremePointMode'], ['Mode', 'originalMode'], ['Decision', 'Decide'], ['PrintTest', 'testMode']]  # [file.py, class]


for i in ModuleandClass:
    exec('from '+ i[0] + ' import*')

global AllModule
AllModule = [ i[1] for i in ModuleandClass ]

        
def getNewstr(parList):
    newstr =''
    if range(len(parList)) == 0:
        newstr ='()'
    for i in range(len(parList)):
        if i == 0:
            newstr += '('
        
        newstr += 'par'+'[' + str(i) +']'+','
                        
        if i == len(parList)-1:
            newstr += ')'
    return newstr  
        
        
        
        
   
def buildObj(string, *parameter):
    global AllModule

    par = []
    
    for i in range(len(parameter)):
        par.append(parameter[i])

    if string in AllModule:        
        buildobject = eval(string + getNewstr(par))
#        return  obj
    else:
        print('Not found in the ModuleandClass!')
        buildobject = False   
#==============================================================================
#         msg = 'Not found!'
#         return msg
#==============================================================================
    return  buildobject



def resetLoopCounter(list):
     for i in range(len(list)):
         string = list[i][1]      #  outputlist
         if string.find('Loop') != -1:
             list[i][4] = 0   #  current time counter


def FindNextBlock(list, Connectionline):
    index = -1
    for i in range(len(list)):
        if Connectionline in list[i][2]: # intputlist          
            index = i
            break;
    if index == -1:
        print('Error: Some lines are missing!')    
    return index


def execBlockChart(list):
    number_ExtremePoint = 0
    number_Process      = 0
    number_Decision     = 0
    number_Loop         = 0
    
    for i in range(len(list)):
        string = list[i][0]
        if string.find('Start')!= -1 or string.find('End')!= -1:
            number_ExtremePoint += 1
        if string.find('Mode')!= -1:
            number_Process += 1
        if string.find('Check')!= -1:
            number_Decision += 1 
        if string.find('Loop')!= -1:
            number_Loop += 1
    print('number_ExtremePoint', number_ExtremePoint)
    print('Process', number_Process)    
    print('Decision', number_Decision)
    print('Loop', number_Loop)
    print('\n\n\n')
 
    
    flag = 0
    if list[0][0] == 'Start':
        nextline = list[0][3][0]
        
        newObj = buildObj(list[0][1], True, [], nextline)
        
        lastBlock = list[flag][0]
        flag = FindNextBlock(list, nextline)
        nextBlock = list[flag][1]  
        string = list[flag][0]

        print('lastBlock',lastBlock)
        print('flag',flag)
        print('nextBlock',nextBlock)
        print('string',string)
        
        print('\n\n\n\n')
        
    while 1:
   
        if string.find('Mode') != -1:
            if lastBlock != 'Loop':
               resetLoopCounter(list)
               
            nextline = list[flag][3][0]
            newObj = buildObj(nextBlock, nextBlock, newObj, newObj.outputLines, nextline)
            newObj.do()
            
            lastBlock = list[flag][0]
            flag = FindNextBlock(list, nextline)
            nextBlock = list[flag][1]
            string = list[flag][0]
            
            print('lastBlock',lastBlock)
            print('flag',flag)
            print('nextBlock',nextBlock)
            print('string',string)
            print('\n\n\n\n\n')
            

            

            
                
        elif string.find('Check') != -1:
            comparisonVariable,  comparisonValue, Operator = list[flag][4][0], list[flag][4][1], list[flag][4][2]
            
            print(comparisonVariable,  comparisonValue, Operator)
            nextline = list[flag][3]
            print(nextline)
            newObj = buildObj(nextBlock, nextBlock, newObj, newObj.outputLines, nextline, comparisonVariable,  comparisonValue, Operator)
            
            
         
            nextline = newObj.getResultLine()
            newObj.setoutputLines(nextline)
               
            print('getvalue', newObj.getResultLine())
                
                
            lastBlock = list[flag][0]
            flag = FindNextBlock(list, nextline)
            nextBlock = list[flag][1]
            string = list[flag][0]    
            
            
            print('lastBlock',lastBlock)
            print('flag',flag)
            print('nextBlock',nextBlock)
            print('string',string)
             
                
#==============================================================================
#         elif string.find('Loop') != -1:
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
#==============================================================================
        
        elif string.find('End') != -1:        
            break
        else:
            if flag == -1:   
                break


            
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
        ['Start', 'ExtremePointMode', [], ['line_0']],
['Mode_A', 'testMode', ['line_0'], ['line_1']],
['Mode_A', 'testMode', ['line_1'], ['line_2']],
['Mode_A', 'testMode', ['line_2'], ['line_3']],
['Mode_A', 'testMode', ['line_3'], ['line_4']],
['Mode_A', 'testMode', ['line_4'], ['line_5']],
['Check_MaxMagBrake0', 'Decide', ['line_5'], ['line_A', 'line_B'], ['currentTime', 4, '>']],
['End0', 'ExtremePointMode', ['line_A'], []],
['End1', 'ExtremePointMode', ['line_B'], []]
    ]
     execBlockChart(list)
    
    