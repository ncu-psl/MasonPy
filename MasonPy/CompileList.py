import SetModule

AllFile = SetModule.getFile()   
AllDefinedClass = SetModule.getClass()

for i in AllFile:
    exec('from '+ i + ' import*')

global AllModule
AllModule = [ i for i in AllDefinedClass ]
       
# 修正字串 
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


# 移除字串編號
def text_cleanup(text, removestr):
         new =""
         for i in text:
             if i not in removestr:
                 new += i
         return new

   
def buildObj(name, *parameter):
    global AllModule

    par = []
    
    for i in range(len(parameter)):
        par.append(parameter[i])

    if name in AllModule:        
        buildobject = eval(name + getNewstr(par))
#        return  obj
    else:
        print('Not found in the AllDefinedClass!')
        buildobject = False   
#==============================================================================
#         msg = 'Not found!'
#         return msg
#==============================================================================
    return  buildobject



def resetLoopCounter(list):
     for i in range(len(list)):
         name = list[i][1]      #  outputlist
         if name.find('Loop') != -1:
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
        name = list[i][0]
        if name.find('Start')!= -1 or name.find('End')!= -1:
            number_ExtremePoint += 1
        if name.find('Mode')!= -1:
            number_Process += 1
        if name.find('Check')!= -1:
            number_Decision += 1 
        if name.find('Loop')!= -1:
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
        
        # append List
        
        lastBlock = list[flag][0]
        
        flag = FindNextBlock(list, nextline)
        nextBlock, name = list[flag][1], list[flag][0]
 
    
    finalData = []
    Loopdict = {}   

    while 1:
   
        if name.find('Mode') != -1:
            nextline = list[flag][3][0]
          

            
            newObj = buildObj(nextBlock, nextBlock, newObj, newObj.outputLines, nextline)
            
            finalData.append(newObj)
            newObj.do()
            
            
            

            
            lastBlock = list[flag][0]
     
            
            flag = FindNextBlock(list, nextline)
            
          
            
            nextBlock, name = list[flag][1], list[flag][0]
            
           
            
                
        elif name.find('Decision') != -1:
            comparisonVariable,  comparisonValue, Operator = list[flag][4][0], list[flag][4][1], list[flag][4][2]

            nextline = list[flag][3]

            newObj = buildObj(nextBlock, nextBlock, newObj, newObj.outputLines, nextline, comparisonVariable,  comparisonValue, Operator)
         
            nextline = newObj.getResultLine()
            # newObj.setoutputLines(nextline)
            
            # append List
            
            newObj= newObj.lastMode
               
            lastBlock = list[flag][0]
            
            flag = FindNextBlock(list, nextline)
            
            nextBlock, name = list[flag][1], list[flag][0]

             
                
        elif name.find('Loop') != -1:
            comparisonVariable,  comparisonValue, Operator = list[flag][4][0], list[flag][4][1], list[flag][4][2]
            Times = list[flag][5]
            nextline = list[flag][3]
            
            if name.find('braek') != -1:
                name = text_cleanup(name, 'break')
                Loopdict[name].resetCounter()
                
            else:
                if name in Loopdict:
                
                    Loopdict[name].setlastMode(newObj)
                    nextline = Loopdict[name].getResultLine()
                    
                else:
                    newObj = buildObj(nextBlock, nextBlock, newObj, newObj.outputLines, nextline, comparisonVariable,  comparisonValue, Operator, Times)
                    exec(name + '=' + 'newObj')
                    exec('Loopdict'+'[' + '\"' + name + '\"' + ']' + '=' + name)
                    nextline = Loopdict[name].getResultLine()
                    newObj= newObj.lastMode
                    
                    
                    

                      
                    
                
#==============================================================================
#                 if not isinstance(newObj.lastMode, Mode):
#                     print('Error')
#                     break
#==============================================================================

               
                lastBlock = list[flag][0]

                flag = FindNextBlock(list, nextline)
            
                nextBlock, name = list[flag][1], list[flag][0]
                
        
        elif name.find('End') != -1:        
            break
        else:
            if flag == -1:   
                break
            
    return finalData     


            
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
    
