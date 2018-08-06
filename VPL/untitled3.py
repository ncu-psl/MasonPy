import ExtremePoint 
import Mode 
import Decision

def checkModule(string):
    AllModule = ['ExtremePoint.ExtremePointMode', 'Mode.originalMode', 'Decision.']
    value = False
    ModuleName = ''
    for i in AllModule:    
        if  type(eval(string)) == type(eval(i)):
            print(dir(eval(i)))
            value = True
            ModuleName = i
    return  value, ModuleName

value, ModuleName = checkModule('originalMode')
print(checkModule('originalMode'))