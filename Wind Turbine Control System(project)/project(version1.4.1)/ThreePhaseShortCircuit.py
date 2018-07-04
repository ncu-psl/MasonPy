from Mode import*
from Databaseformat import*


class Mode_ThreePhaseShortCircuit(originalMode):
    def CalculateValue(self, LastMode, database = referencedata(), WindSpeed=0):
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
        
if __name__ == '__main__':
    import unittest
    import OpenFile
    from initMode import*
    
    class test(unittest.TestCase):
        
        def test_newobject(self):
            WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit, eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit = OpenFile.ReadData_ThreePhaseShortCircuit()
            database_ThreePhaseShortCircuit = referencedata(WindSpeed_ThreePhaseShortCircuit, None, eff_g_ThreePhaseShortCircuit, None, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit)
            Number, TimeSeries, WindSpeed = OpenFile.ReadWindSpeepData()
            
            init = Mode_init()
            ThreePhase = Mode_ThreePhaseShortCircuit(init, database_ThreePhaseShortCircuit, WindSpeed)
            self.assertIsNotNone(ThreePhase)
        
        def test_Property(self):
            WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit, eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit = OpenFile.ReadData_ThreePhaseShortCircuit()
            database_ThreePhaseShortCircuit = referencedata(WindSpeed_ThreePhaseShortCircuit, None, eff_g_ThreePhaseShortCircuit, None, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit)
            Number, TimeSeries, WindSpeed = OpenFile.ReadWindSpeepData()
            init = Mode_init()
            ThreePhase = Mode_ThreePhaseShortCircuit(init, database_ThreePhaseShortCircuit, WindSpeed)
            
        
            self.assertEquals(ThreePhase.CurrentTime, 1)
            self.assertEquals(ThreePhase.WindSpeed, 7.3)
            self.assertIs(ThreePhase.mode, 'Mode_ThreePhaseShortCircuit')
            self.assertEquals(ThreePhase.eff_e, 0.9)
            self.assertEquals(ThreePhase.RPM, 0)

        

    unittest.main()       