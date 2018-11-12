from UserDefinedModule.Databaseformat import*
from UserDefinedModule.OpenFile import*
from UserDefinedModule.TurbineMode.WindTurbine import*

class Mode_Init(turbineMode):
    def setInit(self):
        
        WindSpeedSize, TimeSeries, WindSpeed = ReadWindSpeepData()
        
        parameters = []
#        parameters.append(['WindSpeedList', WindSpeed])
        parameters.append(['MaxWindSpeed_ThreePhaseShortCircuit', 8])
        parameters.append(['TimeDelta', 0.01])
        parameters.append(['MonmentIntertia', 0.7])
        parameters.append(['CutOutRPM', 400])
        parameters.append(['CutOutPower', 3300])
        parameters.append(['MaxMagBrake', 42])
        parameters.append(['Rho', 1.293])
        parameters.append(['D', 3.7])
        parameters.append(['A', '((self.D)/2)**2 * pi'])
        parameters.append(['TorqueMachine', 175])
        
        # parameters.append(['lastMode', ?])
        parameters.append(['WindSpeed', 0])
        parameters.append(['mode', None])
        parameters.append(['Tsr', 0])
        parameters.append(['Cp', None])
        parameters.append(['Tb', None])
        parameters.append(['Tg', None])
        parameters.append(['Tt', None])
        parameters.append(['RPM', 0.0001])
        parameters.append(['power', 0])
        
        
#        print(parameters)
        
        self.setInitValue(parameters)
     
    def calculate(self):
        if self.lastMode != None:
            self.currentTime = self.lastMode.currentTime + 1
        else:
            self.currentTime = 0
   
    def do(self):
        self.calculate()         
        
        
        
if __name__=='__main__':
    FirstMode = Mode_Init()
    
#    print(dir(FirstMode))
    print(FirstMode.RPM)
