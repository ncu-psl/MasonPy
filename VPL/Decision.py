from Mode import*

class Decide(originalMode):
    def __init__(self, name = '', lastMode = None, inputLines=[], outputLines=[], comparisonVariable = None,  comparisonValue = None, Operator = None):
        self.name = name
        
        
        while True:
            if hasattr(lastMode, 'lastMode'):
                if isinstance(lastMode, Decide):
                        lastMode = eval('lastMode'+'.lastMode')
                else:
                    lastMode = lastMode
                    break
            else:
                print('Nothing to compare !')
                lastMode = None
                break
            
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
                        return False
#==============================================================================
#                         msg = 'operator error'
#                         return msg
#==============================================================================
                else:
                    print('comparison Value error!')
                    return False
#==============================================================================
#                     msg = 'comparison Value error!'
#                     return msg
#==============================================================================
            else:
                print('parameter error!')
                return False
#==============================================================================
#                 msg = 'parameter error!'
#                 return msg
#==============================================================================
        else:
            print('input mode error!')
            return False
#==============================================================================
#             msg = 'input mode error!'
#             return msg
#==============================================================================
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
            comparison = Decide('Decide', Modeobject, ['LineA', 'LineB', 'LineC'], ['Line1', 'Line2'], 'currentTime', 0 , '=')
            self.assertIs(comparison.getResult(), 'Line1')
            
        def test_3_getResult(self):
            StartPoint = ExtremePointMode(True, None, 'LineX')
            self.assertEqual(StartPoint.currentTime, -1)
            Modeobject = originalMode('Mode', StartPoint, ['LineX', 'LineY'], 'LineC')
            self.assertEqual(Modeobject.currentTime, 0)    
            comparison = Decide('Decide', Modeobject, ['LineA', 'LineB', 'LineC'], ['Line1', 'Line2'], 'currentTime', 100 , '>')
            self.assertIs(comparison.getResult(), 'Line2')
            
        def test_4_getResult(self):
            StartPoint = ExtremePointMode(True, None, 'LineX')
            self.assertEqual(StartPoint.currentTime, -1)
            Modeobject = originalMode('Mode', StartPoint, ['LineX', 'LineY'], 'LineZ')
            self.assertEqual(Modeobject.currentTime, 0)
            comparison_1 = Decide('Decide', Modeobject, ['LineZ'], ['Line1', 'Line2'], 'currentTime', 0 , '=')
            self.assertIs(comparison_1.getResult(), 'Line1')
            comparison_2 = Decide('Decide', Modeobject, ['Line1'], ['LineA', 'LineB'], 'currentTime', 100 , '>')
            self.assertIs(comparison_2.getResult(), 'LineB')    
            
       


    unittest.main()   