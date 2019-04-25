import os

#==============================================================================
# def getFile():
#     AllFile = []
#     filesFolder = [f for f in os.listdir('.') if os.path.isdir(f)]
#     for f in filesFolder:
#         filesPY = [i for i in os.listdir('./'+ str(f)) if not os.path.isdir(i) and os.path.splitext(i)[1] == '.py']
#         for i in filesPY:
#             file = f+'.'+os.path.splitext(i)[0]
#             AllFile.append(file)
#     return AllFile   
#==============================================================================

def getFile():
    AllFile = []
    filesFolder = [f for f in os.listdir('.') if os.path.isdir(f)]
    
    for f in filesFolder:
        AllFile.extend(findFile(f))
    for i in range(len(AllFile)):
        AllFile[i] = AllFile[i].replace('/', '.') 
    return AllFile 

def findFile(folder = None):
    if folder == None:
        return ;
    else:
        filesFolder = []
        if type(folder) is str:
            folder_path = '/'+ folder
        for f in os.listdir('.'+ folder_path):
            if os.path.isdir(f):
                pass
            else:
                if os.path.splitext(f)[1] == '.py':
                    file = folder+'.'+os.path.splitext(f)[0]
                    filesFolder.append(file) 
                if os.path.splitext(f)[1] == '':
                    file = folder+'/'+os.path.splitext(f)[0]
                    filesFolder.extend(findFile(file))               
        return filesFolder    
  


def getClass():
    # ClassList =  [ClassName]
    BasicClass = ['ExtremePointMode', 'originalMode', 'Decide', 'Loop'] 
    
    #TEST = ['testMode']
    
    UserdefinedClass = ['Mode_Init', 'Mode_ThreePhaseShortCircuit', 'Mode_ThreePhaseShortCircuit_MagBrake', 'Mode_MaxPower', 
    'Mode_MaxTorqueCurrent', 'Mode_MaxTorqueCurrent_MagBrake']  
    
    AllClass = []
    AllClass.extend(BasicClass)
    #AllClass.extend(TEST)
    AllClass.extend(UserdefinedClass)
    return AllClass


if __name__=='__main__':
    import unittest
    
    class test_GetClass(unittest.TestCase):     
        def test_isStrings(self):
            AllClass = getClass()
            for i in AllClass:
                self.assertIs(type(i), str)
    class test_GetFile(unittest.TestCase):    
        def test_isStrings(self):
            file = getFile()
            for i in file:
                self.assertIs(type(i), str)        
                
    unittest.main()



