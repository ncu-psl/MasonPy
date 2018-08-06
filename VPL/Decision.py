from Mode import*

class Decision(originalMode):
    def __init__(self, name = '', lastMode = None, inputLines=[], outputLines=[], comparisonVariable = None,  comparisonValue = None, Operator = None):
        self.name = name
        self.lastMode = lastMode
        self.inputLines = inputLines
        
        if len(outputLines) == 2:
            self.outputTrueLines = outputLines[0]
            self.outputFalseLines = outputLines[1]
        else:
            self.outputTrueLines = None
            self.outputFalseLines = None

        self.comparisonVariable = comparisonVariable
        self.comparisonValue = comparisonValue
        self.Operator = Operator
    
    
    
    def getResult(self):
        if isinstance(self.lastMode, originalMode):
            if isinstance(self.comparisonVariable, str) and isinstance(self.lastMode.getValue(self.comparisonVariable), (int, float)):
                
                if isinstance(self.comparisonValue, (int, float)):
                    if self.Operator in ['>', '>=', '<', '<=', '=']:
                        if self.Operator == '>':
                            TorF = self.lastMode.getValue(self.comparisonVariable) > self.comparisonValue
                        elif self.Operator == '>=':
                            TorF = self.lastMode.getValue(self.comparisonVariable) >= self.comparisonValue 
                        elif self.Operator == '<':
                            TorF = self.lastMode.getValue(self.comparisonVariable) < self.comparisonValue
                        elif self.Operator == '<=':
                            TorF = self.lastMode.getValue(self.comparisonVariable) <= self.comparisonValue
                        else: # self.Operator == '='
                            TorF = self.lastMode.getValue(self.comparisonVariable) == self.comparisonValue
                        
                        if TorF:
                            return self.outputTrueLines
                        else:
                            return self.outputFalseLines         
                    else:
                        print('operator error')
                        msg = 'operator error'
                        return msg
                else:
                    print('comparison Value error!')
                    msg = 'comparison Value error!'
                    return msg
            else:
                print('parameter error!')
                msg = 'parameter error!'
                return msg
        else:
            print('input mode error!')
            msg = 'input mode error!'
            return msg
#            print('expected 2 arguments')

if __name__ == '__main__':
    from ExtremePoint import*
    import unittest
    
    class test(unittest.TestCase):
        
        def test_1_currentTime(self):
            StartPoint = ExtremePointMode(True, None, 'LineX')
            self.assertEqual(StartPoint.currentTime, -1)
            Modeobject = originalMode('Mode', StartPoint, ['LineX', 'LineY'], 'LineC')
            self.assertEqual(Modeobject.currentTime, 0)
        
        def test_2_getResult(self):
            StartPoint = ExtremePointMode(True, None, 'LineX')
            self.assertEqual(StartPoint.currentTime, -1)
            Modeobject = originalMode('Mode', StartPoint, ['LineX', 'LineY'], 'LineC')
            self.assertEqual(Modeobject.currentTime, 0)    
            Comparative = Decision('decision', Modeobject, ['LineA', 'LineB', 'LineC'], ['Line1', 'Line2'], 'currentTime', 1 , '=')
            self.assertIs(Comparative.getResult(), 'Line1')
            
        def test_2_getResult(self):
            StartPoint = ExtremePointMode(True, None, 'LineX')
            self.assertEqual(StartPoint.currentTime, -1)
            Modeobject = originalMode('Mode', StartPoint, ['LineX', 'LineY'], 'LineC')
            self.assertEqual(Modeobject.currentTime, 0)    
            Comparative = Decision('decision', Modeobject, ['LineA', 'LineB', 'LineC'], ['Line1', 'Line2'], 'currentTime', 100 , '>')
            self.assertIs(Comparative.getResult(), 'Line2')
            
       
            
            
            


    unittest.main()   