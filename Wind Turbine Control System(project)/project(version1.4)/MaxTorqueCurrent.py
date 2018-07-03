import Mode
import dataformat

class Mode_MaxTorqueCurrent(Mode):
    def CalculateValue(self, LastMode, database = dataformat.referencedata(), WindSpeed):
        self.WindSpeed    = WindSpeed
        self.mode         = self.namemode()
        self.Tsr          = self.CalculateTSR(LastMode.RPM, self.D, self.WindSpeed)
        self.Cp           = self.CalculateCp(self.Tsr, database.Tsr, database.Cp)
        self.Tb           = self.CalculateTorqueBlade(self.Cp, self.Rho, self.A, self.WindSpeed, LastMode.RPM)
        self.Tg           = self.CalculateTg(LastMode.RPM, database.RPM, database.Tg)
        self.Tm           = self.setTm()
        self.Tt           = self.CalculateTotalTorque(self.Tb, self.Tg, self.Tm)  
        self.eff_g        = self.CalculateEff_g(self.RPM, database.RPM, database.eff_g) 
        self.eff_e        = 0.9
        self.CurrentTime  = LastMode.CurrentTime + 1
        self.RPM          = self.CalculateRPM(LastMode.RPM, self.Tt, self.TimeDelta, self.MonmentIntertia)
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)