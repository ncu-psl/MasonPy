from BasicModule.Mode import*

class testMode(originalMode):

    
    def setInit(self):
        self.setInitValue([['A', 0], ['B', 1], ['C',2]])
    
    def do(self):
        print(self.currentTime)
        print('test')
        
          
        
if __name__=='__main__':
    a = testMode()
    print(a.AllVariables)
    print(a.getValue(a, 'A'))
    print(a.getValue(a, 'B'))
    print(a.getValue(a, 'C'))
    print(a.getValue(a, 'X'))



