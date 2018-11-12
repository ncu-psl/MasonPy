from UserDefinedModule.Databaseformat import*
from UserDefinedModule.OpenFile import*
from UserDefinedModule.TurbineMode.WindTurbine import*

class Mode_MaxPower(turbineMode):
    def CalculateValue(self, LastMode, database, WindSpeed):
        self.CurrentTime  = LastMode.CurrentTime + 1
        self.WindSpeed    = WindSpeed[self.CurrentTime]
        self.mode         = self.namemode('Mode_MaxPower')
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
        
        
#==============================================================================
# if __name__ == '__main__':
#     import unittest
#     import OpenFile
#     from initMode import*
#     
#     class test(unittest.TestCase):
#         
#         def test_newobject(self):
#             RPMtoEffg_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower = OpenFile.ReadData_MaxPower()
#             database_MaxPower = referencedata(None, RPMtoEffg_MaxPower, eff_g_MaxPower, None, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower)
#             Number, TimeSeries, WindSpeed = OpenFile.ReadWindSpeepData()
#             
#             init = Mode_init()
#             MaxPower = Mode_MaxPower(init, database_MaxPower, WindSpeed)
#             self.assertIsNotNone(MaxPower)
#         
#         def test_Property(self):
#             RPMtoEffg_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower = OpenFile.ReadData_MaxPower()
#             database_MaxPower = referencedata(None, RPMtoEffg_MaxPower, eff_g_MaxPower, None, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower)
#             Number, TimeSeries, WindSpeed = OpenFile.ReadWindSpeepData()
#             init = Mode_init()
#             MaxPower = Mode_MaxPower(init, database_MaxPower, WindSpeed)
#             
#         
#             self.assertEquals(MaxPower.CurrentTime, 1)
#             self.assertEquals(MaxPower.WindSpeed, 7.3)
#             self.assertIs(MaxPower.mode, 'Mode_MaxPower')
#             self.assertEquals(MaxPower.eff_e, 0.9)
#       
# 
#         
# 
#     unittest.main()        
#==============================================================================
