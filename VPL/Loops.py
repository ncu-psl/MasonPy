class Loop():
    def __init__(self, Times, lastMode):
        self.lastMode = lastMode
        self.Times = Times
        self.counter = Times
        
    def clearCounter(self):
        self.counter = self.Times
    
    def decreaseCounter(self):
        self.counter = self.counter - 1
    
    def getCounter(self):
        return self.counter
    
    def setlastMode(self, lastMode):
        self.lastMode = lastMode
    
    def getlastMode(self):
        return self.lastMode