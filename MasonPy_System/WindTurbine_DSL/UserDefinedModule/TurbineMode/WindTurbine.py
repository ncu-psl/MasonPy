from BasicModule.Mode import*
from numpy import*
import Parameter
#from Databaseformat import*


class turbineMode(originalMode):
    def setInit(self):
        parameters = []
#        parameters.append(['WindSpeedList', WindSpeed])
        parameters.append(['left_data_size', None])
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
        parameters.append(['RPM', None])
        parameters.append(['power', None])
        
        
#        print(parameters)
        
        self.setInitValue(parameters)
        
    def do(self):
        self.CalculateValue()
        
#==============================================================================
#     def __init__(self , LastMode=None, database = referencedata(), WindSpeed=0):
#         self.MaxWindSpeed_ThreePhaseShortCircuit = 8
#         self.TimeDelta       = 0.01
#         self.MonmentIntertia = 0.7
#         self.CutOutRPM       = 400
#         self.CutOutPower     = 3300
#         self.MaxMagBrake     = 42
#         self.Rho             = 1.293
#         self.D               = 3.7
#         self.A               = ((self.D)/2)**2 * pi
#         self.TorqueMachine   = 175
#         
#         self.CalculateValue(LastMode, database, WindSpeed)
#==============================================================================
        
    def CalculateValue(self):
        # self.lastmode     = LastMode
        
        self.left_data_size = self.lastMode.left_data_size -1
        self.currentTime  = self.lastMode.currentTime + 1
        self.WindSpeed    = self.WindSpeedList[self.currentTime]
        self.mode         = self.namemode()
        self.Tsr          = self.CalculateTSR(self.lastMode.RPM, self.D, self.WindSpeed)
        self.Cp           = self.CalculateCp(self.Tsr, database.Tsr, database.Cp)
        self.Tb           = self.CalculateTorqueBlade(self.Cp, self.Rho, self.A, self.WindSpeed, self.lastMode.RPM)
        self.Tg           = self.CalculateTg(self.lastMode.RPM, database.RPMtoTg, database.Tg)
        self.Tm           = self.setTm()
        self.Tt           = self.CalculateTotalTorque(self.Tb, self.Tg, self.Tm)  
        self.eff_g        = None # self.CalculateEff_g() 
        self.eff_e        = None # self.CalculateEff_e()
        self.RPM          = self.CalculateRPM(self.lastMode.RPM, self.Tt, self.TimeDelta, self.MonmentIntertia)
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)
        

    def namemode(self, mode=''):
        self.mode = mode
        return mode
        
    def CalculateTSR(self, LastRPM, D, WindSpeed):
        if WindSpeed == 0:
            WindSpeed = 0.0001
        Tsr = 2 * pi * (LastRPM / 60) * (D / 2) / WindSpeed
        return Tsr 

    def CalculateCp(self, index, domainlist, rangelist):
        # Approximate Cp by Tsr
        # Cp = self.getApproximation(Tsr, Tsrlist, Cplist)
        Cp = self.getApproximation(index, domainlist, rangelist)
        return Cp
    
    def CalculateTorqueBlade(self, Cp, Rho, A, WindSpeed, LastRPM):
        if LastRPM == 0:
            LastRPM = 0.001
        TorqueBlade = Cp * 0.5 * Rho * A * (WindSpeed**3) / (2 * pi * (LastRPM/60))
        return TorqueBlade
    
    
    
    def CalculateTg(self, index, domainlist, rangelist):
        # Approximate Tg by RPM
        # Tg = self.getApproximation(LastRPM, RPMlist, Tglist)
        Tg = self.getApproximation( index, domainlist, rangelist) 
        if Tg < 0:
            Tg = 0
        return Tg
    
    def setTm(self, TorqueMachine=0):
        Tm = TorqueMachine
        return Tm
    
    
    def CalculateTotalTorque(self, TorqueBlade, TorqueGenerator, TorqueMachine = 0):  
        totaltorque = TorqueBlade - TorqueGenerator - TorqueMachine
        return totaltorque

    def CalculateEff_g(self, index, domainlist, rangelist):
        # eff_g = self.getApproximation(WindSpeed or LastRPM, WindSpeedlist or RPMlist, eff_glist)
        eff_g = self.getApproximation(index, domainlist, rangelist)
        return eff_g

    def CalculateEff_e(self, index, domainlist, rangelist): 
        # eff_g = self.getApproximation(WindSpeed or RPM, WindSpeedlist or RPMlist, eff_elist)
        eff_e = self.getApproximation(index, domainlist, rangelist)
        return eff_e
    
    
    
    def CalculateRPM(self, LastRPM, TorqueTotal, TimeDelta, MonmentIntertia):
        rpm= LastRPM + ( TorqueTotal * TimeDelta / MonmentIntertia ) * 60 / ( 2 * pi )
        if rpm <= 0:
            rpm = 0.01
        return rpm


    def CalculatePower(self, RPM, eff_g, eff_e, Torque):
        power = 2 * pi * RPM/60 * Torque * eff_g * eff_e
        if power < 0:
            power=0                              
        return power
    
    
# 內差近似    
    def getApproximation(self, index, domainlist, rangelist):
        indexleft, indexright = self.getMargin(index, domainlist)
        leftx    = domainlist[indexleft]
        lefty    = rangelist[indexleft]
        rightx   = domainlist[indexright]
        righty   = rangelist[indexright]
        value    = self.getpointinLinearEquation(leftx, lefty, rightx, righty, index)
        if value < 0:
           value = 0 
        #print(leftx, lefty, rightx, righty, index)   
        return value


    def getMargin(self, index, domainlist):
        indexleft  = 0
        indexright = 0
        if index < domainlist[0]:
            indexleft  = 0
            indexright = 1
        elif index > domainlist[len(domainlist)-1]:
            indexleft  = len(domainlist)-2
            indexright = len(domainlist)-1
        else: 
            for i in range(0,len(domainlist)-1):
                if index == domainlist[i]:
                    indexleft  = i
                    indexright = i
                    break;      
                if index > domainlist[i] and index < domainlist[i+1]:
                    indexleft  = i
                    indexright = i+1
                    break; 
            if index == domainlist[len(domainlist)-1]:
                indexleft  = len(domainlist)-1
                indexright = len(domainlist)-1    
        return indexleft, indexright
    
    def getpointinLinearEquation(self, startx, starty, endx, endy, pointx):
        if startx == endx: 
            pointy = starty
        else:
            pointy = (pointx-startx)*(endy-starty)/(endx-startx)+starty
        return pointy
    
    
   

