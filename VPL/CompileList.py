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

     list=[
['Start', 'ExtremePointMode', [], ['line_0']],
['Mode_A', 'testMode', ['line_0', 'line_2'], ['line_1']],
['Loop1', 'Loop', ['line_1'], ['line_A', 'line_2'],[None, None, None], 5],
['End0', 'ExtremePointMode', ['line_A'], []],
    ]

     
     print(len(execBlockChart(list)))
#==============================================================================
#     newObj1 = buildObj('ExtremePointMode', True, [], 'line_0')
#     print(type(newObj1))
#     newObj2 = buildObj('Mode_Init', 'Mode_Init', newObj1, 'line_0', 'line_1')
#     print(type(newObj2))
#     newObj3 = buildObj('Mode_ThreePhaseShortCircuit', 'Mode_ThreePhaseShortCircuit', newObj2, 'line_1', 'line_2')
#     print(type(newObj3))
#==============================================================================
    