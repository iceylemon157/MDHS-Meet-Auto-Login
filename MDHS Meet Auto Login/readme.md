# Auto Enter 程式碼

## 介紹
* 上課時間 (25 分) 準時自動開啟 Meet
* 可達到純後台運行程式碼

## 使用方法

1. 先載好 selenium 跟 webdriver_manager 這兩個 Python Package

   ```
   pip install selenium
   pip install webdriver-manager
   ```

2. 選擇要用 Google 或 Firefox 下載相應的程式碼 (auto_enter_google.py or auto_enter_firefox.py)
3. 在跟程式碼同一個資料夾下創建一個文字檔案叫做 user.txt，請寫入四行分別依序為 "學校 Gmail 帳號", "學校 Gmail 密碼", "明道雲端平台帳號", "明道雲端平台密碼" (不包含引號)
4. 雙擊執行程式

## 關掉小黑框

1. 找到你的 Python 資料夾 (可以在 cmd 輸入 ```where python``` )
2. 在 python 資料夾找到 Lib\site-packages\selenium\webdriver\common\service.py 這個檔案
3. 替換成資料夾中的 service.py
