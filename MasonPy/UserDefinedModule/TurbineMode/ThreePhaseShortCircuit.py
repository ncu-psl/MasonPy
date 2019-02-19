from UserDefinedModule.Databaseformat import*
from UserDefinedModule.OpenFile import*
from UserDefinedModule.TurbineMode.WindTurbine import*

class Mode_ThreePhaseShortCircuit(turbineMode):

    def CalculateValue(self):
        self.readFile()
        self.currentTime  = self.lastMode.currentTime + 1
        self.WindSpeedList= self.lastMode.WindSpeedList
        self.WindSpeed    = self.WindSpeedList[self.currentTime]
        self.mode         = self.namemode('Mode_ThreePhaseShortCircuit')
        self.Tsr          = self.CalculateTSR(self.lastMode.RPM, self.D, self.WindSpeed)
        self.Cp           = self.CalculateCp(self.Tsr, self.database_ThreePhaseShortCircuit.Tsr, self.database_ThreePhaseShortCircuit.Cp)
        self.Tb           = self.CalculateTorqueBlade(self.Cp, self.Rho, self.A, self.WindSpeed, self.lastMode.RPM)
        self.Tg           = self.CalculateTg(self.lastMode.RPM, self.database_ThreePhaseShortCircuit.RPMtoTg, self.database_ThreePhaseShortCircuit.Tg)
        self.Tm           = self.setTm()
        self.Tt           = self.CalculateTotalTorque(self.Tb, self.Tg, self.Tm)  
        self.eff_g        = self.CalculateEff_g(self.WindSpeed, self.database_ThreePhaseShortCircuit.WindSpeed, self.database_ThreePhaseShortCircuit.eff_g)
        self.eff_e        = 0.9
        self.RPM          = 0
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)
        
    def readFile(self):
        self.WindSpeed_ThreePhaseShortCircuit, self.eff_g_ThreePhaseShortCircuit, self.eff_e_ThreePhaseShortCircuit, self.RPM_ThreePhaseShortCircuit , self.Tg_ThreePhaseShortCircuit, self.Tsr_ThreePhaseShortCircuit, self.Cp_ThreePhaseShortCircuit = ReadData_ThreePhaseShortCircuit()
        self.database_ThreePhaseShortCircuit = referencedata(self.WindSpeed_ThreePhaseShortCircuit, None, self.eff_g_ThreePhaseShortCircuit, None, self.RPM_ThreePhaseShortCircuit , self.Tg_ThreePhaseShortCircuit, self.Tsr_ThreePhaseShortCircuit, self.Cp_ThreePhaseShortCircuit)
        
        
