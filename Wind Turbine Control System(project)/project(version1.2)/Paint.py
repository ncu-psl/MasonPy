from numpy import*
import matplotlib.pyplot as plt

def PaintDiagram(str_name, str_ylabel, x, y):

    plt.figure(figsize=(16,9)) #(dpi  (16*80)*(9*80) = 1240*720)
    
    plt.xlim(min(x),max(x))
    plt.ylim(min(y),max(y))
    
    plt.xlabel("Time(s)")
    plt.ylabel(str_ylabel)
    plt.title(str_name)
    plt.plot(x,y)
    
    plt.show()