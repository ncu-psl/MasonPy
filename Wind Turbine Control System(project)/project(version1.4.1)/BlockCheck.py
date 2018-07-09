from Block import*
class blockcheck(block):
    def __init__(self, blockname, inputMode, inputlist, outlist, cycletime=0, variable, value, Operator):
        self.blockname = blockname
        self.inputMode = inputMode
        self.input     = inputlist
        self.outTrue   = outlist[0]
        self.outFalse  = outlist[1]
        self.cycletime = 0
        self.parameter = parameter
        self.value     = value
        self.Operator  = Operator
    
    def connectLine(self):
        if Operator == '>=':
            Line = self.Comparisongreaterorequal()
        else:
            Line = self.Comparisongreater()
        return Line    


    
    def Comparisongreaterorequal(self):
        if self.parameter == 'WindSpeed':
            Authenticity = inputMode.WindSpeed >= self.value
        if self.parameter == 'RPM':
            Authenticity = inputMode.RPM >= self.value
        if self.parameter == 'Power':
            Authenticity = inputMode.power >= self.value
        if Authenticity is True:
            return self.outTrue
        else:
            return self.outFalse

    def Comparisongreater(parameter, value):
        if self.parameter == 'WindSpeed':
            Authenticity = inputMode.WindSpeed > self.value
        if self.parameter == 'RPM':
            Authenticity = inputMode.RPM > self.value
        if self.parameter == 'Power':
            Authenticity = inputMode.power > self.value
        if Authenticity is True:
            return self.outTrue
        else:
            return self.outFalse