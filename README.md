***
# MasonPy-System
***
## 簡介
本研究為一套流程圖式特定領域語言。

[摘要](https://github.com/ncu-psl/MasonPy-System/wiki)

***
## MasonPy 架構
[MasonPy 架構](https://github.com/ncu-psl/MasonPy-System/wiki/MasonPy-%E6%9E%B6%E6%A7%8B)
***
## 程式語言
Python
***
## 下載及操作
下載MasonPy-System中的MasonPy_DSL及MasonPy_Framwork兩個檔案，MasonPy_DSL的GUI.py為主程式，MasonPy System/MasonPy_Framwork/UserDefineModule(example)為範例自定義功能塊。
***
## 流程圖基本功能塊簡介
[流程圖功能塊簡介](https://github.com/ncu-psl/MasonPy-System/wiki/%E6%B5%81%E7%A8%8B%E5%9C%96DSL-%E5%8A%9F%E8%83%BD%E5%A1%8A-%E7%B0%A1%E4%BB%8B)
***
## MasonPy DSL 指令說明及範例
[DSL 指令說明及範例](https://github.com/ncu-psl/MasonPy-System/wiki/MasonPy-DSL-%E6%8C%87%E4%BB%A4%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%AF%84%E4%BE%8B)
***
## 自定義領域功能塊
[自定義領域功能塊方法](https://github.com/ncu-psl/MasonPy-System/wiki/%E5%8A%9F%E8%83%BD%E5%A1%8A-%E8%87%AA%E5%AE%9A%E7%BE%A9)
***
## MasonPy Debugger 簡介
[Debugger](https://github.com/ncu-psl/MasonPy-System/wiki/Debugger-%E7%B0%A1%E4%BB%8B)
***
***
***
# 用於繪製風力發電控制邏輯之特定領域語言
***
## 簡介
此特定領域語言是基於MasonPy所擴增的一組風力發電相關的DSL  
此DSL有6個功能塊，Init、MaxPower、MaxTorqueCurrent、ThreePhaseShortCircuit、MaxTorqueCurrent_MagBrake、ThreePhaseShortCircuit_MagBrake 
***
## 下載與操作
1.下載MasonPy System中的MasonPy_Framwork及WindTurbine_DSL資料夾，將WindTurbine_DSL中的檔案與資料夾放入MasonPy_Framwork資料夾，再將MasonPy_Framwork中的UserDefineModule(example)資料夾刪除。  
  
2.打開SetModule.py，將第51行TEST = ['testMode','HeronFormula']跟第61行AllClass.extend(TEST)刪除，再將第51行的UserdefinedClass的內容用下列列表取代['Mode_Init', 'Mode_ThreePhaseShortCircuit', 'Mode_ThreePhaseShortCircuit_MagBrake', 'Mode_MaxPower', 'Mode_MaxTorqueCurrent', 'Mode_MaxTorqueCurrent_MagBrake']。  
  
3.執行GUI.py就可使用，[範例GUI使用說明](https://github.com/ncu-psl/MasonPy-System/wiki/%E9%99%84%E5%B8%B6GUI%E4%B9%8B%E4%BB%8B%E7%B4%B9)。
***

