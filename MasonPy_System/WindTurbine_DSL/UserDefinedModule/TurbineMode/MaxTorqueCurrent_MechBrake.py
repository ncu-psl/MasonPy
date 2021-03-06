from UserDefinedModule.TurbineMode.MaxTorqueCurrent import*
from UserDefinedModule.Databaseformat import*
from UserDefinedModule.OpenFile import*

class MaxTorqueCurrent_MechBrake(MaxTorqueCurrent):
    def CalculateValue(self):
        self.readFile()
        self.left_data_size = self.lastMode.left_data_size -1
        self.currentTime  = self.lastMode.currentTime + 1
        self.WindSpeedList= self.lastMode.WindSpeedList
        self.WindSpeed    = self.WindSpeedList[self.currentTime]
        self.mode         = self.namemode('MaxTorqueCurrent_MechBrake')
        self.Tsr          = self.CalculateTSR(self.lastMode.RPM, self.D, self.WindSpeed)
        self.Cp           = self.CalculateCp(self.Tsr, self.database_MaxTorqueCurrent.Tsr, self.database_MaxTorqueCurrent.Cp)
        self.Tb           = self.CalculateTorqueBlade(self.Cp, self.Rho, self.A, self.WindSpeed, self.lastMode.RPM)
        self.Tg           = self.database_MaxTorqueCurrent.Tg
        self.Tm           = self.setTm(110)
        self.Tt           = self.CalculateTotalTorque(self.Tb, self.Tg, self.Tm)  
        self.eff_g        = self.CalculateEff_g(self.lastMode.RPM, self.database_MaxTorqueCurrent.RPMtoEffg, self.database_MaxTorqueCurrent.eff_g) 
        self.eff_e        = 0.9
        self.RPM          = self.CalculateRPM(self.lastMode.RPM, self.Tt, self.TimeDelta, self.MonmentIntertia)
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)
        Parameter.RPM.append(self.RPM)
        Parameter.Wind_Speed.append(self.WindSpeed)
        Parameter.Power.append(self.power)
        