from Mode import*



class testMode(originalMode):

    
    def setInit(self):
        self.A=1
        self.B=2
        self.C=3
    
    def do(self):
        print(self.currentTime)
        print('test')
        
        
        
if __name__=='__main__':
    a = testMode()
    print(a.getValue(a,'A'))