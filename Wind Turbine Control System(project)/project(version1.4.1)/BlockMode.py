from Block import*
class blockmode(block):
    def __init__(self, Mode, inputlist, outlist, cycletime=0):
        self.Mode      = Mode
        self.input     = inputlist
        self.outlist   = outlist[0]
        self.cycletime = 0