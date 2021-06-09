# 明道中學 Meet 自動登入程式

## 介紹

* 30秒內自動幫你進入到 Meet
* 可以自動判斷現在應該上哪一堂課或手動輸入要上的節數

## 使用方法

1. 先載好 selenium 跟 webdriver_manager 這兩個 Python Package

   ```
   pip install selenium
   pip install webdriver-manager
   ```

2. 選擇要用 Google 或 Firefox 下載相應的程式碼
3. 在跟程式碼同一個資料夾下創建一個文字檔案叫做 user.txt，請寫入四行分別依序為 "學校 Gmail 帳號", "學校 Gmail 密碼", "明道雲端平台帳號", "明道雲端平台密碼" (不包含引號)
4. 雙擊執行程式
5. 過程中會問你是否是否要自動判斷現在是哪一節課，依照指示在小黑框上面回應即可
