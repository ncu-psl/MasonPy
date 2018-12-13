import sys

class MissingLineException(Exception):
    def __init__(self, InputNum = 0, OutputNum = 0, err='Error: \"連接線錯誤\" \n'):
        InputErrMsg = self.getErrMsg(self.checkErrFlag(InputNum), self.setInputErrMsg())
        OutputErrMsg = self.getErrMsg(self.checkErrFlag(OutputNum), self.setOutputErrMsg())
        self.err = err + InputErrMsg + OutputErrMsg
        Exception.__init__(self, self.err)

    def checkErrFlag(self, LinesNum):
        if LinesNum < 1:
            ErrFlag = 0
        if LinesNum == 1:
            ErrFlag = 1
        if LinesNum > 1:
            ErrFlag = 2     
        return ErrFlag
    
    def setInputErrMsg(self):
        ErrMsg = {'0': 'IMsg0', '1': 'IMsg1', '2': 'IMsg2'}
        return ErrMsg
    
    def setOutputErrMsg(self):
        ErrMsg = {'0': 'OMsg0', '1': 'OMsg1', '2': 'OMsg2'}
        return ErrMsg   
    
    def getErrMsg(self, ErrFlag, ErrMsgDict):
        err =  ErrMsgDict[str(ErrFlag)] +'\n'
        return err


#==============================================================================
# Start Lines
#==============================================================================
class StartMissingLineException(MissingLineException):
    def setInputErrMsg(self):
        ErrMsg = {'0': '', '1': 'Start 不得有輸入線', '2': 'Start 不得有輸入線'}
        return ErrMsg
    
    def setOutputErrMsg(self):
        ErrMsg = {'0': 'Start 缺少輸出線', '1': '', '2': 'Start 僅能一條輸出線'}
        return ErrMsg
    

#==============================================================================
# End Lines
#==============================================================================
class EndMissingLineException(MissingLineException):
    def setInputErrMsg(self):
        ErrMsg = {'0': 'End 缺少輸入線', '1': '', '2': ''}
        return ErrMsg
    
    def setOutputErrMsg(self):
        ErrMsg = {'0': '', '1': 'End 不得有輸出線', '2': 'End 不得有輸出線'}
        return ErrMsg


#==============================================================================
# Process Lines
#==============================================================================
class ProcessMissingLineException(MissingLineException):
    def setInputErrMsg(self):
        ErrMsg = {'0': 'Process 缺少輸入線', '1': '', '2': ''}
        return ErrMsg
    
    def setOutputErrMsg(self):
        ErrMsg = {'0': 'Process 缺少輸出線', '1': '', '2': ''}
        return ErrMsg


#==============================================================================
# Decision Lines
#==============================================================================
class DecisionMissingLineException(MissingLineException):
    def checkErrFlag(self, LinesNum):
        if LinesNum < 1:
            ErrFlag = 0
        if LinesNum == 1:
            ErrFlag = 1
        if LinesNum > 1:
            ErrFlag = 2
        if LinesNum > 2:
            ErrFlag = 3    
        return ErrFlag    

    def setInputErrMsg(self):
        ErrMsg = {'0': 'Decision 缺少輸入線', '1': '', '2': '',  '3': ''}
        return ErrMsg
    
    def setOutputErrMsg(self):
        ErrMsg = {'0': 'DecisionDecision 輸出線必須為兩條,目前不足2條', '1': 'Decision 輸出線必須為兩條,目前不足1條', '2': '', '3': 'Decision 輸出線僅能兩條,目前過多'}
        return ErrMsg


#==============================================================================
# Loop Lines
#==============================================================================
class LoopMissingLineException(MissingLineException):
    def setInputErrMsg(self):
        ErrMsg = {'0': 'Loop 缺少輸入線', '1': '', '2': '',  '3': ''}
        return ErrMsg
    
    def setOutputErrMsg(self):
        ErrMsg = {'0': 'Loop 輸出線必須為兩條,目前不足2條', '1': 'Loop 輸出線必須為兩條,目前不足1條', '2': '', '3': 'Loop 輸出線僅能兩條,目前過多'}
        return ErrMsg  
   
    
#==============================================================================
# raise MissingLineException
#==============================================================================
def MissingLineRaise(BlockName, InputNum, OutputNum):
    BlockDict = {'Start':'StartMissingLineException', 'End':'EndMissingLineException', 
    'Process':'ProcessMissingLineException', 'Decision':'DecisionMissingLineException', 'Loop':'LoopMissingLineException'}    
    print('raise '+ BlockDict[BlockName] + '('+str(InputNum) +','+ str(OutputNum) +')')
    exec('raise '+ BlockDict[BlockName] + '('+str(InputNum) +','+ str(OutputNum) +')')

   
    
    
    
    

#==============================================================================
# ErrorMsg = [HasStart_ErrMsg, HasEnd_ErrMsg, StartMissingLine_ErrMsg,
#             EndMissingLine_ErrMsg, ProcessMissingLine_ErrMsg, DecisionMissingLine_ErrMsg,
#             LoopMissingLine_ErrMsg, DecisionInput_ErrMsg, LoopInput_ErrMsg,]
#==============================================================================

  

errmsg = ''
while 1:
    try:
        x = int(input('輸入x:'))
        y = int(input('輸入y:'))
        print(x, y)
        MissingLineRaise('End', x, y)
#==============================================================================
#         if x is False or y is False :
#             MissingLineRaise(x, y)
#==============================================================================
            
        
    except MissingLineException as e:
        MissingLinemsg = str(sys.exc_info()[1])+'\n'
        print(e) 
    print('###################')    
    print(MissingLinemsg)
    
#==============================================================================
# if __name__ =='__main__':
# 
#     import unittest    
#     class test(unittest.TestCase):
#         
#         def test_1_currentTime(self):
#             try:
#                 StartMissingMissingLineRaise(x, y)       
#             except MissingLineException as e:
#==============================================================================
                