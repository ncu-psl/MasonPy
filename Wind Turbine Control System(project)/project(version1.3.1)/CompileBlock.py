import Parameter
import Formula
from numba import jit


def execProcess(string):
    exec("Formula."+string+"()")
    
def evalDecision(string):
    return eval("Formula."+string+"()")


def evalComparison(string, variable, value): 
    return eval("Formula." + string + "(" +'\''+ variable + '\'' + "," + str(value)  + ")")


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
def execBlockChart(list):
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
 
    flag = -1
    lastBlock =""
    if list[0][1] == "Start":
        Connectionline = list[0][3][0]
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
        
                

