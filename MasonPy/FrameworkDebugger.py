import sys
#==============================================================================
# Missing Lines Exception
# Start (輸入線,輸出線) = (0, 1)
# End (輸入線,輸出線) = (n>0, 0)
# Process (輸入線,輸出線)=(n>0, n>0)
# Decision (輸入線,輸出線)=(n>0, 2)
# Loop (輸入線,輸出線)=(n>0, 2)
#==============================================================================
class MissingLineException(Exception):
    def __init__(self, InputNum = 0, OutputNum = 0, err='Error: \"連接線錯誤\"\n'):
        self.ErrFlag = []
        InputErrMsg = self.getErrMsg(self.checkErrFlag(InputNum), self.setInputErrMsg())
        OutputErrMsg = self.getErrMsg(self.checkErrFlag(OutputNum), self.setOutputErrMsg())
        self.err = err + InputErrMsg + OutputErrMsg
        if (InputErrMsg + OutputErrMsg) =='':
            self.err = ''
        Exception.__init__(self, self.err)

    def getFinalErrMsg(self):
        return self.err
    
    def getErrFlag(self):    #  取得錯誤的 blocks 名稱
        return self.ErrFlag
    
    def checkErrFlag(self, LinesNum):
        if LinesNum < 1:
            ErrFlag = 0
        if LinesNum == 1:
            ErrFlag = 1
        if LinesNum > 1:
            ErrFlag = 2     
        return ErrFlag
    
    
    def setInputErrMsg(self):
        ErrMsg = {'0': 'IMsg0', '1': 'IMsg1', '2': 'IMsg2'} # {key, value} = {Numbers of lines, Error Msg}
        return ErrMsg
    
    def setOutputErrMsg(self):
        ErrMsg = {'0': 'OMsg0', '1': 'OMsg1', '2': 'OMsg2'} # {key, value} = {Numbers of lines, Error Msg}
        return ErrMsg   
    
    def getErrMsg(self, ErrFlag, ErrMsgDict):
        err =  ErrMsgDict[str(ErrFlag)]
        if err != '':
            err =  err +'\n'
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
        ErrMsg = {'0': 'Process 缺少輸出線', '1': '', '2': 'Process 僅能一條輸出線'}
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
        ErrMsg = {'0': 'Decision 輸出線必須為兩條,目前不足2條', '1': 'Decision 輸出線必須為兩條,目前不足1條', '2': '', '3': 'Decision 輸出線僅能兩條,目前過多'}
        return ErrMsg

#==============================================================================
# Loop Lines
#==============================================================================
class LoopMissingLineException(DecisionMissingLineException):
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
    if eval(BlockDict[BlockName] + '('+str(InputNum) +','+ str(OutputNum) +')'+'.getFinalErrMsg()') != '':
        exec('raise '+ BlockDict[BlockName] + '('+str(InputNum) +','+ str(OutputNum) +')')
           

   

#==============================================================================
# Missing Blocks Exception
# Start (數量) = (1)
# End (數量) = (n>0)
# Process (數量) = (n>=0)
# Decision (數量) = (n>=0)
# Loop (n>=0)
#==============================================================================    
class MissingBlockException(Exception):
    def __init__(self, InputList = [], err='Error: \"端點錯誤\"\n'):
        ExtremePointList = self.getExtremePointBlock(InputList)
        StartErrMsg = self.getErrMsg(self.checkErrFlag(ExtremePointList, 'Start'), self.setStartErrMsg())
        EndErrMsg = self.getErrMsg(self.checkErrFlag(ExtremePointList, 'End'), self.setEndErrMsg())
        self.err = err + StartErrMsg + EndErrMsg
        if (StartErrMsg + EndErrMsg) =='':
            self.err = ''
        Exception.__init__(self, self.err)
        
    def getFinalErrMsg(self):
        return self.err
    
    def getExtremePointBlock(self, InputList):
        tempList = [InputList[i][0] for i in range(len(InputList))]
        ExtremePointList = []
        for i in range(len(tempList)):
            if tempList[i].find('Start') != -1:
                ExtremePointList.append('Start')
            if tempList[i].find('End') != -1:
                ExtremePointList.append('End')
        return ExtremePointList     
    
    def checkErrFlag(self, InputList, BolckName):
        if InputList.count(BolckName) == 0:
            ErrFlag = 0
        if InputList.count(BolckName) == 1:
            ErrFlag = 1
        if InputList.count(BolckName) > 1:
            ErrFlag = 2     
        return ErrFlag
    
    def setStartErrMsg(self):
        ErrMsg = {'0': '缺少 Start', '1': '', '2': 'Start 僅能有一個'}
        return ErrMsg

    def setEndErrMsg(self):
        ErrMsg = {'0': '缺少 End', '1': '', '2': ''}
        return ErrMsg
    
    def getErrMsg(self, ErrFlag, ErrMsgDict):
        err =  ErrMsgDict[str(ErrFlag)]
        if err != '':
            err =  err +'\n'
        return err
  
