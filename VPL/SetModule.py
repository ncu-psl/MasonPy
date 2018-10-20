def getModuleandClass():
    
    # ModuleandClass =  [file.py, class]
    ModuleandClass = [['ExtremePoint', 'ExtremePointMode'], ['Mode', 'originalMode'], ['Decision', 'Decide'], ['Loops', 'Loop'], 
                      ['PrintTest', 'testMode']]  
    
    return ModuleandClass


if __name__=='__main__':
    import unittest
    
    class test(unittest.TestCase):
        
        def test_len(self):
            ModuleandClass = getModuleandClass()
            for i in ModuleandClass:
                self.assertEqual(len(i), 2)          
        
        def test_isStrings(self):
            ModuleandClass = getModuleandClass()
            for i in ModuleandClass:
                self.assertIs(type(i[0]),type('') )
                self.assertIs(type(i[1]),type('') )        

    unittest.main()
