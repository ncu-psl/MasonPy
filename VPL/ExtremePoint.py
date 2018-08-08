from Mode import*

class ExtremePointMode(object):
    def __init__(self, STartorEnd = None, inputLines=[], outputLines=''):
        if STartorEnd:
            self.Mode = 'START'
            self.currentTime = -1
            self.inputLines = None
            self.outputLines = outputLines
        else:
            self.Mode = 'END'
            self.currentTime = -2
            self.inputLines = inputLines
            self.outputLines = None
    
    

    
    
if __name__ == '__main__':
    import unittest
    
    class test(unittest.TestCase):
        
        def test_newobject(self):
            StartPoint = ExtremePointMode(True)
            self.assertIsNotNone(StartPoint)
            
        def test_object_Start(self):
            StartPoint = ExtremePointMode(True, None, 'Line1')
            self.assertIs(StartPoint.Mode, 'START')
            self.assertEqual(StartPoint.currentTime, -1)
            self.assertIs(StartPoint.inputLines, None)    
            self.assertIs(StartPoint.outputLines, 'Line1')
            
        def test_object_End(self):
            StartPoint = ExtremePointMode(False,  ['Line1', 'Line2', 'Line3'] , None)
            self.assertIs(StartPoint.Mode, 'END')
            self.assertEqual(StartPoint.currentTime, -2)
            self.assertEqual(StartPoint.inputLines, ['Line1', 'Line2', 'Line3'])    
            self.assertIs(StartPoint.outputLines, None)    

    unittest.main()   