def MissingBlockRaise(InputList):
    if eval('MissingBlockException' + '(InputList)'+'.getFinalErrMsg()') != '':
           exec('raise '+ 'MissingBlockException' + '(InputList)')    
    


class DecisionErrorException(Exception):
    def __init__(self, InputList, err='Error: \"Decision參數設定錯誤\"\n'):
        self.ErrFlag = []
        DecisionList = self.getDecisionBlock(InputList)
        ConditionalErrMsg = self.getErrMsg(DecisionList, self.setValueErrMsg())
        self.err = err + ConditionalErrMsg
        if ConditionalErrMsg =='':
            self.err = ''
        Exception.__init__(self, self.err)
    
    def getFinalErrMsg(self):
        return self.err
    
    def getErrFlag(self):    #  取得錯誤的 blocks 名稱
        return self.ErrFlag
    
    def getErrMsg(self, DecisionList, ErrMsgDict):
        ErrFlag = 0
        for i in range(len(DecisionList)):
            if type(DecisionList[i][4][1]) != int and type(DecisionList[i][4][1]) != float:
                ErrFlag = -1
                self.ErrFlag.append(DecisionList[i][0])
        err =  ErrMsgDict[str(ErrFlag)]
        if err != '':
            err =  err +'\n'
        return err    
            
    def getDecisionBlock(self, InputList):
        DecisionList = []
        for i in range(len(InputList)):
            if InputList[i][1].find('Decide') != -1:
                DecisionList.append(InputList[i])
        return DecisionList 

    def setValueErrMsg(self):
        ErrMsg = {'-1':'條件式 比較值錯誤', '0':''}
        return ErrMsg

def DecisionErrorRaise(InputList):
    if eval('DecisionErrorException' + '(InputList)'+'.getFinalErrMsg()') != '':
           exec('raise '+ 'DecisionErrorException' + '(InputList)')
           
           
class LoopErrorException(DecisionErrorException):
    def __init__(self, InputList, err='Error: \"Loop參數設定錯誤\"\n'):
        self.ErrFlag = []
        LoopList = self.getLoopBlock(InputList)
        ErrMsg = self.getErrMsg(LoopList)
        self.err = err + ErrMsg
        if ErrMsg =='':
            self.err = ''
        Exception.__init__(self, self.err)
    
    def getLoopBlock(self, InputList):
        DecisionList = []
        for i in range(len(InputList)):
            if InputList[i][1].find('Loop') != -1:
                DecisionList.append(InputList[i])
        return DecisionList 
    
    def getFinalErrMsg(self):
        return self.err
    
    def getErrFlag(self):    #  取得錯誤的 blocks 名稱
        return self.ErrFlag
    
    def getErrMsg(self, LoopList):
        HasConditional = True 
        HasCounter = True
        
        for i in range(len(LoopList)):
            if type(LoopList[i][4][1]) != int and type(LoopList[i][4][1]) != float and type(LoopList[i][5]) != int:
                HasConditional = False
                HasCounter = False
                self.ErrFlag.append(LoopList[i][0])
        err =  self.getwhichErrMsg(HasConditional, HasCounter)
        if err != '':
            err =  err +'\n'
        return err
    
    def getwhichErrMsg(self, HasConditional, HasCounter):
        ErrMsg = ''
        if HasConditional is False and HasCounter is False:
            ErrMsg = '至少須設定 條件式 或 Counter'
        return ErrMsg    
    
    
    def getParameterErrMsg(self):
        ErrMsg = 'Counter 錯誤'
        return ErrMsg

    def getValueErrMsg(self):
        ErrMsg = '條件式 比較值錯誤'
        return ErrMsg

