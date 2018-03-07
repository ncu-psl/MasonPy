# -*- coding: utf-8 -*-
import xlwt
from numpy import*

import OpenFile
    


def ExportExcelData(TimeSeries, WindSpeed, RPM, Power, Cp, eff_g, Mode):
 
    setting_row      = 0
    
    number_column    = 0  # A Field
    Time_column      = 1  # B Field 
    WindSpeed_column = 2  # C Field
    RPM_column       = 3  # D Field
    Power_column     = 4  # E Field
    Cp_column        = 5  # F Field
    effg_column      = 6  # G Field
    Mode_column      = 7  # H Field
    
    
    
    
    
    book = xlwt.Workbook(encoding="utf-8")    
    sheet1 = book.add_sheet("number 1~50,000")
    sheet1.write(setting_row, number_column, "number")            
    sheet1.write(setting_row, Time_column, "Time (ms)")     
    sheet1.write(setting_row, WindSpeed_column, "WindSpeed (m/s)")   
    sheet1.write(setting_row, RPM_column, "RPM")            
    sheet1.write(setting_row, Power_column, "Power (W)")   
    sheet1.write(setting_row, Cp_column, "Cp")            
    sheet1.write(setting_row, effg_column, "eff_g")
    sheet1.write(setting_row, Mode_column, "mode")     
    
    sheet2 = book.add_sheet("number 50,001~100,000")
    sheet2.write(setting_row, number_column, "number")         
    sheet2.write(setting_row, Time_column, "Time (ms)")       
    sheet2.write(setting_row, WindSpeed_column, "WindSpeed (m/s)")   
    sheet2.write(setting_row, RPM_column, "RPM")            
    sheet2.write(setting_row, Power_column, "Power (W)")  
    sheet2.write(setting_row, Cp_column, "Cp")            
    sheet2.write(setting_row, effg_column, "eff_g")     
    sheet2.write(setting_row, Mode_column, "mode")     
    
    sheet3 = book.add_sheet("number 100,001~150,000")
    sheet3.write(setting_row, number_column, "number")         
    sheet3.write(setting_row, Time_column, "Time (ms)")      
    sheet3.write(setting_row, WindSpeed_column, "WindSpeed (m/s)") 
    sheet3.write(setting_row, RPM_column, "RPM")          
    sheet3.write(setting_row, Power_column, "Power (W)")  
    sheet3.write(setting_row, Cp_column, "Cp")            
    sheet3.write(setting_row, effg_column, "eff_g")
    sheet3.write(setting_row, Mode_column, "mode")        
    
    sheet4 = book.add_sheet("number 150,001~200,000")
    sheet4.write(setting_row, number_column, "number")     
    sheet4.write(setting_row, Time_column, "Time (ms)")      
    sheet4.write(setting_row, WindSpeed_column, "WindSpeed (m/s)") 
    sheet4.write(setting_row, RPM_column, "RPM")              
    sheet4.write(setting_row, Power_column, "Power (W)")     
    sheet4.write(setting_row, Cp_column, "Cp")            
    sheet4.write(setting_row, effg_column, "eff_g")
    sheet4.write(setting_row, Mode_column, "mode")     
    
    sheet5 = book.add_sheet("number 200,001~250,000")
    sheet5.write(setting_row, number_column, "number")       
    sheet5.write(setting_row, Time_column, "Time (ms)")        
    sheet5.write(setting_row, WindSpeed_column, "WindSpeed (m/s)")  
    sheet5.write(setting_row, RPM_column, "RPM")            
    sheet5.write(setting_row, Power_column, "Power (W)")      
    sheet5.write(setting_row, Cp_column, "Cp")            
    sheet5.write(setting_row, effg_column, "eff_g")
    sheet5.write(setting_row, Mode_column, "mode")        
    
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
            sheet1.write(i, number_column, n+1)
            sheet1.write(i, Time_column, round(TimeSeries[n], 5))
            sheet1.write(i, WindSpeed_column, round(WindSpeed[n], 5))
            sheet1.write(i, RPM_column, round(RPM[n], 5))
            sheet1.write(i, Power_column, round(Power[n], 5))
            sheet1.write(i, Cp_column, round(Cp[n], 5))
            sheet1.write(i, effg_column, round(eff_g[n], 5))
            sheet1.write(i, Mode_column, Mode[n])
        elif n < NumberofSheet*2:
            i = i+1
            sheet2.write(i, number_column, n+1)
            sheet2.write(i, Time_column, round(TimeSeries[n], 5))
            sheet2.write(i, WindSpeed_column, round(WindSpeed[n], 5))
            sheet2.write(i, RPM_column, round(RPM[n], 5))
            sheet2.write(i, Power_column, round(Power[n], 5))
            sheet2.write(i, Cp_column, round(Cp[n], 5))
            sheet2.write(i, effg_column, round(eff_g[n], 5))
            sheet2.write(i, Mode_column, Mode[n])
        elif n < NumberofSheet*3:
            i = i+1
            sheet3.write(i, number_column, n+1)
            sheet3.write(i, Time_column, round(TimeSeries[n], 5))
            sheet3.write(i, WindSpeed_column, round(WindSpeed[n], 5))
            sheet3.write(i, RPM_column, round(RPM[n], 5))
            sheet3.write(i, Power_column, round(Power[n], 5))
            sheet3.write(i, Cp_column, round(Cp[n], 5))
            sheet3.write(i, effg_column, round(eff_g[n], 5))
            sheet3.write(i, Mode_column, Mode[n])
        elif n < NumberofSheet*4:
            i = i+1
            sheet4.write(i, number_column, n+1)
            sheet4.write(i, Time_column, round(TimeSeries[n], 5))
            sheet4.write(i, WindSpeed_column, round(WindSpeed[n], 5))
            sheet4.write(i, RPM_column, round(RPM[n], 5))
            sheet4.write(i, Power_column, round(Power[n], 5))
            sheet4.write(i, Cp_column, round(Cp[n], 5))
            sheet4.write(i, effg_column, round(eff_g[n], 5))
            sheet4.write(i, Mode_column, Mode[n])
        elif n < NumberofSheet*5:
            i = i+1
            sheet5.write(i, number_column, n+1)
            sheet5.write(i, Time_column, round(TimeSeries[n], 5))
            sheet5.write(i, WindSpeed_column, round(WindSpeed[n], 5))
            sheet5.write(i, RPM_column, round(RPM[n], 5))
            sheet5.write(i, Power_column, round(Power[n], 5))
            sheet5.write(i, Cp_column, round(Cp[n], 5))
            sheet5.write(i, effg_column, round(eff_g[n], 5))
            sheet5.write(i, Mode_column, Mode[n])
        else:
             print("error : More than 200,000 documents")
            
            
            
        
    book.save("output.xls")





if __name__=='__main__':
    
    ExportExcelData()
    