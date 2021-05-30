# 明道中學 Meet 自動登入程式

## 使用方法

1. 先載好 selenium 這個 Python Package

   ```
   pip install selenium
   ```

2. 下載跟你的 Chrome 同一個版本的 Chrome Driver，在 C磁碟下 創建一個資料夾叫做 Webdriver，然後把 chromedriver.exe 丟進去
3. 把 Webdriver 這個資料夾加到環境變數   
4. 將 auto_meet_login.py 下載下來
5. 在跟程式碼同一個資料夾下創建一個文字檔案叫做 user.txt，請寫入四行分別依序為 "學校 Gmail 帳號", "學校 Gmail 密碼", "明道雲端平台帳號", "明道雲端平台密碼"
6. 雙擊 auto_meet_login.py
7. 過程中會問你是否是否要自動判斷現在是哪一節課，依照指示在小黑框上面回應即可
