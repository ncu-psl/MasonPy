from numpy import*
import matplotlib.pyplot as plt

def PaintDiagram(str_name, str_xlabel, str_ylabel_1,  str_ylabel_2,  str_ylabel_3, x, isPaint_WindSpeed, y1, isPaint_RPM, y2, isPaint_Power, y3):

    y2X10  = [i*10 for i in y2]
    
    fig, ax1 = plt.subplots(figsize=(16,9)) #(dpi  (16*80)*(9*80) = 1240*720)
    if isPaint_RPM is True:
        ax1.plot(x, y2X10, label = str_ylabel_2, color='b')
        str_ylabel_2 = str_ylabel_2 + "     X  10" + "\n"
    else:
        str_ylabel_2 = ""
        
    if isPaint_Power is True:
        ax1.plot(x, y3, label = str_ylabel_3, color='r')
        str_ylabel_3 = str_ylabel_3 + "\n"
    else:
        str_ylabel_3 = ""
    
    
    ax1.set_title(str_name)
    ax1.set_ylim(min(min(y2X10), min(y3)),max(max(y2X10), max(y3)))
    ax1.set_xlabel(str_xlabel)
    ax1.set_ylabel(str_ylabel_2 + str_ylabel_3)
    ax1.legend(loc=2) # upper left
    ax1.set_xlim(min(x), max(x))
    
    if isPaint_WindSpeed is True:  
        ax2 = ax1.twinx()
        ax2.plot(x, y1, label = str_ylabel_1, color='g')
        ax2.set_xlim(min(x), max(x))
        ax2.set_ylim(min(y1),max(y1))
        ax2.set_ylabel(str_ylabel_1)
        ax2.legend(loc=1) # upper right
    
    
    
    plt.savefig("filename.png")
    return fig
    #plt.show()
    