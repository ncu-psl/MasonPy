import ExtremePoint 
import Mode 
import Decision

#==============================================================================
# def checkModule(string):
#     AllModule = ['ExtremePoint', 'Mode', 'Decision']
#     value = False
#     ModuleName = ''
#     for i in AllModule:    
#         if  type(eval(string)) == type(eval(i)):
#             print(dir(eval(i)))
#             value = True
#             ModuleName = i
#     return  value, ModuleName
# 
# value, ModuleName = checkModule('originalMode')
# print(checkModule('originalMode'))
#==============================================================================

string = 'originalMode'
print(type(eval('originalMode')))

AllModule = ['ExtremePoint', 'Mode', 'Decision']

for i in AllModule:
    print( hasattr( eval(i)originalMode(), str(string))