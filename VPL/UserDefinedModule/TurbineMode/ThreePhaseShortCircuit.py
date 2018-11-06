import Databaseformat
import OpenFile
import WindTurbine

class Mode_ThreePhaseShortCircuit(WindTurbine.turbineMode):

    def CalculateValue(self, LastMode, database, WindSpeed=0):
        self.CurrentTime  = LastMode.CurrentTime + 1
        self.WindSpeed    = WindSpeed[self.CurrentTime]
        self.mode         = self.namemode('Mode_ThreePhaseShortCircuit')
        self.Tsr          = self.CalculateTSR(LastMode.RPM, self.D, self.WindSpeed)
        self.Cp           = self.CalculateCp(self.Tsr, database.Tsr, database.Cp)
        self.Tb           = self.CalculateTorqueBlade(self.Cp, self.Rho, self.A, self.WindSpeed, LastMode.RPM)
        self.Tg           = self.CalculateTg(LastMode.RPM, database.RPMtoTg, database.Tg)
        self.Tm           = self.setTm()
        self.Tt           = self.CalculateTotalTorque(self.Tb, self.Tg, self.Tm)  
        self.eff_g        = self.CalculateEff_g(self.WindSpeed, database.WindSpeed, database.eff_g)
        self.eff_e        = 0.9
        self.RPM          = 0
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)
        
    def readFile(self):
        self.WindSpeed_ThreePhaseShortCircuit, self.eff_g_ThreePhaseShortCircuit, self.eff_e_ThreePhaseShortCircuit, self.RPM_ThreePhaseShortCircuit , self.Tg_ThreePhaseShortCircuit, self.Tsr_ThreePhaseShortCircuit, self.Cp_ThreePhaseShortCircuit = OpenFile.ReadData_ThreePhaseShortCircuit()
        self.database_ThreePhaseShortCircuit = Databaseformat.referencedata(self.WindSpeed_ThreePhaseShortCircuit, None, self.eff_g_ThreePhaseShortCircuit, None, self.RPM_ThreePhaseShortCircuit , self.Tg_ThreePhaseShortCircuit, self.Tsr_ThreePhaseShortCircuit, self.Cp_ThreePhaseShortCircuit)
        
        
