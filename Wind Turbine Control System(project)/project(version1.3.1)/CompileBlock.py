import Parameter
import Formula
from numba import jit


def execProcess(str):
    exec("Formula."+str+"()")
    
def evalDecision(str):
    return eval("Formula."+str+"()")



#==============================================================================
# 
# 
# 
# def resetLoopCounter(list, ModeName):
#     Parameter.LastMode = Parameter.PresentMode
#     Parameter.PresentMode = ModeName
#     if Parameter.LastMode != Parameter.PresentMode:
#         for i in range(len(list)):
#             str= list[i][0]
#             if str.find("Loop") != -1:
#                 list[i][4] = 0
#     
# 
# 
# 
# def execBlockChart(list):
#     Process  = 0
#     Decision = 0
#     Loop     = 0
#     for i in range(len(list)):
#         str = list[i][0]
#         if str.find("Mode") != -1:
#             Process += 1
#         if str.find("Check") != -1:
#             Decision += 1 
#         if str.find("Loop") != -1:
#             Loop += 1    
#     print("Process", Process)    
#     print("Decision", Decision)
#     print("Loop", Loop)
#  
#     if list[0][0] =="Start":
#         flag = list[0][1]
#         while 1:
#             str = list[flag][0]
#             #print(str)
#             if str.find("Mode") != -1:
#                 Parameter.listMode.append(str)
#                 Parameter.CurrentTime += 1
#                 resetLoopCounter(list, str)
#                 execProcess(str)
#                 flag = list[flag][1]    
#             if str.find("Check") != -1:
#                 if evalDecision(str):
#                     flag = list[flag][1]
#                 else:
#                     flag = list[flag][2]
#                     
#                     #resetLoopCounter(list, str)
#                  
#                     
#             if str.find("Loop") != -1:
#                 if list[flag][4] == list[flag][3]:
#                     list[flag][4] = 0
#                     flag = list[flag][1]
#                 else:   
#                     list[flag][4] += 1
#                     flag = list[flag][2] 
#                     
#             
#             # 計算所有資料完畢
#             if (Parameter.CurrentTime == (len(Parameter.TimeSeries)-1)):
#                  break
#  
#==============================================================================

#==============================================================================
# [Modename  , functionname,  inputlinelist[] ,outputline[]]
# [Checkname ,, functionname, inputlinelist[] ,outputlinelist[ture,false]]
# [Loopname  ,, functionname, inputlinelist[] ,outputline[]]
#==============================================================================

@jit
def resetLoopCounter(list):
     for i in range(len(list)):
         str = list[i][1]      #  outputlist
         if str.find("Loop") != -1:
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
        str = list[i][1]
        if str.find("Mode")!= -1:
            Process += 1
        if str.find("Check")!= -1:
            Decision += 1 
        if str.find("Loop")!= -1:
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
        str = list[flag][1]
    
        
    while 1:
        
         
        str = list[flag][1]
   
        if str.find("Mode") != -1:
            if (Parameter.CurrentTime == (len(Parameter.TimeSeries)-1)):
             break
         
            Parameter.ModeStack.append(str)
            Parameter.CurrentTime += 1
            
            if lastBlock != "Loop":
               resetLoopCounter(list)
               
            execProcess(str)
            lastBlock = str
            Connectionline = list[flag][3][0]
            flag = FindNextBlock(list, Connectionline)

            
            
            
        if str.find("Check") != -1:
            if evalDecision(str):
                Connectionline = list[flag][3][0]
                flag = FindNextBlock(list, Connectionline)
            else:
                Connectionline = list[flag][3][1]
                flag = FindNextBlock(list, Connectionline)
            lastBlock = str    
                #resetLoopCounter(list, str)
             
                
        if str.find("Loop") != -1:
            if list[flag][4] == list[flag][5]:
                list[flag][4] = 0
                Connectionline = list[flag][3][0]
                flag = FindNextBlock(list, Connectionline)
            else:  
 
                list[flag][4] += 1
                Connectionline = list[flag][3][1]
                flag = FindNextBlock(list, Connectionline)
                lastBlock = str

        
        # 計算所有資料完畢
        #len(Parameter.TimeSeries)-1)
        
                

                