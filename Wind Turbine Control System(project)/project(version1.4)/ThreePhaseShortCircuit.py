from Mode import*
from dataformat import*
import initMode

class Mode_ThreePhaseShortCircuit(originalMode):
    def CalculateValue(self, LastMode, database = referencedata(), WindSpeed):
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
        self.RPM          = self.CalculateRPM(LastMode.RPM, self.Tt, self.TimeDelta, self.MonmentIntertia)
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)
        
if __name__ == '__main__':
    import unittest

    class test(unittest.TestCase):
        def test_newobject(self):
            init = Mode_init()
            ThreePhase = Mode_ThreePhaseShortCircuit(init)
            self.assertIsNotNone(ThreePhase)
        
#==============================================================================
#         def test_Property(self):
#             init = Mode_init()
#             self.assertEquals(init.MaxWindSpeed_ThreePhaseShortCircuit, 8)
#             self.assertEquals(init.TimeDelta, 0.01)
#             self.assertEquals(init.MonmentIntertia, 0.7)
#             self.assertEquals(init.CutOutRPM, 400)
#             self.assertEquals(init.CutOutPower, 3300)
#             self.assertEquals(init.MaxMagBrake, 42)
#             self.assertEquals(init.Rho, 1.293)
#             self.assertEquals(init.D, 3.7)
#             self.assertEquals(init.A, (3.7/2)**2*pi)
#             self.assertEquals(init.TorqueMachine, 175)
# 
#             self.assertEquals(init.CurrentTime, 0)
#             self.assertEquals(init.WindSpeed, 0)
#             self.assertIs(init.mode, 'initial')
#             self.assertEquals(init.Tsr, 0)
#             self.assertEquals(init.Cp, 0)
#             self.assertEquals(init.Tb, 0)
#             self.assertEquals(init.Tg, 0)
#             self.assertEquals(init.Tm, 0)
#             self.assertEquals(init.eff_g, 0)
#             self.assertEquals(init.eff_e, 0.9)
#             self.assertEquals(init.RPM, 0.0001)
#             self.assertEquals(init.power, 0)
#==============================================================================

    unittest.main()       