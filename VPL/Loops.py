from Decision import*
class Loop(Decide):
    # self, name = '', lastMode = None, inputLines=[], outputLines=[]
    def __init__(self, name='', lastMode=None, inputLines=[], outputLines=[], comparisonVariable = None,  comparisonValue = None, Operator = None, Times=None):
        
        self.name = name
        
        while True:
            if hasattr(lastMode, 'lastMode'):
                if isinstance(lastMode, Decide):
                        lastMode = eval('lastMode'+'.lastMode')
                else:
                    break
            else:
                print('Nothing to compare !')
                lastMode = None
                break
            
        self.inputLines = inputLines
        
        if len(outputLines) == 2:
            self.endLines = outputLines[0]
            self.continueLines = outputLines[1]
        else:
            self.endLines = None
            self.continueLines = None
            
        self.comparisonVariable = comparisonVariable
        self.comparisonValue = comparisonValue
        self.Operator = Operator
        self.Times = Times
        self.counter = Times

#==============================================================================
#     def checkCounter(self):
#         if self.comparisonVariable != None and self.comparisonValue!= None and self.Operator!= None:
#             TorF = self.getResultValue()
#         else:
#==============================================================================
            
            
    
    def resetCounter(self):
        self.counter = self.Times
    
    def cleanCounter(self):
        self.counter = 0
    
    def decrementCounter(self):
        self.counter = self.counter - 1
    
    def getCounter(self):
        return self.counter
    
    def setlastMode(self, lastMode):
        self.lastMode = lastMode
    
    def getlastMode(self):
        return self.lastMode
    
    
if __name__ == '__main__':
    from ExtremePoint import*
    
    import unittest
    
    class test(unittest.TestCase):
            
        def test_3_getResultLine(self):
            StartPoint = ExtremePointMode(True, None, 'LineX')
            self.assertEqual(StartPoint.currentTime, -1)
            Modeobject = originalMode('Mode', StartPoint, ['LineX', 'LineY'], 'LineC')
            self.assertEqual(Modeobject.currentTime, 0)    
            comparison = Decide('Decide', Modeobject, ['LineA', 'LineB', 'LineC'], ['Line1', 'Line2'], 'currentTime', 100 , '>')
            self.assertIs(comparison.getResultLine(), 'Line2')

            

    unittest.main()       