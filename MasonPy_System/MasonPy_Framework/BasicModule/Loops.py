from BasicModule.Decision import*
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
        self.lastMode = lastMode    
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
    
    def getResultLine(self):
        HasDecision = (self.comparisonVariable != None and self.comparisonValue!= None and self.Operator!= None)
        HasCounter  = (self.counter != None)
        if HasCounter:
            if self.counter <= 0:   
                self.resetCounter()       
        
        if HasDecision:
            if HasCounter:
                if not self.getResultValue():
                    TorF = (not self.getResultValue()) and self.counter != 1
                    self.decrementCounter()
                else:
                    TorF = False  
            else:    
                TorF = not self.getResultValue()
                print('self.getResultValue()',self.getResultValue())
        else:
            if HasCounter:
                TorF = (self.counter != 1)
                self.decrementCounter()
            else:    
                print('Lack of conditions or counter')
                TorF = False
    
        
        if TorF:
            return self.continueLines
        else:
            return self.endLines    
        
        
        
        
    
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
            
        def test_1_getResultLine(self):
            StartPoint = ExtremePointMode(True, None, 'LineX')
            self.assertEqual(StartPoint.currentTime, -1)
            Modeobject = originalMode('Mode', StartPoint, ['LineX',], 'LineY')
            #self.assertEqual(Modeobject.currentTime, 0)  
            Loop5times = Loop('loop5times', Modeobject, ['LineY'], ['LineX', 'Line1'], 'currentTime', 3 , '=', 0)
            # print(Loop5times.getResultLine())
            self.assertIs(Loop5times.getResultLine(), 'LineX')
            

            

    unittest.main()       