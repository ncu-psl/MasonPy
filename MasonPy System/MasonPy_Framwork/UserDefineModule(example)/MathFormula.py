from BasicModule.Mode import*
from math import*

class HeronFormula(originalMode):

    def setintro(self):
        info = '海龍公式\n'
        info = info + '三角形三邊長(A、B、C),求三角形面積Area=? \n'
        info = info + 'S = (A+B+C)/2 \n'
        info = info + 'Area = √(s(s−a)(s−b)(s−c)) \n'
        self.intro_str = info
        
    
    def setInit(self):
        self.setInitValue([['A', 5], ['B', 12], ['C',13],['Area',None]])
    

    def do(self):
        self.CalArea()

        
    def CalArea(self):
        S = (self.A+self.B+self.C)/2
        if self.A <= 0 or self.B <= 0 or self.C <= 0:
            self.Area = None
        else:
            self.Area = sqrt(S*(S-self.A)*(S-self.B)*(S-self.C))
        
          
        
if __name__=='__main__':
    a = HeronFormula()
    a.do()
    print(a.AllVariables)
    print(a.getValue(a, 'A'))
    print(a.getValue(a, 'B'))
    print(a.getValue(a, 'C'))
    print(a.getValue(a, 'Area'))