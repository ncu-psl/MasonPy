class referencedata(object):
    def __init__(self, WindSpeed=None, RPMtoEffg=None, eff_g=None, eff_e=None, RPMtoTg=None, Tg=None, Tsr=None, Cp=None):
        self.WindSpeed = WindSpeed
        self.RPMtoEffg = RPMtoEffg
        self.eff_g     = eff_g
        self.eff_e     = eff_e
        
        self.RPMtoTg   = RPMtoTg
        self.Tg        = Tg
        
        self.Tsr       = Tsr
        self.Cp        = Cp
        
    def setWindSpeed(self, WindSpeed=None):
        self.WindSpeed = WindSpeed
        return self.WindSpeed
    
    def setRPMtoEffg(self, RPMtoEffg=None):
        self.RPMtoEffg   = RPMtoEffg
        return self.RPMtoEffg
    
    def setEff_g(self, eff_g=None):
        self.eff_g     = eff_g
        return self.eff_g
    
    def setEff_e(self, eff_e=None):
        self.eff_e     = eff_e
        return self.eff_e
    
    def setRPMtoTg(self, RPMtoTg=None):
        self.RPMtoTg   = RPMtoTg
        return self.RPMtoTg
    
    def setTg(self, Tg=None):
        self.Tg        = Tg
        return self.Tg
    
    def setTsr(self, Tsr=None):
        self.Tsr       = Tsr
        return self.Tsr
    
    def setCp(self, Cp=None):
        self.Cp       = Cp
        return self.Cp
    
    
    
    
if __name__ == '__main__':
    import unittest
    import OpenFile
    
    class test_newobject(unittest.TestCase):
        def test_newThreePhaseShortCircuit(self):
            WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit, eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit = OpenFile.ReadData_ThreePhaseShortCircuit()
            database_ThreePhaseShortCircuit = referencedata(WindSpeed_ThreePhaseShortCircuit, None, eff_g_ThreePhaseShortCircuit, None, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit)
            self.assertIsNotNone(database_ThreePhaseShortCircuit)
        def test_newMaxPower(self):
            RPMtoEffg_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower = OpenFile.ReadData_MaxPower()
            database_MaxPower = referencedata(None, RPMtoEffg_MaxPower, eff_g_MaxPower, None, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower)
            self.assertIsNotNone(database_MaxPower)
        def test_newMaxTorqueCurrent(self):
            RPM__MaxTorqueCurrent, eff_g_MaxTorqueCurrent, eff_e_MaxTorqueCurrent, Tg_MaxTorqueCurrent, Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent = OpenFile.ReadData_MaxTorqueCurrent()
            database_MaxTorqueCurrent = referencedata(None, RPM__MaxTorqueCurrent, eff_g_MaxTorqueCurrent, None, None, None, Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent)
            self.assertIsNotNone(database_MaxTorqueCurrent)    
        
        
        
        
    class test_property(unittest.TestCase):    
#==============================================================================
#         WindSpeed_ThreePhaseShortCircuit
#         [0.0, 4.0, 6.0, 8.0, 10.0, 12.0]
#         eff_g_ThreePhaseShortCircuit
#         [0.0, 0.81, 0.87, 0.9, 0.89, 0.84]
#         eff_e_ThreePhaseShortCircuit
#         None  # 0.9
#         RPM_ThreePhaseShortCircuit
#         [0.0, 20.0, 25.0, 30.0, 35.0, 42.0]
#         Tg_ThreePhaseShortCircuit
#         [0.0, 79.0, 92.0, 101.0, 106.0, 111.0]
#         Tsr_ThreePhaseShortCircuit
#         [0.0, 0.968166667, 2.03315, 3.098133333, 4.163116667, 5.2281, 6.293083333, 7.358066667, 8.42305]
#         Cp_ThreePhaseShortCircuit
#         [0.0, 0.005254767, 0.059455338, 0.185437614, 0.299656442, 0.361849571, 0.363630963, 0.31708412, 0.243355401]
#==============================================================================
        def test_ThreePhaseShortCircuit(self):
            WindSpeed_ThreePhaseShortCircuit, eff_g_ThreePhaseShortCircuit, eff_e_ThreePhaseShortCircuit, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit = OpenFile.ReadData_ThreePhaseShortCircuit()
            database_ThreePhaseShortCircuit = referencedata(WindSpeed_ThreePhaseShortCircuit, None, eff_g_ThreePhaseShortCircuit, None, RPM_ThreePhaseShortCircuit , Tg_ThreePhaseShortCircuit, Tsr_ThreePhaseShortCircuit, Cp_ThreePhaseShortCircuit)
            
            self.assertEquals(database_ThreePhaseShortCircuit.WindSpeed, [0.0, 4.0, 6.0, 8.0, 10.0, 12.0])
            self.assertEquals(database_ThreePhaseShortCircuit.RPMtoEffg, None)
            self.assertEquals(database_ThreePhaseShortCircuit.eff_g, [0.0, 0.81, 0.87, 0.9, 0.89, 0.84])
            self.assertEquals(database_ThreePhaseShortCircuit.eff_e, None)
            
            self.assertEquals(database_ThreePhaseShortCircuit.RPMtoTg, [0.0, 20.0, 25.0, 30.0, 35.0, 42.0])
            self.assertEquals(database_ThreePhaseShortCircuit.Tg, [0.0, 79.0, 92.0, 101.0, 106.0, 111.0])
            
            self.assertEquals(database_ThreePhaseShortCircuit.Tsr, [0.0, 0.968166667, 2.03315, 3.098133333, 4.163116667, 5.2281, 6.293083333, 7.358066667, 8.42305])
            self.assertEquals(database_ThreePhaseShortCircuit.Cp, [0.0, 0.005254767, 0.059455338, 0.185437614, 0.299656442, 0.361849571, 0.363630963, 0.31708412, 0.243355401])





