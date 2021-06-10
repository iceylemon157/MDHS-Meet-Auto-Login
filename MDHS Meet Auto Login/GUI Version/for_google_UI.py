from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CDM
from datetime import datetime


def Login(auto, day=0, time=0):
    print(auto, day, time, 'lalala')
    try:
        f = open("user.txt", "r")
    except:
        input("Please create user.txt file")
        exit()
    lines = f.readlines()
    f.close()

    for i in range(4):
        lines[i] = lines[i].strip()

    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")

    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })

    driver = webdriver.Chrome(chrome_options=opt, executable_path=CDM().install())

    url = "https://accounts.google.com/signin"
    mail = lines[0]
    password = lines[1]
    driver.get(url)
    sleep(2)
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(mail)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    sleep(3)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    sleep(3)

    crm_url = "http://crm.mingdao.edu.tw/crm/index.asp"

    user = lines[2]
    password = lines[3]

    driver.get(crm_url)
    driver.find_element_by_xpath('//*[@id="showin_input"]').send_keys(user)
    driver.find_element_by_xpath(
        '/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[4]/td[2]/input').send_keys(
        password)
    driver.find_element_by_xpath(
        '/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[6]/td/input').click()
    driver.find_element_by_xpath(
        '/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td/table[1]/tbody/tr[2]/td[2]/div/a[1]').click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])

    if auto != 'n':
        now = datetime.now()
        day = now.weekday() + 1
        time = now.hour * 60 + now.minute
        ctime = [555, 615, 675, 730, 855, 915, 975, 1030]
        if time > 1030:
            print("今天已經下課囉")
            sleep(3)
            print("關閉程式")
            driver.quit()
            exit()
        for i, k in enumerate(ctime):
            if k > time:
                time = i + 1
                break
    else:
        day = int(day.split(' ')[1])
        time = int(time.split(' ')[1])

    driver.find_element_by_xpath('//*[@id="F_{}_{}_P"]/div'.format(day, time)).click()
    sleep(1)
    a = driver.find_element_by_xpath('//*[@id="popupContent"]').get_attribute('src')
    driver.get(a)
    driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
