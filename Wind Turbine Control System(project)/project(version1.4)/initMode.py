import Mode
import dataformat

class Mode_init(Mode):
    def __init__(self , LastMode=None, database = dataformat.referencedata(), WindSpeed):
        self.MaxWindSpeed_ThreePhaseShortCircuit = 8
        self.CurrentTime     = 1
        self.TimeDelta       = 0.01
        self.MonmentIntertia = 0.7
        self.CutOutRPM       = 400
        self.CutOutPower     = 3300
        self.MaxMagBrake     = 42
        self.Rho             = 1.293
        self.D               = 3.7
        self.A               = self.D**2 * pi
        self.TorqueMachine   = 175
        
        self.WindSpeed    = 0
        self.mode         = 'initial'
        self.Tsr          = 0
        self.Cp           = 0
        self.Tb           = 0
        self.Tg           = 0
        self.Tm           = 0
        self.Tt           = 0 
        self.eff_g        = 0
        self.eff_e        = 0.9
        self.CurrentTime  = 0
        self.RPM          = 0.0001
        self.power        = 0