# -*- coding: utf-8 -*-
import xlwt

def ExportExcelData():
    book = xlwt.Workbook(encoding="utf-8")    
    sheet1 = book.add_sheet("Sheet 1")
    
    sheet1.write(0, 0, "Time (ms)")         #sheet1.write(0, A, "Time (ms)")
    sheet1.write(0, 1, "WindSpeed (m/s)")   #sheet1.write(0, B, "WindSpeed (m/s)")
    sheet1.write(0, 2, "RPM")               #sheet1.write(0, C, "RPM")
    sheet1.write(0, 3, "Power (W)")         #sheet1.write(0, D, "Power (W)")
    sheet1.write(0, 4, "mode")              #sheet1.write(0, E, "mode")
    
    
#==============================================================================
#     i=1
#     
#     for n in size(TimeSeries):
#         i = i+1
#         sheet1.write(i, 0, TimeSeries[n])
#         sheet1.write(i, 1, WindSpeed[n])
#==============================================================================
    book.save("output.xls")





if __name__=='__main__':
    ExportExcelData()
    