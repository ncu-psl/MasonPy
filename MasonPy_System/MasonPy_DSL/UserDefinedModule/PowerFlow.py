from BasicModule.Mode import*

class threePhaseData_original(originalMode):
    def setInit(self):
        self.par = []
        self.par.append(['Vg1', None])
        
        self.par.append(['Pg2', None])
        self.par.append(['Qg2', None])
        self.par.append(['theta2', None])
        self.par.append(['Vg2_abs',None])
        
        self.par.append(['Vg2_temp',None]) # 疊代初值
        
        
        self.par.append(['P3', None])
        self.par.append(['Q3', None])
        self.par.append(['theta3', None])
        self.par.append(['V3_abs',None])
        
        self.par.append(['V3_temp', None]) # 疊代初值
        
        self.par.append(['Line12', None])
        self.par.append(['Line23', None])
        self.par.append(['Line13', None])
        self.par.append(['Llist', None])
        
        self.par.append(['Y12', None])
        self.par.append(['Y23', None])
        self.par.append(['Y13', None])
        
        self.par.append(['Z12', None])
        self.par.append(['Z23', None])
        self.par.append(['Z13', None])
        
        self.par.append(['Ybus', None])
        
        
        
        self.setInitValue(self.par)
        
        
        
        

    
    def do(self):
        self.Llist = [self.Line12, self.Line23, self.Line13]
        print(self.AllVariables)


    def copyValue(self):
        self.Vg1 = self.lastMode.Vg1
        
        self.Pg2 = self.lastMode.Pg2
        self.Qg2 = self.lastMode.Qg2
        self.theta2 = self.lastMode.theta2
        self.Vg2_abs = self.lastMode.Vg2_abs
        
        self.Vg2_temp = self.lastMode.Vg2_temp # 疊代初值
        
        
        self.P3 = self.lastMode.P3
        self.Q3 = self.lastMode.Q3
        self.theta3 = self.lastMode.theta3
        self.V3_abs = self.lastMode.V3_abs
        
        self.V3_temp = self.lastMode.V3_temp # 疊代初值
        
        self.Line12 = self.lastMode.Line12
        self.Line23 = self.lastMode.Line23
        self.Line13 = self.lastMode.Line13
        self.Llist = self.lastMode.Llist
        
        self.Y12 = self.lastMode.Y12
        self.Y23 = self.lastMode.Y23
        self.Y13 = self.lastMode.Y13
        
        self.Z12 = self.lastMode.Z12
        self.Z23 = self.lastMode.Z23
        self.Z13 = self.lastMode.Z13
        
        self.Ybus = self.lastMode.Ybus
    
class threePhaseData_Z(threePhaseData_original):
#==============================================================================
#     def setInit(self):
#         par = []
#         par.append(['Vg1', 1])
#         
#         par.append(['Pg2', 1])
#         par.append(['Qg2', None])
#         par.append(['theta2', None])
#         par.append(['Vg_abs2',1])
#         
#         par.append(['Vg_2',1]) # 疊代初值
#         
#         
#         par.append(['P3', 1.5])
#         par.append(['Q3', 0.8j])
#         par.append(['theta3', None])
#         par.append(['V_abs3',None])
#         
#         par.append(['V_3',1]) # 疊代初值
#         
#         par.append(['Line12', 0.2j])
#         par.append(['Line23', 0.25j])
#         par.append(['Line13', 0.1j])
#         par.append(['Llist', None])
#         
#         self.setInitValue(par)
#==============================================================================

    def do(self):
        self.Vg1 = 1
         
        self.Pg2 = 1
        self.Vg2_abs =1
         
#        self.Vg_2temp = 1 # 疊代初值
         
         
        self.P3 = 1.5
        self.Q3 = 0.8j

         
#        self.V_3temp =1 # 疊代初值
         
        self.Line12 = 0.2j
        self.Line23 = 0.25j
        self.Line13 = 0.1j
        self.Llist = [self.Line12, self.Line23, self.Line13]
        
        
        
class threePhaseData_Y(threePhaseData_original):
#==============================================================================
#     def setInit(self):
#         par = []
#         par.append(['Vg1', 1.02])
#         
#         par.append(['Pg2', 0.7])
#         par.append(['Qg2', None])
#         par.append(['theta2', None])
#         par.append(['Vg_abs2',1.01])
#         
#         par.append(['P3', 0.9])
#         par.append(['Q3', 0.8j])
#         par.append(['theta3', None])
#         par.append(['Vg_abs3',None])
#         
#         par.append(['Line12', -0j])
#         par.append(['Line23', -12j])
#         par.append(['Line13', -8j])
#         par.append(['Llist', None])
#         
#         self.setInitValue(par)
#==============================================================================

    
    def do(self):
        self.Vg1 = 1.02
         
        self.Pg2 = 0.7
        self.Vg2_abs = 1.01
         
#        self.Vg2_temp =1 # 疊代初值
         
         
        self.P3 = 0.9
        self.Q3 = 0.8j

         
#        self.V3_temp =1 # 疊代初值
         
        self.Line12 = -0j
        self.Line23 = -12j
        self.Line13 = -8j
        self.Llist = [self.Line12, self.Line23, self.Line13]
        print('Llist', self.Llist)
          
        
if __name__=='__main__':
    a = threePhaseData_Z()
    a.do()
    print(a.AllVariables)
    print(a.getValue(a, 'Vg1'))
    
    print(a.getValue(a, 'Pg2'))
    print(a.getValue(a, 'Vg2_abs'))
    
    print(a.getValue(a, 'P3'))
    print(a.getValue(a, 'Q3'))
    
    print(a.getValue(a, 'Llist'))



