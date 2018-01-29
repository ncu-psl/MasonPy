# -*- coding: utf-8 -*-
import xlwt
from numpy import*

import OpenFile
    


def ExportExcelData(TimeSeries, WindSpeed, RPM, Power, Mode):
 
    book = xlwt.Workbook(encoding="utf-8")    
    sheet1 = book.add_sheet("number 1~50,000")
    sheet1.write(0, 0, "number")            #sheet1.write(0, A, "Time (ms)")
    sheet1.write(0, 1, "Time (ms)")         #sheet1.write(0, B, "Time (ms)")
    sheet1.write(0, 2, "WindSpeed (m/s)")   #sheet1.write(0, C, "WindSpeed (m/s)")
    sheet1.write(0, 3, "RPM")               #sheet1.write(0, D, "RPM")
    sheet1.write(0, 4, "Power (W)")         #sheet1.write(0, E, "Power (W)")
    sheet1.write(0, 5, "mode")              #sheet1.write(0, F, "mode")
    
    sheet2 = book.add_sheet("number 50,001~100,000")
    sheet2.write(0, 0, "number")            #sheet1.write(0, A, "Time (ms)")
    sheet2.write(0, 1, "Time (ms)")         #sheet1.write(0, B, "Time (ms)")
    sheet2.write(0, 2, "WindSpeed (m/s)")   #sheet1.write(0, C, "WindSpeed (m/s)")
    sheet2.write(0, 3, "RPM")               #sheet1.write(0, D, "RPM")
    sheet2.write(0, 4, "Power (W)")         #sheet1.write(0, E, "Power (W)")
    sheet2.write(0, 5, "mode")              #sheet1.write(0, F, "mode")
    
    sheet3 = book.add_sheet("number 100,001~150,000")
    sheet3.write(0, 0, "number")            #sheet1.write(0, A, "Time (ms)")
    sheet3.write(0, 1, "Time (ms)")         #sheet1.write(0, B, "Time (ms)")
    sheet3.write(0, 2, "WindSpeed (m/s)")   #sheet1.write(0, C, "WindSpeed (m/s)")
    sheet3.write(0, 3, "RPM")               #sheet1.write(0, D, "RPM")
    sheet3.write(0, 4, "Power (W)")         #sheet1.write(0, E, "Power (W)")
    sheet3.write(0, 5, "mode")              #sheet1.write(0, F, "mode")
    
    sheet4 = book.add_sheet("number 150,001~200,000")
    sheet4.write(0, 0, "number")            #sheet1.write(0, A, "Time (ms)")
    sheet4.write(0, 1, "Time (ms)")         #sheet1.write(0, B, "Time (ms)")
    sheet4.write(0, 2, "WindSpeed (m/s)")   #sheet1.write(0, C, "WindSpeed (m/s)")
    sheet4.write(0, 3, "RPM")               #sheet1.write(0, D, "RPM")
    sheet4.write(0, 4, "Power (W)")         #sheet1.write(0, E, "Power (W)")
    sheet4.write(0, 5, "mode")              #sheet1.write(0, F, "mode")
    
    sheet5 = book.add_sheet("number 200,001~250,000")
    sheet5.write(0, 0, "number")            #sheet1.write(0, A, "Time (ms)")
    sheet5.write(0, 1, "Time (ms)")         #sheet1.write(0, B, "Time (ms)")
    sheet5.write(0, 2, "WindSpeed (m/s)")   #sheet1.write(0, C, "WindSpeed (m/s)")
    sheet5.write(0, 3, "RPM")               #sheet1.write(0, D, "RPM")
    sheet5.write(0, 4, "Power (W)")         #sheet1.write(0, E, "Power (W)")
    sheet5.write(0, 5, "mode")              #sheet1.write(0, F, "mode")
    
    NumberofSheet = 50000
    
#==============================================================================
#     i=1
#     for n in range(size(TimeSeries)):       
#         i = i+1
#         sheet1.write(i, 0, n)
#         sheet1.write(i, 1, TimeSeries[n])    
#         sheet1.write(i, 2, WindSpeed[n])
#         
#         if n == 50000:
#             break
#==============================================================================
    
    i = 1
    for n in range(0, size(TimeSeries)):
        if n % NumberofSheet == 0:
            i = 1
            
        if n < NumberofSheet:
            i = i+1
            sheet1.write(i, 0, n)
            sheet1.write(i, 1, round(TimeSeries[n], 5))
            sheet1.write(i, 2, round(WindSpeed[n], 5))
            sheet1.write(i, 3, round(RPM[n], 5))
            sheet1.write(i, 4, round(Power[n], 5))
            sheet1.write(i, 5, Mode[n])
        elif n < NumberofSheet*2:
            i = i+1
            sheet2.write(i, 0, n)
            sheet2.write(i, 1, round(TimeSeries[n], 5))
            sheet2.write(i, 2, round(WindSpeed[n], 5))
            sheet2.write(i, 3, round(RPM[n], 5))
            sheet2.write(i, 4, round(Power[n], 5))
            sheet2.write(i, 5, Mode[n])
        elif n < NumberofSheet*3:
            i = i+1
            sheet3.write(i, 0, n)
            sheet3.write(i, 1, round(TimeSeries[n], 5))
            sheet3.write(i, 2, round(WindSpeed[n], 5))
            sheet3.write(i, 3, round(RPM[n], 5))
            sheet3.write(i, 4, round(Power[n], 5))
            sheet3.write(i, 5, Mode[n])
        elif n < NumberofSheet*4:
            i = i+1
            sheet4.write(i, 0, n)
            sheet4.write(i, 1, round(TimeSeries[n], 5))
            sheet4.write(i, 2, round(WindSpeed[n], 5))
            sheet4.write(i, 3, round(RPM[n], 5))
            sheet4.write(i, 4, round(Power[n], 5))
            sheet4.write(i, 5, Mode[n])
        elif n < NumberofSheet*5:
            i = i+1
            sheet5.write(i, 0, n)
            sheet5.write(i, 1, round(TimeSeries[n], 5))
            sheet5.write(i, 2, round(WindSpeed[n], 5))
            sheet5.write(i, 3, round(RPM[n], 5))
            sheet5.write(i, 4, round(Power[n], 5))
            sheet5.write(i, 5, Mode[n])
        else:
             print("error : More than 200,000 documents")
            
            
            
        
    book.save("output.xls")





if __name__=='__main__':
    
    ExportExcelData()
    