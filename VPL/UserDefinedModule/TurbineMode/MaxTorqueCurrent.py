from UserDefinedModule.Databaseformat import*
from UserDefinedModule.OpenFile import*
from UserDefinedModule.TurbineMode.WindTurbine import*

class Mode_MaxTorqueCurrent(turbineMode):
    def CalculateValue(self):
        self.readFile()
        self.currentTime  = self.self.lastMode.currentTime + 1
        self.WindSpeedList= self.self.lastMode.WindSpeedList
        self.WindSpeed    = self.WindSpeedList[self.currentTime]
        self.mode         = self.namemode('Mode_MaxTorqueCurrent')
        self.Tsr          = self.CalculateTSR(self.lastMode.RPM, self.D, self.WindSpeed)
        self.Cp           = self.CalculateCp(self.Tsr, self.database_MaxTorqueCurrent.Tsr, self.database_MaxTorqueCurrent.Cp)
        self.Tb           = self.CalculateTorqueBlade(self.Cp, self.Rho, self.A, self.WindSpeed, self.lastMode.RPM)
        self.Tg           = self.CalculateTg(self.lastMode.RPM, self.database_MaxTorqueCurrent.RPMtoTg, self.database_MaxTorqueCurrent.Tg)
        self.Tm           = self.setTm()
        self.Tt           = self.CalculateTotalTorque(self.Tb, self.Tg, self.Tm)  
        self.eff_g        = self.CalculateEff_g(self.lastMode.RPM, self.database_MaxTorqueCurrent.RPMtoEffg, self.database_MaxTorqueCurrent.eff_g) 
        self.eff_e        = 0.9
        self.RPM          = self.CalculateRPM(self.lastMode.RPM, self.Tt, self.TimeDelta, self.MonmentIntertia)
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)
        
    def readFile(self):
        self.WindSpeed_MaxTorqueCurrent, self.eff_g_MaxTorqueCurrent, self.eff_e_MaxTorqueCurrent, self.RPM_MaxTorqueCurrent , self.Tg_MaxTorqueCurrent, self.Tsr_MaxTorqueCurrent, self.Cp_MaxTorqueCurrent = ReadData_MaxTorqueCurrent()
        self.database_MaxTorqueCurrent = referencedata(self.WindSpeed_MaxTorqueCurrent, None, self.eff_g_MaxTorqueCurrent, None, self.RPM_MaxTorqueCurrent , self.Tg_MaxTorqueCurrent, self.Tsr_MaxTorqueCurrent, self.Cp_MaxTorqueCurrent)
            
        
