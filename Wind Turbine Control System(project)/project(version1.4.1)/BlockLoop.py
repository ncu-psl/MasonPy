from Block import*
class blockloop(block):
    def __init__(self, blockname, inputMode, inputlist, outlist, cycletime):
        self.blockname = blockname
        self.inputMode = inputMode
        self.input     = inputlist
        self.outTrue   = outlist[0]
        self.outFalse  = outlist[1]
        self.cycletime = cycletime
        self.countdown = cycletime
    
    def connectLine(self):
        self.countdown()
        if self.countdown == 0:
            self.reset()
            Line = self.outTrue
        else:
            Line = self.outFalse
        return Line
    
    def countdown(self):
        self.countdown = self.countdown - 1
            
        
    def reset(self):
        self.countdown = self.cycletime
        