#==============================================================================
#         RPMtoEffg_MaxPower
#         [105.0, 168.0, 217.0, 218.0, 370.0]
#         eff_g_MaxPower
#         [0.81, 0.87, 0.9, 0.89, 0.84]
#         eff_e_MaxPower
#         None # 0.9
#         RPMtoTG_MaxPower
#         [0.0, 105.0, 168.0, 217.0, 281.0, 370.0]
#         Tg_MaxPower
#         [0.0, 14.0, 30.0, 54.0, 83.0, 110.0]
#         Tsr_MaxPower
#         [0.0, 0.968166667, 2.03315, 3.098133333, 4.163116667, 5.2281, 6.293083333, 7.358066667, 8.42305]
#         Cp_MaxPower
#         [0.0, 0.005254767, 0.059455338, 0.185437614, 0.299656442, 0.361849571, 0.363630963, 0.31708412, 0.243355401]       
#==============================================================================
        def test_MaxPower(self):
            RPMtoEffg_MaxPower, eff_g_MaxPower, eff_e_MaxPower, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower = OpenFile.ReadData_MaxPower()
            database_MaxPower = referencedata(None, RPMtoEffg_MaxPower, eff_g_MaxPower, None, RPMtoTG_MaxPower, Tg_MaxPower, Tsr_MaxPower, Cp_MaxPower)
            
            self.assertEquals(database_MaxPower.WindSpeed, None)
            self.assertEquals(database_MaxPower.RPMtoEffg, [105.0, 168.0, 217.0, 218.0, 370.0])
            self.assertEquals(database_MaxPower.eff_g, [0.81, 0.87, 0.9, 0.89, 0.84])
            self.assertEquals(database_MaxPower.eff_e, None)
            
            self.assertEquals(database_MaxPower.RPMtoTg, [0.0, 105.0, 168.0, 217.0, 281.0, 370.0])
            self.assertEquals(database_MaxPower.Tg, [0.0, 14.0, 30.0, 54.0, 83.0, 110.0])
            
            self.assertEquals(database_MaxPower.Tsr, [0.0, 0.968166667, 2.03315, 3.098133333, 4.163116667, 5.2281, 6.293083333, 7.358066667, 8.42305])
            self.assertEquals(database_MaxPower.Cp, [0.0, 0.005254767, 0.059455338, 0.185437614, 0.299656442, 0.361849571, 0.363630963, 0.31708412, 0.243355401])
       
        
        
#==============================================================================
#         RPM__MaxTorqueCurrent
#         [0.0, 90.3968254, 127.5714286, 168.7647059, 210.4054054, 253.75, 295.0, 333.0, 374.516129, 411.5384615, 448.8461538]
#         eff_g_MaxTorqueCurrent
#         [0.0, 0.413315, 0.589179, 0.676737306, 0.73577073, 0.76665125, 0.790547, 0.815694, 0.841986581, 0.84530818, 0.857300539]
#         eff_e_MaxTorqueCurrent
#         None # 0.9
#         Tg_MaxTorqueCurrent
#         None # 110
#         Tsr__MaxTorqueCurrent
#         [0.0, 0.968166667, 2.03315, 3.098133333, 4.163116667, 5.2281, 6.293083333, 7.358066667, 8.42305]
#         Cp_MaxTorqueCurrent
#         [0.0, 0.005254767, 0.059455338, 0.185437614, 0.299656442, 0.361849571, 0.363630963, 0.31708412, 0.243355401]        
#==============================================================================
        def test_MaxTorqueCurrent(self):
            RPM__MaxTorqueCurrent, eff_g_MaxTorqueCurrent, eff_e_MaxTorqueCurrent, Tg_MaxTorqueCurrent, Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent = OpenFile.ReadData_MaxTorqueCurrent()
            database_MaxTorqueCurrent = referencedata(None, RPM__MaxTorqueCurrent, eff_g_MaxTorqueCurrent, None, None, None, Tsr__MaxTorqueCurrent, Cp_MaxTorqueCurrent)
            
            self.assertEquals(database_MaxTorqueCurrent.WindSpeed, None)
            self.assertEquals(database_MaxTorqueCurrent.RPMtoEffg, [0.0, 90.3968254, 127.5714286, 168.7647059, 210.4054054, 253.75, 295.0, 333.0, 374.516129, 411.5384615, 448.8461538])
            self.assertEquals(database_MaxTorqueCurrent.eff_g, [0.0, 0.413315, 0.589179, 0.676737306, 0.73577073, 0.76665125, 0.790547, 0.815694, 0.841986581, 0.84530818, 0.857300539])
            self.assertEquals(database_MaxTorqueCurrent.eff_e, None)
            
            self.assertEquals(database_MaxTorqueCurrent.RPMtoTg, None)
            self.assertEquals(database_MaxTorqueCurrent.Tg, None)
            
            self.assertEquals(database_MaxTorqueCurrent.Tsr, [0.0, 0.968166667, 2.03315, 3.098133333, 4.163116667, 5.2281, 6.293083333, 7.358066667, 8.42305])
            self.assertEquals(database_MaxTorqueCurrent.Cp, [0.0, 0.005254767, 0.059455338, 0.185437614, 0.299656442, 0.361849571, 0.363630963, 0.31708412, 0.243355401])

        
    unittest.main()
    
    