def LoopErrorRaise(InputList):
    if eval('LoopErrorException' + '(InputList)'+'.getFinalErrMsg()') != '':
           exec('raise '+ 'LoopErrorException' + '(InputList)')    

#==============================================================================
# ErrorMsg = [HasStart_ErrMsg, HasEnd_ErrMsg, StartMissingLine_ErrMsg,
#             EndMissingLine_ErrMsg, ProcessMissingLine_ErrMsg, DecisionMissingLine_ErrMsg,
#             LoopMissingLine_ErrMsg, DecisionInput_ErrMsg, LoopInput_ErrMsg,]
#==============================================================================


def TestMissingLineRaise(BlockName, x, y):
    MissingLinemsg = None
    try:
        MissingLineRaise(BlockName, x, y)
    except MissingLineException as e:
        MissingLinemsg = str(sys.exc_info()[1])
#==============================================================================
#     print('###################')    
#     print(MissingLinemsg)
#==============================================================================
    return MissingLinemsg


def TestErrorRaise(InputList):
    ALLErrMsg = ''
    
    # 檢查是否缺端點
    try:
        MissingBlockRaise(InputList)
    except MissingBlockException as e:
        MissingBlockmsg = str(sys.exc_info()[1])
        ALLErrMsg = ALLErrMsg + '\n' + MissingBlockmsg 
    
    # 檢查線是否連接正確
    for i in range(len(InputList)):
        if InputList[i][0].find('Start') != -1:
            BlockName = 'Start'
        if InputList[i][0].find('End') != -1:
            BlockName = 'End'             
        if InputList[i][0].find('Mode') != -1:
            BlockName = 'Process'
        if InputList[i][0].find('Decision') != -1:
            BlockName = 'Decision'
        if InputList[i][0].find('Loop') != -1:
            BlockName = 'Loop'
        InputNum, OutputNum = len(InputList[i][2]), len(InputList[i][3])             
  
        try:
            MissingLineRaise(BlockName, InputNum, OutputNum)
        except MissingLineException as e:
            MissingLinemsg = str(sys.exc_info()[1])
            ALLErrMsg = ALLErrMsg + '\n' + MissingLinemsg
       
    
    # 檢查線Decision是否設定正確              
    try:
        DecisionErrorRaise(InputList)
    except DecisionErrorException as e:
        DecisionErrormsg = str(sys.exc_info()[1])
        ALLErrMsg = ALLErrMsg + '\n' + DecisionErrormsg
        
    # 檢查線Loop是否設定正確              
    try:
        LoopErrorRaise(InputList)
    except LoopErrorException as e:
        LoopErrormsg = str(sys.exc_info()[1])
        ALLErrMsg = ALLErrMsg + '\n' + LoopErrormsg    

    return ALLErrMsg


