from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager as GDM
from datetime import datetime

f = open("user.txt", "r")
lines = f.readlines()
f.close()

for i in range(4):
	lines[i] = lines[i].strip()

profile = FirefoxProfile()
profile.set_preference("permissions.default.microphone", 1)
profile.set_preference("permissions.default.camera", 1)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile, executable_path=GDM().install())

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
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[4]/td[2]/input').send_keys(password)
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[6]/td/input').click()
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td/table[1]/tbody/tr[2]/td[2]/div/a[1]').click()
sleep(5)
driver.switch_to.window(driver.window_handles[1])

auto = input("自動判斷? (y/n)")

if auto[0] == "n":
	print("要上哪一堂課呢?")
	ok = False
	while not ok:
		day = int(input("星期 (1~5的數字):"))
		if day > 5 or day < 1:
			print("超出範圍")
		else:
			ok = True
	ok = False
	while not ok:
		time = int(input("第幾節課 (1~8的數字)"))
		if time > 9 or time < 1:
			print("超出範圍")
		else:
			ok = True
else:
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

driver.find_element_by_xpath('//*[@id="F_{}_{}_P"]/div'.format(day, time)).click()
sleep(1)
a = driver.find_element_by_xpath('//*[@id="popupContent"]').get_attribute('src')
driver.get(a)
driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
sleep(5)
driver.switch_to.window(driver.window_handles[2])
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]').click()
