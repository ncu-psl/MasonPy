import Parameter
import Formula



def execProcess(str):
    exec("Formula."+str+"()")
    
def evalDecision(str):
    return eval("Formula."+str+"()")

def resetLoopCounter(list, ModeName):
    Parameter.LastMode = Parameter.PresentMode
    Parameter.PresentMode = ModeName
    if Parameter.LastMode != Parameter.PresentMode:
        for i in range(len(list)):
            str= list[i][0]
            if str.find("Loop") != -1:
                list[i][4] = 0
    



def execBlockChart(list):
    Process  = 0
    Decision = 0
    Loop     = 0
    for i in range(len(list)):
        str = list[i][0]
        if str.find("Mode") != -1:
            Process += 1
        if str.find("Check") != -1:
            Decision += 1 
        if str.find("Loop") != -1:
            Loop += 1    
    print("Process", Process)    
    print("Decision", Decision)
    print("Loop", Loop)
 
    if list[0][0] =="Start":
        flag = list[0][1]
        while 1:
            str = list[flag][0]
            #print(str)
            if str.find("Mode") != -1:
                Parameter.listMode.append(str)
                Parameter.CurrentTime += 1
                resetLoopCounter(list, str)
                execProcess(str)
                flag = list[flag][1]    
            if str.find("Check") != -1:
                if evalDecision(str):
                    flag = list[flag][1]
                else:
                    flag = list[flag][2]
            if str.find("Loop") != -1:
                if list[flag][4] == list[flag][3]:
                    list[flag][4] = 0
                    flag = list[flag][1]
                else:   
                    list[flag][4] += 1
                    flag = list[flag][2]      
            if (Parameter.CurrentTime == (len(Parameter.TimeSeries)-1)):
                 break
             
                