if __name__ =='__main__':

    import unittest    
    class test(unittest.TestCase): 

         # Start (輸入線,輸出線)=(0, 1)
         # Start 輸入線正確 輸出線正確
         def test_Start_1_MissingLineRaise(self):
             self.assertIs(TestMissingLineRaise('Start', 0, 1), None)
         # Start 輸入線正確 輸出線錯誤(缺少)
         def test_Start_2_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Start', 0, 0), 'Error: "連接線錯誤"\nStart 缺少輸出線\n')
         # Start 輸入線錯誤(不得有輸入線) 輸出線錯誤(缺少)
         def test_Start_3_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Start', 2, 0), 'Error: "連接線錯誤"\nStart 不得有輸入線\nStart 缺少輸出線\n')
         # Start 輸入線錯誤(不得有輸入線) 輸出線錯誤(過多)
         def test_Start_4_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Start', 3, 3), 'Error: "連接線錯誤"\nStart 不得有輸入線\nStart 僅能一條輸出線\n')
         # Start 輸入線正確 輸出線錯誤(缺少)
         def test_Start_5_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Start', 0, 0), 'Error: "連接線錯誤"\nStart 缺少輸出線\n')
         # Start 輸入線正確 輸出線錯誤(過多)
         def test_Start_6_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Start', 0, 2), 'Error: "連接線錯誤"\nStart 僅能一條輸出線\n')
             
             
         # End (輸入線,輸出線)=(n>0, 0)
         # End 輸入線正確 輸出線正確
         def test_End_1_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('End', 1, 0), None)
         def test_End_2_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('End', 5, 0), None)    
         
         # End 輸入線正確 輸出線錯誤
         def test_End_3_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('End', 1, 1), 'Error: "連接線錯誤"\nEnd 不得有輸出線\n')
         def test_End_4_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('End', 5, 5), 'Error: "連接線錯誤"\nEnd 不得有輸出線\n')    
         # End 輸入線錯誤(缺少) 輸出線正確
         def test_End_5_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('End', 0, 0), 'Error: "連接線錯誤"\nEnd 缺少輸入線\n')
         # End 輸入線錯誤(缺少) 輸出線錯誤
         def test_End_6_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('End', 0, 1), 'Error: "連接線錯誤"\nEnd 缺少輸入線\nEnd 不得有輸出線\n')
         def test_End_7_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('End', 0, 5), 'Error: "連接線錯誤"\nEnd 缺少輸入線\nEnd 不得有輸出線\n')   
         
         # Process (輸入線,輸出線)=(n>0, n>0)
         def test_Process_1_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Process', 1, 4), 'Error: "連接線錯誤"\nProcess 僅能一條輸出線\n')
         def test_Process_2_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Process', 5, 1), None)
         def test_Process_3_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Process', 3, 3), 'Error: "連接線錯誤"\nProcess 僅能一條輸出線\n')
         # End 輸入線正確 輸出線錯誤
         def test_Process_4_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Process', 3, 0), 'Error: "連接線錯誤"\nProcess 缺少輸出線\n')
         # End 輸入線錯誤 輸出線正確
         def test_Process_5_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Process', 0, 3), 'Error: "連接線錯誤"\nProcess 缺少輸入線\nProcess 僅能一條輸出線\n')
         # End 輸入線錯誤 輸出線錯誤
         def test_Process_6_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Process', 0, 0), 'Error: "連接線錯誤"\nProcess 缺少輸入線\nProcess 缺少輸出線\n')    
         
         # Decision (輸入線,輸出線)=(n>0, 2)
         def test_Decision_1_MissingLineRaise(self):
             self.assertIs(TestMissingLineRaise('Decision', 1, 2), None)
         def test_Decision_2_MissingLineRaise(self):
             self.assertIs(TestMissingLineRaise('Decision', 5, 2), None)
         # Decision 輸入線正確 輸出線錯誤(缺少)
         def test_Decision_3_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Decision', 1, 0), 'Error: "連接線錯誤"\nDecision 輸出線必須為兩條,目前不足2條\n')
         def test_Decision_4_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Decision', 1, 1), 'Error: "連接線錯誤"\nDecision 輸出線必須為兩條,目前不足1條\n')
         # Decision 輸入線正確 輸出線錯誤(過多)
         def test_Decision_5_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Decision', 1, 3), 'Error: "連接線錯誤"\nDecision 輸出線僅能兩條,目前過多\n')
             def test_Decision_6_MissingLineRaise(self):
                 self.assertEqual(TestMissingLineRaise('Decision', 1, 5), 'Error: "連接線錯誤"\nDecision 輸出線僅能兩條,目前過多\n')    
         # Decision 輸入線錯誤 輸出線正確
         def test_Decision_7_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Decision', 0, 2), 'Error: "連接線錯誤"\nDecision 缺少輸入線\n')
         # Decision 輸入線錯誤 輸出線錯誤
         def test_Decision_8_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Decision', 0, 0), 'Error: "連接線錯誤"\nDecision 缺少輸入線\nDecision 輸出線必須為兩條,目前不足2條\n')
         def test_Decision_9_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Decision', 0, 1), 'Error: "連接線錯誤"\nDecision 缺少輸入線\nDecision 輸出線必須為兩條,目前不足1條\n')
         def test_Decision_10_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Decision', 0, 10), 'Error: "連接線錯誤"\nDecision 缺少輸入線\nDecision 輸出線僅能兩條,目前過多\n')
         
         # Loop (輸入線,輸出線)=(n>0, 2)
         def test_Loop_1_MissingLineRaise(self):
             self.assertIs(TestMissingLineRaise('Loop', 1, 2), None)
         def test_Loop_2_MissingLineRaise(self):
             self.assertIs(TestMissingLineRaise('Loop', 5, 2), None)
         # Loop 輸入線正確 輸出線錯誤(缺少)
         def test_Loop_3_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Loop', 1, 0), 'Error: "連接線錯誤"\nLoop 輸出線必須為兩條,目前不足2條\n')
         def test_Loop_4_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Loop', 1, 1), 'Error: "連接線錯誤"\nLoop 輸出線必須為兩條,目前不足1條\n')
         # Loop 輸入線正確 輸出線錯誤(過多)
         def test_Loop_5_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Loop', 1, 3), 'Error: "連接線錯誤"\nLoop 輸出線僅能兩條,目前過多\n')
         def test_Loop_6_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Loop', 1, 5), 'Error: "連接線錯誤"\nLoop 輸出線僅能兩條,目前過多\n')    
         # Loop 輸入線錯誤 輸出線正確
         def test_Loop_7_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Loop', 0, 2), 'Error: "連接線錯誤"\nLoop 缺少輸入線\n')
         # Loop 輸入線錯誤 輸出線錯誤
         def test_Loop_8_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Loop', 0, 0), 'Error: "連接線錯誤"\nLoop 缺少輸入線\nLoop 輸出線必須為兩條,目前不足2條\n')
         def test_Loop_9_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Loop', 0, 1), 'Error: "連接線錯誤"\nLoop 缺少輸入線\nLoop 輸出線必須為兩條,目前不足1條\n')
         def test_Loop_10_MissingLineRaise(self):
             self.assertEqual(TestMissingLineRaise('Loop', 0, 10), 'Error: "連接線錯誤"\nLoop 缺少輸入線\nLoop 輸出線僅能兩條,目前過多\n')
         
         # Missing Blocks
         # ExtremePoint
         def test_ExtremePoint_1_MissingBlockRaise(self):
             list_1=[
                     ['Start', 'ExtremePointMode', [], ['line_0']],
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_0'],['WindSpeed', 8, '>='], 200],
                     ['End0', 'ExtremePointMode', ['line_A'], []],
                     ]
             ExtremePointList = MissingBlockException(list_1)
             self.assertEqual(ExtremePointList.getFinalErrMsg(), '')
         # 缺少 Start
         def test_ExtremePoint_2_MissingBlockRaise(self):
             list_1=[
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_0'],['WindSpeed', 8, '>='], 200],
                     ['End0', 'ExtremePointMode', ['line_A'], []],
                     ]
             ExtremePointList = MissingBlockException(list_1)
             self.assertEqual(ExtremePointList.getFinalErrMsg(), 'Error: "端點錯誤"\n缺少 Start\n')
         # 缺少 End    
         def test_ExtremePoint_3_MissingBlockRaise(self):
             list_1=[
                     ['Start', 'ExtremePointMode', [], ['line_0']],
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_0'],['WindSpeed', 8, '>='], 200],                    
                     ]
             ExtremePointList = MissingBlockException(list_1)
             self.assertEqual(ExtremePointList.getFinalErrMsg(), 'Error: "端點錯誤"\n缺少 End\n')
         # 缺少 Start 缺少 End    
         def test_ExtremePoint_4_MissingBlockRaise(self):
             list_1=[
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_0'],['WindSpeed', 8, '>='], 200],
                     ]
             ExtremePointList = MissingBlockException(list_1)
             self.assertEqual(ExtremePointList.getFinalErrMsg(), 'Error: "端點錯誤"\n缺少 Start\n缺少 End\n')
         # 過多 Start 缺少 End
         def test_ExtremePoint_5_MissingBlockRaise(self):
             list_1=[
                     ['Start', 'ExtremePointMode', [], ['line_2']],
                     ['Start', 'ExtremePointMode', [], ['line_0']],
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ['Loop1', 'Loop', ['line_1', 'line_2'], ['line_A', 'line_0'],['WindSpeed', 8, '>='], 200],
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ]
             ExtremePointList = MissingBlockException(list_1)
             self.assertEqual(ExtremePointList.getFinalErrMsg(), 'Error: "端點錯誤"\nStart 僅能有一個\n缺少 End\n')
             
         # Decision Error
         # Decision輸入參數正確
         def test_ExtremePoint_1_DecisionErrorRaise(self):
             list_1=[
                     ['Start', 'ExtremePointMode', [], ['line_0']],
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ['Decision1', 'Decide', ['line_1'], ['line_A', 'line_0'],['WindSpeed', 8, '>=']],
                     ['End0', 'ExtremePointMode', ['line_A', 'line_0'], []],
                     ]
             DecisionList = DecisionErrorException(list_1)
             self.assertEqual(DecisionList.getFinalErrMsg(), '')
         # Decision Error
         # 無 Decision 但輸入參數正確
         def test_ExtremePoint_2_DecisionErrorRaise(self):
             list_1=[
                     ['Start', 'ExtremePointMode', [], ['line_0']],
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ['Loop1', 'Loop', ['line_1', 'line_2'], ['line_A', 'line_0'],['WindSpeed', 8, '>='], 200],
                     ['End0', 'ExtremePointMode', ['line_A', 'line_0'], []],
                     ]
             DecisionList = DecisionErrorException(list_1)
             self.assertEqual(DecisionList.getFinalErrMsg(), '')    
         # 輸入參數錯誤
         def test_ExtremePoint_3_DecisionErrorRaise(self):
             list_1=[
                     ['Start', 'ExtremePointMode', [], ['line_0']],
                     ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                     ['Decision1', 'Decide', ['line_1'], ['line_A', 'line_0'],['WindSpeed', 'ABC', '>=']],
                     ['End0', 'ExtremePointMode', ['line_A'], []],
                     ]
             DecisionList = DecisionErrorException(list_1)             
             self.assertEqual(DecisionList.getFinalErrMsg(), 'Error: \"Decision參數設定錯誤\"\n條件式 比較值錯誤\n')

         # Loop Error
         # 錯誤: 無終止條件或計數器
         def test_1_LoopErrorRaise(self):
             list_1=[
                    ['Start', 'ExtremePointMode', [], ['line_0']],
                    ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                    ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_2'],[None, None, None], None],
                    ['End0', 'ExtremePointMode', ['line_A'], []],
                    ]
             LoopList = LoopErrorException(list_1)
             self.assertEqual(LoopList.getFinalErrMsg(), 'Error: "Loop參數設定錯誤"\n至少須設定 條件式 或 Counter\n')
         # 輸入正確    
         def test_2_LoopErrorRaise(self):
             list_1=[
                    ['Start', 'ExtremePointMode', [], ['line_0']],
                    ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                    ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_2'],[None, None, None], 5],
                    ['End0', 'ExtremePointMode', ['line_A'], []],
                    ]
             LoopList = LoopErrorException(list_1)
             self.assertEqual(LoopList.getFinalErrMsg(), '')    
            
    unittest.main()
    
#==============================================================================
#     list_1=[['Start', 'ExtremePointMode', [], ['line_0']],
# ['Loop1', 'Loop', ['line_1'], ['line_2', 'line_3'],[None, None, None], 10],
# ['Mode_A', 'testMode', ['line_0', 'line_3'], ['line_1']],
# ['End1', 'ExtremePointMode', ['line_2'], []],
#     ]
#==============================================================================
#==============================================================================
#     list_2=[['Start', 'ExtremePointMode', [], ['line_0']],
# ['Mode_A', 'testMode', ['line_1',], []],
# ['End1', 'ExtremePointMode', [], []],
#     ]
#==============================================================================
#==============================================================================
#     list_3=[
# 
#  ['Mode_A', 'testMode', [], ['line_1']],
#  ['Loop5', 'Loop', ['line_1'], ['line_A', 'line_B','line_C'],['A', 8, '<'], 5],
#  ['End0', 'ExtremePointMode', ['line_A'], []],
#  ['End1', 'ExtremePointMode', ['line_B'], []],
#  ['End2', 'ExtremePointMode', ['line_C'], []],
#      ]
#     Msg = TestErrorRaise(list_3)
#     print(Msg)
#==============================================================================

