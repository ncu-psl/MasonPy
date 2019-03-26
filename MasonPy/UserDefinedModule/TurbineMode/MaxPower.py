from UserDefinedModule.Databaseformat import*
from UserDefinedModule.OpenFile import*
from UserDefinedModule.TurbineMode.WindTurbine import*

class Mode_MaxPower(turbineMode):
    def CalculateValue(self):
        self.readFile()
        self.left_data_size = self.lastMode.left_data_size -1
        self.currentTime  = self.lastMode.currentTime + 1
        self.WindSpeedList= self.lastMode.WindSpeedList
        self.WindSpeed    = self.WindSpeedList[self.currentTime]
        self.mode         = self.namemode('Mode_MaxPower')
        self.Tsr          = self.CalculateTSR(self.lastMode.RPM, self.D, self.WindSpeed)
        self.Cp           = self.CalculateCp(self.Tsr, self.database_MaxPower.Tsr, self.database_MaxPower.Cp)
        self.Tb           = self.CalculateTorqueBlade(self.Cp, self.Rho, self.A, self.WindSpeed, self.lastMode.RPM)
        self.Tg           = self.CalculateTg(self.lastMode.RPM, self.database_MaxPower.RPMtoTg, self.database_MaxPower.Tg)
        self.Tm           = self.setTm()
        self.Tt           = self.CalculateTotalTorque(self.Tb, self.Tg, self.Tm)  
        self.eff_g        = self.CalculateEff_g(self.lastMode.RPM, self.database_MaxPower.RPMtoEffg, self.database_MaxPower.eff_g) 
        self.eff_e        = 0.9
        self.RPM          = self.CalculateRPM(self.lastMode.RPM, self.Tt, self.TimeDelta, self.MonmentIntertia)
        self.power        = self.CalculatePower(self.RPM, self.eff_g, self.eff_e, self.Tg)
        
    def readFile(self):
        self.WindSpeed_MaxPower, self.eff_g_MaxPower, self.eff_e_MaxPower, self.RPM_MaxPower , self.Tg_MaxPower, self.Tsr_MaxPower, self.Cp_MaxPower = ReadData_MaxPower()
        self.database_MaxPower = referencedata(self.WindSpeed_MaxPower, None, self.eff_g_MaxPower, None, self.RPM_MaxPower , self.Tg_MaxPower, self.Tsr_MaxPower, self.Cp_MaxPower)
        
        
    
        
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
#             self.assertEquals(MaxPower.currentTime, 1)
#             self.assertEquals(MaxPower.WindSpeed, 7.3)
#             self.assertIs(MaxPower.mode, 'Mode_MaxPower')
#             self.assertEquals(MaxPower.eff_e, 0.9)
#       
# 
#         
# 
#     unittest.main()        
#==============================================================================
