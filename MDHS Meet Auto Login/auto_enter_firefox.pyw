from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager as GDM
from datetime import datetime
import schedule

driver = None

f = open("user.txt", "r")
lines = f.readlines()
f.close()
for i in range(4):
        lines[i] = lines[i].strip()
                
def Login_Google():
        
        global driver

        profile = FirefoxProfile()
        profile.set_preference("permissions.default.microphone", 1)
        profile.set_preference("permissions.default.camera", 1)
        profile.update_preferences()
        args = ["hide_console", ]
        driver = webdriver.Firefox(service_args=args, firefox_profile=profile, executable_path=GDM().install())

        url = "https://accounts.google.com/signin"
        mail = lines[0]
        password = lines[1]
        driver.get(url)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//input[@type="email"]').send_keys(mail)
        driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        driver.find_element_by_id("passwordNext").click()
        driver.implicitly_wait(5)

def Login_Meet():
    crm_url = "http://crm.mingdao.edu.tw/crm/index.asp"
    user = lines[2]
    password = lines[3]
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(crm_url)

    try:
        driver.find_element_by_xpath('//*[@id="showin_input"]').send_keys(user)
        driver.find_element_by_xpath(
            '/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[4]/td[2]/input').send_keys(
            password)
        driver.find_element_by_xpath(
            '/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[6]/td/input').click()
    except:
        pass
    driver.find_element_by_xpath(
        '/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td/table[1]/tbody/tr[2]/td[2]/div/a[1]').click()
    driver.close()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[-1])
    now = datetime.now()
    day = now.weekday() + 1
    time = now.hour * 60 + now.minute
    ctime = [555, 615, 675, 730, 855, 915, 975, 1030]
    for i, k in enumerate(ctime):
        if k > time:
            time = i + 1
            break
    driver.find_element_by_xpath('//*[@id="F_{}_{}_P"]/div'.format(day, time)).click()
    sleep(1)
    meet_url = driver.find_element_by_xpath('//*[@id="popupContent"]').get_attribute('src')
    driver.get(meet_url)
    driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
    meet_url = driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').text
    driver.close()

    driver.switch_to.window(driver.window_handles[-1])
    temp_count = 1
    html_source = driver.page_source
    while "????????????" in driver.page_source and datetime.now().minute <= 27:
        print("?????? Meet ???????????????????????????????????????")
        print("???????????????")
        sleep(10)
        try:
            driver.get(meet_url)
        except Exception:
            pass
    if "????????????" in driver.page_source:
        print("??????????????????")
    else:
        driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()

# DISCONNECTED_MSG = 'Unable to evaluate script: disconnected: not connected to DevTools\n'

def Login():
        if datetime.now().weekday() > 5:
                return
        Login_Google()
        Login_Meet()

hours = ['08', '09', 10, 11, 13, 14, 15, 16]
for i in hours:
        schedule.every().day.at(f'{i}:25:00').do(Login)

if __name__ == '__main__':
        while True:
                schedule.run_pending()
                sleep(1)
