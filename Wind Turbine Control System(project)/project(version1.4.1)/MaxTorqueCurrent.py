from Mode import*
from Databaseformat import*

class Mode_MaxTorqueCurrent(originalMode):
    def CalculateValue(self, LastMode, database, WindSpeed):
        self.CurrentTime  = LastMode.CurrentTime + 1
        self.WindSpeed    = WindSpeed[self.CurrentTime]
        self.mode         = self.namemode('Mode_MaxTorqueCurrent')
        self.Tsr          = self.CalculateTSR(LastMode.RPM, self.D, self.WindSpeed)
        self.Cp           = self.CalculateCp(self.Tsr, database.Tsr, database.Cp)
        self.Tb           = self.CalculateTorqueBlade(self.Cp, self.Rho, self.A, self.WindSpeed, LastMode.RPM)
        self.Tg           = self.CalculateTg(LastMode.RPM, database.RPMtoTg, database.Tg)
        self.Tm           = self.setTm()
        self.Tt           = self.CalculateTotalTorque(self.Tb, self.Tg, self.Tm)  
        self.eff_g        = self.CalculateEff_g(LastMode.RPM, database.RPMtoEffg, database.eff_g) 
        self.eff_e        = 0.9
        self.RPM          = self.CalculateRPM(LastMode.RPM, self.Tt, self.TimeDelta, self.MonmentIntertia)
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)
        
        
        
