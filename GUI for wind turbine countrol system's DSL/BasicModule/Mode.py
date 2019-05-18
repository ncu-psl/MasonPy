from numpy import*

class originalMode(object):
    def __init__(self, name = '', lastMode = None, inputLines=[], outputLines=''):
        self.setintro()
        self.name = name
        self.lastMode = lastMode
        self.inputLines = inputLines
        self.outputLines = outputLines
        self.calculate()
        self.AllVariables = []
        self.setInit()
        
    def setintro(self):
        self.intro_str = ''
        
    def setInit(self):
        self.setInitValue()
        pass
    
    def do(self):
        pass
    
    def setInitValue(self, *parameters):  # parameter = [variable, value]  self.variable=value
        for i in range(len(parameters[0])):
            self.AllVariables.append(str(parameters[0][i][0]))
            exec( 'self.' + str(parameters[0][i][0]) +'='+ str(parameters[0][i][1]))
            # type == str
              
    def calculate(self):
        if self.lastMode != None:
            self.currentTime = self.lastMode.currentTime + 1
        else:
            self.currentTime = 0     
    
    def rename(self, name):
        self.name = name
        return self.name
    
    def setLastMode(self, lastMode):
        self.lastMode = lastMode
        return self.lastMode
    
    def setInputLines(self, inputLines):
        self.inputLines = inputLines
        return self.inputLines
            
    def setOutputLines(self, outputLines):
        self.OutputLines = outputLines     
        return self.OutputLines
    
    def checkConnect(self, lastMode):
        if isinstance(lastMode, originalMode):
            if lastMode.outputLines in self.inputLines:
                return True
            else:
                print('Can not connect !')
                return False
#==============================================================================
#                 msg = 'Can not connect !'
#                 return  msg
#==============================================================================
        else:
            print('type of input is error !')
            return False            
#==============================================================================
#             msg = 'type of input is error !'
#             return msg
#==============================================================================
        
    def isConnect(self):
        connectLine = self.lastMode.outputLines
        if connectLine in self.inputLines:
            return True
        else:
            print('Not connected !')
            return False
#==============================================================================
#             msg = 'Not connected !'
#             return  msg
#==============================================================================
   
    def getValue(self, obj, string):
        if  str(string) in dir(obj):
            value = eval('self.'+string)
            return value
        else:
            print('Parameter error !')
            return False
#==============================================================================
#             msg = 'Parameter error !'
#             return msg
#==============================================================================

    
    
if __name__ == '__main__':
    from ExtremePoint import*
    import unittest
    
    class test(unittest.TestCase):
        
        def test_newobject(self):
            
            Modeobject = originalMode()
            self.assertIsNotNone(Modeobject)
        
        def test_Property(self):
            Modeobject = originalMode()
            self.assertIs(Modeobject.name, '')
            self.assertIsNone(Modeobject.lastMode)
            self.assertEqual(Modeobject.inputLines, [])
            self.assertIs(Modeobject.outputLines, '')
            self.assertEqual(Modeobject.currentTime, 0)
            
        def test_method_1_rename(self):
            Modeobject = originalMode()
            self.assertIs(Modeobject.rename('ABC'), 'ABC')
            
        def test_method_2_setLastMode(self):
            Modeobject = originalMode()
            lastMode = originalMode()
            self.assertIs(type(Modeobject.setLastMode(lastMode)), type(lastMode))
            
        def test_method_3_setInputLines(self):
            Modeobject = originalMode()
            inputLines = ['LineA', 'LineB']
            self.assertEqual(Modeobject.setInputLines(inputLines), inputLines)
        
        def test_method_4_setOutputLines(self):
            Modeobject = originalMode()
            outputLines = 'LineA'
            self.assertEqual(Modeobject.setOutputLines(outputLines), outputLines)
            
        def test_5_currentTime(self):
            lastMode = originalMode('last', None, ['LineX', 'LineY'], 'LineA')
            self.assertEqual(lastMode.currentTime, 0)
            nextMode = originalMode('next', lastMode, ['LineA', 'LineB'], 'LineF')
            self.assertEqual(nextMode.currentTime, 1)
        
        def test_method_6_isConnect(self):
            lastMode = originalMode('lastMode', None, ['LineX', 'LineY'], 'LineA')
            nextMode = originalMode('Mode_1', lastMode, ['LineA', 'LineB'], 'LineF')
            self.assertIs(nextMode.isConnect(), True)
        
        def test_method_7_isConnect(self):
            lastMode = originalMode('lastMode', None, ['LineX', 'LineY'], 'LineC')
            nextMode = originalMode('Mode_1', lastMode, ['LineA', 'LineB', 'LineC', 'LineD'], 'LineF')
            self.assertIs(nextMode.isConnect(), True)
        
        def test_method_8_isConnect(self):
            lastMode = originalMode('lastMode', None, ['LineX', 'LineY'], 'LineC')
            nextMode = originalMode('Mode_1', lastMode, ['LineA', 'LineB'], 'LineC')
            self.assertIs(nextMode.isConnect(), False)   
            
        def test_method_9_getValue(self):
            lastMode = originalMode('last', None, ['LineX', 'LineY'], 'LineA')
            nextMode = originalMode('next', lastMode, ['LineA', 'LineB'], 'LineF') 
            self.assertIs(nextMode.getValue(nextMode, 'name'), 'next')    
            self.assertIs(type(nextMode.getValue(nextMode, 'lastMode')), type(lastMode))
            self.assertEqual(nextMode.getValue(nextMode, 'inputLines'), ['LineA', 'LineB'])
            self.assertIs(nextMode.getValue(nextMode, 'outputLines'), 'LineF')
            
        def test_method_10_getValue(self):
            lastMode = originalMode('last', None, ['LineX', 'LineY'], 'LineA')
            nextMode = originalMode('next', lastMode, ['LineA', 'LineB'], 'LineF') 
            self.assertIs(nextMode.getValue(nextMode, 'data'), False) 
        
        def test_method_11_checkConnect(self):
            A_Mode = originalMode('A', None, ['LineX', 'LineY'], 'LineA')
            B_Mode = originalMode('B', A_Mode, ['LineA', 'LineB'], 'LineF') 
            self.assertIs(A_Mode.checkConnect(B_Mode), False)

        def test_method_12_checkConnect(self):
            A_Mode = originalMode('A', None, ['LineX', 'LineY'], 'LineA')
            B_Mode = originalMode('B', A_Mode, ['LineA', 'LineB'], 'LineF') 
            self.assertEqual(B_Mode.checkConnect(A_Mode), True)
        
        def test_13_getResultLine(self):
            
            StartPoint = ExtremePointMode(True, None, 'LineX')
            self.assertEqual(StartPoint.currentTime, -1)
            Modeobject = originalMode('Mode', StartPoint, ['Line0'], 'Line1')
            Modelist = []
            Modelist.append(Modeobject)
            for i in range(4):
                Modeobject = originalMode('Mode', Modeobject, ['Line'+ str(1 + i)], 'Line' + str(2 + i))
                Modelist.append(Modeobject)
            
            self.assertEqual(Modelist[4].currentTime, Modelist[4].getValue(Modelist[4], 'currentTime'))


    unittest.main()   