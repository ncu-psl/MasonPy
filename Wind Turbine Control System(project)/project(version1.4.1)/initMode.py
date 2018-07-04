from numpy import*
from Mode import*
from Databaseformat import*


class Mode_init(originalMode):
    def __init__(self, LastMode=None, database = referencedata(), WindSpeed=0):
        self.MaxWindSpeed_ThreePhaseShortCircuit = 8
        self.TimeDelta       = 0.01
        self.MonmentIntertia = 0.7
        self.CutOutRPM       = 400
        self.CutOutPower     = 3300
        self.MaxMagBrake     = 42
        self.Rho             = 1.293
        self.D               = 3.7
        self.A               = ((self.D)/2)**2 * pi
        self.TorqueMachine   = 175
        
        self.CurrentTime  = 0
        self.WindSpeed    = 0
        self.mode         = self.namemode('initial')
        self.Tsr          = 0
        self.Cp           = 0
        self.Tb           = 0
        self.Tg           = 0
        self.Tm           = 0
        self.Tt           = 0 
        self.eff_g        = 0
        self.eff_e        = 0.9
        self.RPM          = 0.0001
        self.power        = 0
 





if __name__ == '__main__':       
    import unittest

    class test(unittest.TestCase):
        def test_newobject(self):
            init = Mode_init()
            self.assertIsNotNone(init)
        
        def test_Property(self):
            init = Mode_init()
            self.assertEquals(init.MaxWindSpeed_ThreePhaseShortCircuit, 8)
            self.assertEquals(init.TimeDelta, 0.01)
            self.assertEquals(init.MonmentIntertia, 0.7)
            self.assertEquals(init.CutOutRPM, 400)
            self.assertEquals(init.CutOutPower, 3300)
            self.assertEquals(init.MaxMagBrake, 42)
            self.assertEquals(init.Rho, 1.293)
            self.assertEquals(init.D, 3.7)
            self.assertEquals(init.A, (3.7/2)**2*pi)
            self.assertEquals(init.TorqueMachine, 175)

            self.assertEquals(init.CurrentTime, 0)
            self.assertEquals(init.WindSpeed, 0)
            self.assertIs(init.mode, 'initial')
            self.assertEquals(init.Tsr, 0)
            self.assertEquals(init.Cp, 0)
            self.assertEquals(init.Tb, 0)
            self.assertEquals(init.Tg, 0)
            self.assertEquals(init.Tm, 0)
            self.assertEquals(init.eff_g, 0)
            self.assertEquals(init.eff_e, 0.9)
            self.assertEquals(init.RPM, 0.0001)
            self.assertEquals(init.power, 0)

    unittest.main()