#==============================================================================
#      list=[
# ['Start', 'ExtremePointMode', [], ['line_0']],
# ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
# ['Mode_B', 'Mode_ThreePhaseShortCircuit', ['line_1'], ['line_2']],
# ['Loop1', 'Loop', ['line_2'], ['line_A', 'line_1'],['WindSpeed', 8, '>='], 200],
# ['End0', 'ExtremePointMode', ['line_A'], []],
#     ]
#==============================================================================

     list1=[
['Start', 'ExtremePointMode', [], ['line_0']],
['Loop1', 'Loop', ['line_1'], ['line_A', 'line_2'],[None, None, None], 5],
['Mode_A', 'testMode', ['line_0', 'line_2'], ['line_1']],
['End0', 'ExtremePointMode', ['line_A'], []],
    ]
     list2 = [['Start', 'ExtremePointMode', [], ['line_0']], 
['Mode_Mode_Init1', 'Mode_Init', ['line_0'], ['line_1']], 
['Mode_Mode_ThreePhaseShortCircuit2', 'Mode_ThreePhaseShortCircuit', ['line_1', 'line_8', 'line_9', 'line_24', 'line_38'], ['line_2']], 
['Mode_Mode_ThreePhaseShortCircuit_MagBrake3', 'Mode_ThreePhaseShortCircuit_MagBrake', ['line_34', 'line_39'], ['line_35']], 
['Mode_Mode_MaxPower4', 'Mode_MaxPower', ['line_10', 'line_17'], ['line_11']], 
['Mode_Mode_MaxTorqueCurrent5', 'Mode_MaxTorqueCurrent', ['line_14', 'line_16', 'line_23'], ['line_18']], 
['Mode_Mode_MaxTorqueCurrent6', 'Mode_MaxTorqueCurrent', ['line_5', 'line_21', 'line_29'], ['line_25']], 
['Mode_Mode_MaxTorqueCurrent_MagBrake7', 'Mode_MaxTorqueCurrent_MagBrake', ['line_28', 'line_33'], ['line_30']], 
['Decision_left_data_size0', 'Decide', ['line_2'], ['line_4', 'line_3'], ['left_data_size', 0.0, '>']], 
['End8', 'ExtremePointMode', ['line_3'], []], 
['Decision_RPM1', 'Decide', ['line_4'], ['line_5', 'line_6'], ['RPM', 42.0, '>']], 
['Decision_left_data_size2', 'Decide', ['line_18'], ['line_19', 'line_20'], ['left_data_size', 0.0, '>']], 
['Decision_RPM3', 'Decide', ['line_22'], ['line_23', 'line_24'], ['RPM', 42.0, '>']], 
['Decision_RPM4', 'Decide', ['line_19'], ['line_21', 'line_22'], ['RPM', 400.0, '>=']], 
['Decision_power5', 'Decide', ['line_15'], ['line_16', 'line_17'], ['power', 3300.0, '>=']], 
['Decision_RPM6', 'Decide', ['line_12'], ['line_14', 'line_15'], ['RPM', 400.0, '>=']], 
['Decision_left_data_size7', 'Decide', ['line_11'], ['line_12', 'line_13'], ['left_data_size', 0.0, '>']], 
['Decision_WindSpeed8', 'Decide', ['line_6'], ['line_9', 'line_7'], ['WindSpeed', 8.0, '>']], 
['Loop0', 'Loop', ['line_37'], ['line_38', 'line_39'], [None, None, None], 2000], 
['Loop1', 'Loop', ['line_27'], ['line_28', 'line_29'], [None, None, None], 8], 
['Loop2', 'Loop', ['line_7'], ['line_10', 'line_8'], [None, None, None], 200], 
['End9', 'ExtremePointMode', ['line_13'], []], 
['End10', 'ExtremePointMode', ['line_20'], []], 
['Decision_left_data_size9', 'Decide', ['line_25'], ['line_27', 'line_26'], ['left_data_size', 0.0, '>']], 
['End11', 'ExtremePointMode', ['line_26'], []], 
['Decision_left_data_size10', 'Decide', ['line_30'], ['line_32', 'line_31'], ['left_data_size', 0.0, '>']], 
['End12', 'ExtremePointMode', ['line_31'], []], 
['Decision_RPM11', 'Decide', ['line_32'], ['line_33', 'line_34'], ['RPM', 42.0, '>']], 
['End13', 'ExtremePointMode', ['line_36'], []], 
['Decision_left_data_size12', 'Decide', ['line_35'], ['line_37', 'line_36'], ['left_data_size', 0.0, '>']]]
     print(len(execBlockChart(list2)))
#==============================================================================
#     newObj1 = buildObj('ExtremePointMode', True, [], 'line_0')
#     print(type(newObj1))
#     newObj2 = buildObj('Mode_Init', 'Mode_Init', newObj1, 'line_0', 'line_1')
#     print(type(newObj2))
#     newObj3 = buildObj('Mode_ThreePhaseShortCircuit', 'Mode_ThreePhaseShortCircuit', newObj2, 'line_1', 'line_2')
#     print(type(newObj3))
#==============================================================================
    