# WindTurbine DSL與fortran比較操作時間之實驗
## 實驗環境
本實驗需安裝一組DSL及他的Framwork，以下為安裝步驟
1.下載MasonPy System中的MasonPy_Framwork及WindTurbine_DSL資料夾，將WindTurbine_DSL中的檔案與資料夾放入MasonPy_Framwork資料夾，再將MasonPy_Framwork中的UserDefineModule_example資料夾刪除。 
2.打開SetModule.py，將第51行TEST = ['testMode','HeronFormula']跟第61行AllClass.extend(TEST)刪除，再將第51行的UserdefinedClass的內容用下列列表取代['Mode_Init', 'Mode_ThreePhaseShortCircuit', 'Mode_ThreePhaseShortCircuit_MagBrake', 'Mode_MaxPower', 'Mode_MaxTorqueCurrent', 'Mode_MaxTorqueCurrent_MagBrake']。  
3.執行GUI.py就可使用，[範例GUI使用說明](https://github.com/ncu-psl/MasonPy-System/wiki/%E9%99%84%E5%B8%B6GUI%E4%B9%8B%E4%BB%8B%E7%B4%B9)，本GUI與範例有些不同，左側功能區沒有用圖形摺疊，都以文字表示。右上資訊區是顯示參數在各個時間所組成的折線圖。
## 實驗設計
本實驗分為3部分  
第一部分：讓受試者使用fortran、DSL及使用GUI分別寫出控制邏輯的程式碼，本部分再細分為2個階段，第一階段使用較簡單之流程圖，第二階段使用較複雜之流程圖。  
第二部分：受試者會拿到一張由第一部分第二階段的流程圖所修改成的新流程圖，受試者須用第一部分第二階段他們所寫的2份程式碼及GUI所畫的流程圖來更改為新的流程圖。  
第三部分：受試者會拿到2份新流程圖所轉成的程式碼，1份為fortran所寫的；1份為DSL所寫的，但受試者不知道2份是相同的流程圖。受試者需要從程式碼繪製出原本的流程圖。  
## 實驗檔案
每位受試者的資料都集中在以受試者編號命名的資料夾中  
第一部分第一階段產生"測試1-1(DSL程式碼).txt"及"測試1-1(Fortran程式碼).txt"2個程式碼檔案  
第一部分第二階段產生"測試1-2(DSL程式碼).txt"及"測試1-2(Fortran程式碼).txt"2個程式碼檔案  
第二部分產生"測試2(DSL程式碼).txt"及"測試2(Fortran程式碼).txt"2個程式碼檔案  
第三部分的解果為"測試3結果"的圖片檔  
受試者的計時結果紀錄在"測試時間.txt"中
## 受試者受試時間
蔡承耘 2019-6-22 20:00-23:00進行測試  
呂柏憲 2019-6-22 17:00-20:00進行測試  
曹舒維 2019-6-22 1700-1800 2300-0100進行測試  
黃子平 2019-6-22 22:30-24:30進行測試  
劉康郁 2019-6-23 12:00-17:00進行測試  
