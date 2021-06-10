# 明道中學 Meet 自動登入程式

## 介紹

* 30秒內自動幫你進入到 Meet
* 可以自動判斷現在應該上哪一堂課或手動輸入要上的節數

## GUI 使用方法

1. 下載 main.exe
2. 在跟 exe 檔同一個資料夾下創建一個文字檔案叫做 user.txt，請寫入四行分別依序為 "學校 Gmail 帳號", "學校 Gmail 密碼", "明道雲端平台帳號", "明道雲端平台密碼" (不包含引號)
3. 直接點開 main.exe 就可以用了

PS: 開啟瀏覽器的過程，GUI介面可能會顯示 "沒有回應"，等到開到 Meet 的畫面時會自動變回去，不需要把他關掉。
PS2: 小黑框是程式執行本體，關掉他會把整個程式關掉
Ps3: 瀏覽器開啟過程中若把瀏覽器關掉或是關閉(新增)分頁可能會使程式發生錯誤，直到介面顯示 Meet 已成功開啟才完成。

## Python 程式碼 使用方法 

1. 先載好 selenium 跟 webdriver_manager 這兩個 Python Package

   ```
   pip install selenium
   pip install webdriver-manager
   ```

2. 選擇要用 Google 或 Firefox 下載相應的程式碼
3. 在跟程式碼同一個資料夾下創建一個文字檔案叫做 user.txt，請寫入四行分別依序為 "學校 Gmail 帳號", "學校 Gmail 密碼", "明道雲端平台帳號", "明道雲端平台密碼" (不包含引號)
4. 雙擊執行程式
5. 過程中會問你是否是否要自動判斷現在是哪一節課，依照指示在小黑框上面回應即可
