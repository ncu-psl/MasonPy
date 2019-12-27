***
# MasonPy-System
***
## 簡介 Introduction 
本研究為一套流程圖式特定領域語言。
MasonPy提供自定義功能塊功能，可藉此定義所應用領域的一系列功能塊，達到建構一套自己的DSL。並將這套功能塊提供End-User藉由UI拖拉拼接流程，完成程式。

We are developing a domain-specific language (DSL)  framework along with flow diagram.
MasonPy provides the user defined functional blocks to create customized DSL which consists of a series of funtional blocks for the specific topic. End-User can drag and drop the units to complete a program.


[摘要 Abstract](https://github.com/ncu-psl/MasonPy-System/wiki)

***
## 架構 MasonPy Architecture
[MasonPy 架構 (Chinese)](https://github.com/ncu-psl/MasonPy-System/wiki/MasonPy-%E6%9E%B6%E6%A7%8B)

[MasonPy Architecture (English)](https://github.com/ncu-psl/MasonPy-System/wiki/MasonPy-Structure)
***
## Programming Language
Python3
***
## IDE
Spyder
***
## 操作說明 How to use
下載MasonPy-System中的MasonPy_DSL及MasonPy_Framwork兩個檔案，將MasonPy_DSL內容全部複製至MasonPy_Framwork，MasonPy_DSL的GUI.py為主程式，MasonPy System/MasonPy_Framwork/UserDefineModule_example為範例自定義功能塊。

1. Download MasonPy_DSL and MasonPy_Framwork in MasonPy-System.
2. Copy the contents of MasonPy_DSL to MasonPy_Framwork.
3. GUI.py in MasonPy_DSL is the main program. MasonPy System, MasonPy_Framwork, and UserDefineModule_example are the examples of user defined functional blocks.
***
## 流程圖基本功能塊簡介 Flowchart basic functional block introduction
[流程圖基本功能塊簡介 Flowchart basic functional block introduction](https://github.com/ncu-psl/MasonPy-System/wiki/%E6%B5%81%E7%A8%8B%E5%9C%96DSL-%E5%8A%9F%E8%83%BD%E5%A1%8A-%E7%B0%A1%E4%BB%8B)
***
## 指令說明及範例 MasonPy DSL instruction description and examples
[指令說明及範例 instruction description and examples](https://github.com/ncu-psl/MasonPy-System/wiki/MasonPy-DSL-%E6%8C%87%E4%BB%A4%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%AF%84%E4%BE%8B)
***
## 自定義領域功能塊 User defined functional block
[自定義領域功能塊方法 Method for user defined functional block](https://github.com/ncu-psl/MasonPy-System/wiki/%E5%8A%9F%E8%83%BD%E5%A1%8A-%E8%87%AA%E5%AE%9A%E7%BE%A9)
***
## 簡介 MasonPy Debugger introduction
[Debugger](https://github.com/ncu-psl/MasonPy-System/wiki/Debugger-%E7%B0%A1%E4%BB%8B)
***
***
***
# 用於繪製風力發電控制邏輯之特定領域語言 DSL for drawing the control logic diagram about wind power
***
## 簡介 Introduction
此特定領域語言是基於MasonPy所擴增的一組風力發電相關的DSL  
此DSL有6個功能塊，Init、MaxPower、MaxTorqueCurrent、ThreePhaseShortCircuit、MaxTorqueCurrent_MagBrake、ThreePhaseShortCircuit_MagBrake 

This domain-specific language is based on MasonPy about the field of wind power.
There are six funtional blocks. Such as Init, MaxPower, MaxTorqueCurrent, ThreePhaseShortCircuit, MaxTorqueCurrent_MagBrake and ThreePhaseShortCircuit_MagBrake.

***
## 操作說明 How to use
1. 下載MasonPy System中的MasonPy_Framwork及WindTurbine_DSL資料夾，將WindTurbine_DSL中的檔案與資料夾放入MasonPy_Framwork資料夾，再將MasonPy_Framwork中的UserDefineModule_example資料夾刪除。

2. 打開SetModule.py，將第51行TEST = ['testMode','HeronFormula']跟第61行AllClass.extend(TEST)刪除，再將第51行的UserdefinedClass的內容用下列列表取代['Mode_Init', 'Mode_ThreePhaseShortCircuit', 'Mode_ThreePhaseShortCircuit_MagBrake', 'Mode_MaxPower', 'Mode_MaxTorqueCurrent', 'Mode_MaxTorqueCurrent_MagBrake']。  

3. 執行GUI.py就可使用，[範例GUI使用說明](https://github.com/ncu-psl/MasonPy-System/wiki/%E9%99%84%E5%B8%B6GUI%E4%B9%8B%E4%BB%8B%E7%B4%B9)，本GUI與範例有些不同，左側功能區沒有用圖形摺疊，都以文字表示。右上資訊區是顯示參數在各個時間所組成的折線圖。

.
1. Download MasonPy_Framwork and WindTurbine_DSL in MasonPy System, and move the files and folders in  WindTurbine_DSL to MasonPy_Framwork folder. Next, delete UserDefineModule_example folder in MasonPy_Framwork.

2. For SetModule.py, delete TEST = ['testMode','HeronFormula'] of line 51 and AllClass.extend(TEST) of line 61, and replace the contents of UserdefinedClass of line 51 with the following list ['Mode_Init', 'Mode_ThreePhaseShortCircuit', 'Mode_ThreePhaseShortCircuit_MagBrake', 'Mode_MaxPower', 'Mode_MaxTorqueCurrent', 'Mode_MaxTorqueCurrent_MagBrake'].

3. Run GUI.py to execute. [GUI introduction](https://github.com/ncu-psl/MasonPy-System/wiki/%E9%99%84%E5%B8%B6GUI%E4%B9%8B%E4%BB%8B%E7%B4%B9)
This is a little different from the example. The left-side function area is not folded with graphics, but is represented by text. The upper right information area is a line chart showing the parameters at various times.
***
