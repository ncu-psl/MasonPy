from BasicModule.Mode import*
from UserDefinedModule.PowerFlow import*
from math import*
from numpy import*

class Gauss_Seidel(threePhaseData_original):
    
    def do(self):
        self.copyValue()
        self.setV_init()
        
        self.CalV3()
        self.CalV2()
        print('V3_temp',self.V3_temp)
        print('Vg2_temp',self.Vg2_temp)
        
    def setV_init(self):
        if self.lastMode.Vg2_temp == None:
            self.Vg2_temp = 1 # 疊代初值   
        if self.lastMode.V3_temp == None:
            self.V3_temp = 1 # 疊代初值
    
    def CalV3(self): 
        self.V3_temp = (-1*(self.P3-self.Q3)/self.V3_temp-self.Ybus[0][2]*self.Vg1-self.Ybus[1][2]*self.Vg2_temp)/self.Ybus[2][2]
        self.V3_abs = self.V3_temp.real
        self.theta3 = atan(self.V3_temp.imag/self.V3_temp.real) # *180/pi
    
    def CalV2(self):
        Stemp = -(self.Vg2_temp*(self.Vg1*self.Ybus[0][1]+self.Vg2_temp*self.Ybus[1][1]+self.V3_temp*self.Ybus[2][1]))
        self.Qg2 = 1j * Stemp.imag
        self.Vg2_temp = ((self.Pg2-self.Qg2)/self.Vg2_temp-self.Ybus[0][1]*self.Vg1-self.Ybus[1][2]*self.V3_temp)/self.Ybus[1][1]
        self.theta2 = atan(self.Vg2_temp.imag/self.Vg2_temp.real)
        self.Vg2_temp = self.Vg2_abs*cos(self.theta2) + 1j*self.Vg2_abs*sin(self.theta2)
        
          
        
if __name__=='__main__':
    a = Gauss_Seidel()
    a.do()
