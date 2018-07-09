class block(object):
    def __init__(self, blockname, inputMode, inputlist, outlist, cycletime=0):
        self.Mode      = blockname
        self.inputMode = inputMode
        self.input     = inputlist
        self.outlist   = outlist
        self.cycletime = cycletime