from numpy import*
import matplotlib.pyplot as plt

def PaintDiagram(str_name, str_ylabel_1,  str_ylabel_2,  str_ylabel_3, x, isPaint_WindSpeed, y1, isPaint_RPM, y2, isPaint_Power, y3):

    plt.figure(figsize=(16,9)) #(dpi  (16*80)*(9*80) = 1240*720)
    
    
    y1X100 = [i*100 for i in y1]
    y2X10  = [i*10 for i in y2]
    
    
    plt.xlim(min(x), max(x))
    plt.ylim(min(min(y1X100), min(y2X10), min(y3)),max(max(y1X100), max(y2X10), max(y3)))
    
    plt.title(str_name)
    
    if isPaint_WindSpeed is True:
        plt.plot(x, y1X100, label = str_ylabel_1, color='g')
        str_ylabel_1 = str_ylabel_1 + " X 100" + "\n"
    else:
        str_ylabel_1 =""
        
    if isPaint_RPM is True:
        plt.plot(x, y2X10, label = str_ylabel_2, color='b')
        str_ylabel_2 = str_ylabel_2 + "      X 10" +"\n"
    else:
        str_ylabel_2 = ""
    if isPaint_Power is True:
        plt.plot(x, y3, label = str_ylabel_3, color='r')
        str_ylabel_3 = str_ylabel_3 +"\n"
    else:
        str_ylabel_3 = ""
    plt.xlabel("Time(s)")
    plt.ylabel(str_ylabel_1 + str_ylabel_2 + str_ylabel_3)
    
    
    plt.legend(loc=2)
    plt.show()
    