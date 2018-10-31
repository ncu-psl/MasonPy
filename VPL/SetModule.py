import os

def getFile():
    AllFile = []
    filesFolder = [f for f in os.listdir('.') if os.path.isdir(f)]
    for f in filesFolder:
        filesPY = [i for i in os.listdir('./'+ str(f)) if not os.path.isdir(i) and os.path.splitext(i)[1] == '.py']
        for i in filesPY:
            file = f+'.'+os.path.splitext(i)[0]
            AllFile.append(file)
    return AllFile     


def getClass():
    # ClassList =  [ClassName]
    BasicClass = ['ExtremePointMode', 'originalMode', 'Decide', 'Loop', 'testMode'] 
    
    UserdefinedClass = ['testMode']  
    
    ModuleandClass = []
    ModuleandClass.extend(BasicClass)
    ModuleandClass.extend(UserdefinedClass)
    
    return ModuleandClass


if __name__=='__main__':
    import unittest
    
    class test(unittest.TestCase):     
        def test_isStrings(self):
            ModuleandClass = getModuleandClass()
            for i in ModuleandClass:
                self.assertIs(type(i), str)
    unittest.main()
