import sys

class MissingLineException(Exception):
    def __init__(self, InputNum = 0, OutputNum = 0, err='Error: \"連接線錯誤\"\n'):
        InputErrMsg = self.getErrMsg(self.checkErrFlag(InputNum), self.setInputErrMsg())
        OutputErrMsg = self.getErrMsg(self.checkErrFlag(OutputNum), self.setOutputErrMsg())
        self.err = err + InputErrMsg + OutputErrMsg
        if (InputErrMsg + OutputErrMsg) =='':
            self.err = ''
        Exception.__init__(self, self.err)

    def getFinalErrMsg(self):
        return self.err
    
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

   
    
    
class MissingBlockException(Exception):
    def __init__(self, InputList = [], err='Error: \"錯誤端點\"\n'):
        AllBlock = self.getAllBlock(InputList)
        StartErrMsg = self.getErrMsg(self.checkErrFlag(AllBlock, 'Start'), self.setStartErrMsg())
        EndErrMsg = self.getErrMsg(self.checkErrFlag(AllBlock, 'End'), self.setEndErrMsg())
        self.err = err + StartErrMsg + EndErrMsg
        if (StartErrMsg + EndErrMsg) =='':
            self.err = ''
        Exception.__init__(self, self.err)
    
    def getAllBlock(self, InputList):
        tempList = [InputList[i][0] for i in range(len(InputList))]
        AllBlock = []
        for i in range(len(tempList)):
            if tempList[i].find('Start') != -1:
                AllBlock.append('Start')
            if tempList[i].find('End') != -1:
                AllBlock.append('End')
        return AllBlock     
    
    def getFinalErrMsg(self):
        return self.err
    
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
  
def MissingBlockRaise(BlockName, InputList):
    if eval('MissingBlockException' + '(InputNum)'+'.getFinalErrMsg()') != '':
           exec('raise '+ 'MissingBlockException' + '(InputNum)')    
    
    
    

#==============================================================================
# ErrorMsg = [HasStart_ErrMsg, HasEnd_ErrMsg, StartMissingLine_ErrMsg,
#             EndMissingLine_ErrMsg, ProcessMissingLine_ErrMsg, DecisionMissingLine_ErrMsg,
#             LoopMissingLine_ErrMsg, DecisionInput_ErrMsg, LoopInput_ErrMsg,]
#==============================================================================

  

errmsg = ''

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
            self.assertEqual(TestMissingLineRaise('Process', 1, 4), None)
        def test_Process_2_MissingLineRaise(self):
            self.assertEqual(TestMissingLineRaise('Process', 5, 1), None)
        def test_Process_3_MissingLineRaise(self):
            self.assertEqual(TestMissingLineRaise('Process', 3, 3), None)
        # End 輸入線正確 輸出線錯誤
        def test_Process_4_MissingLineRaise(self):
            self.assertEqual(TestMissingLineRaise('Process', 3, 0), 'Error: "連接線錯誤"\nProcess 缺少輸出線\n')
        # End 輸入線錯誤 輸出線正確
        def test_Process_5_MissingLineRaise(self):
            self.assertEqual(TestMissingLineRaise('Process', 0, 3), 'Error: "連接線錯誤"\nProcess 缺少輸入線\n')
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
            self.assertEqual(ExtremePointList.getFinalErrMsg(), 'Error: "錯誤端點"\n缺少 Start\n')
        # 缺少 End    
        def test_ExtremePoint_3_MissingBlockRaise(self):
            list_1=[
                    ['Start', 'ExtremePointMode', [], ['line_0']],
                    ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                    ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_0'],['WindSpeed', 8, '>='], 200],
                    ]
            ExtremePointList = MissingBlockException(list_1)
            self.assertEqual(ExtremePointList.getFinalErrMsg(), 'Error: "錯誤端點"\n缺少 End\n')
        # 缺少 Start 缺少 End    
        def test_ExtremePoint_4_MissingBlockRaise(self):
            list_1=[
                    ['Mode_A', 'Mode_Init', ['line_0'], ['line_1']],
                    ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_0'],['WindSpeed', 8, '>='], 200],
                    ]
            ExtremePointList = MissingBlockException(list_1)
            self.assertEqual(ExtremePointList.getFinalErrMsg(), 'Error: "錯誤端點"\n缺少 Start\n缺少 End\n')
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
            self.assertEqual(ExtremePointList.getFinalErrMsg(), 'Error: "錯誤端點"\nStart 僅能有一個\n缺少 End\n')    
            
    unittest.main()
