class referencedata(object):
    def __init__(self, WindSpeed=None, RPMtoEffg=None, eff_g=None, eff_e=None, RPMtoTg=None, Tg=None, Tsr=None, Cp=None):
        self.WindSpeed = WindSpeed
        self.RPMtoEffg = RPMtoEffg
        self.eff_g     = eff_g
        self.eff_e     = eff_e
        
        self.RPMtoTg       = RPMtoTg
        self.Tg        = Tg
        
        self.Tsr       = Tsr
        self.Cp        = Cp
        
    def setWindSpeed(self, WindSpeed):
        self.WindSpeed = WindSpeed
        return self.WindSpeed
    
    def setRPMtoEffg(self, RPMtoEffg):
        self.RPMtoEffg   = RPMtoEffg
        return self.RPMtoEffg
    
    def setEff_g(self, eff_g):
        self.eff_g     = eff_g
        return self.eff_g
    
    def setEff_e(self, eff_e):
        self.eff_e     = eff_e
        return self.eff_e
    
    def setRPMtoTg(self, RPMtoTg):
        self.RPMtoTg   = RPMtoTg
        return self.RPMtoTg
    
    def setTg(self, Tg):
        self.Tg        = Tg
        return self.Tg
    
    def setTsr(self, Tsr):
        self.Tsr       = Tsr
        return self.Tsr
    
    def setCp(self, Cp):
        self.Cp       = Cp
        return self.Cp
    
    
    
    
if __name__ == '__main__':
    def testnewobject():
        database = referencedata()
        print('database', database)
        print('Tsr', database.Tsr)
    

    testnewobject()
    
    