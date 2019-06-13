from BasicModule.Mode import*
from UserDefinedModule.PowerFlow import*

class YtoYbus(threePhaseData_original):

    
#==============================================================================
#     def setInit(self): # 2
#         par = []
#         par.append(['Y12', None])
#         par.append(['Y23', None])
#         par.append(['Y13', None])
#         par.append(['Ybus', None])
#         self.setInitValue(par)
#==============================================================================
    
    
    def do(self):
        self.copyValue()
        self.CalYbus()
        print('Ybus',self.Ybus)
    
    def CalYbus(self):
        
        self.Y12 = self.lastMode.Llist[0]
        self.Y23 = self.lastMode.Llist[1]
        self.Y13 = self.lastMode.Llist[2]
        
        self.Y11 = (self.Y12+self.Y13)
        self.Y22 = (self.Y12+self.Y23)
        self.Y33 = (self.Y13+self.Y23)
        self.Ybus=[[self.Y11,-1*self.Y12,-1*self.Y13],[-1*self.Y12,self.Y22,-1*self.Y23],[-1*self.Y13,-1*self.Y23,self.Y33]]
    
        
        
class ZtoYbus(YtoYbus):    # 1
#==============================================================================
#     def setInit(self):
#         par = []
#         par.append(['Z12', None])
#         par.append(['Z23', None])
#         par.append(['Z13', None])
#         par.append(['Ybus', None])
#         self.setInitValue(par)
#         print(par)
#==============================================================================
    def setintro(self):
        info = 'Calculate the Ybus Matrix.\n'
        info = info + ' I Matrix * Ybus Matrix = V Matrix \n' 
        info = info + 'I1=(-1/Z12)*(V1-V2)+(-1/Z13)*(V1-V2)\n'+'I2=(-1/Z12)*(V2-V1)+(-1/Z23)*(V2-V3)\n'+'I3=(-1/Z13)*(V3-V1)+(-1/Z23)*(V3-V2)\n'
        self.intro_str = info
        
    def do(self):
        self.copyValue()
        self.CalYbus()
        print('Ybus',self.Ybus)
       

    
    def CalYbus(self):
        
        self.Z12 = self.lastMode.Llist[0]
        self.Z23 = self.lastMode.Llist[1]
        self.Z13 = self.lastMode.Llist[2]
        
        self.Z11 = 1/(1/self.Z12+1/self.Z13)
        self.Z22 = 1/(1/self.Z12+1/self.Z23)
        self.Z33 = 1/(1/self.Z13+1/self.Z23)
        self.Ybus=[[1/self.Z11,-1/self.Z12,-1/self.Z13],[-1/self.Z12,1/self.Z22,-1/self.Z23],[-1/self.Z13,-1/self.Z23,1/self.Z33]]
    
     
        
          
        
if __name__=='__main__':
    a = YtoYbus()
    a.do()
    print(a.AllVariables)
    print(a.getValue(a, 'Y12'))
    print(a.getValue(a, 'Y23'))
    print(a.getValue(a, 'Y13'))
    print(a.getValue(a, 'Ybus'))
    
    b = ZtoYbus()
    b.do()
    print(b.AllVariables)
    print(b.getValue(a, 'Z12'))
    print(b.getValue(a, 'Z23'))
    print(b.getValue(a, 'Z13'))
    print(b.getValue(a, 'Ybus'))
    


