#Screening.py
#A.Schwartz
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('http://screening.wustl.edu/')  # loads up
time.sleep(3)
driver.get(driver.current_url)  # connect to re-directed site - login

# log in
txtUsername = driver.find_element_by_xpath('//*[@id="ucWUSTLKeyLogin_txtUsername"]')
txtUsername.send_keys('username')

txtPassword = driver.find_element_by_xpath('//*[@id="ucWUSTLKeyLogin_txtPassword"]')
txtPassword.send_keys('password')

btnLogin = driver.find_element_by_xpath('//*[@id="ucWUSTLKeyLogin_btnLogin"]')
btnLogin.click()

# duo mobile
driver.get(driver.current_url)  # connect to re-directed site - duo


tab = ActionChains(driver)
tab = tab.send_keys(Keys.TAB)
enter = ActionChains(driver)
enter = enter.send_keys(Keys.ENTER)

tab.perform()
time.sleep(.9)
tab.perform()
enter.perform()

print('Duo notification sent.')
#user accepts duo push notification
print('We will wait 15 seconds')
time.sleep(15)
print('15 seconds later')
#form page is loaded
driver.get(driver.current_url) # connect to re-directed site - form
print('New url loaded')

btnDanforth = driver.find_element_by_xpath('//*[@id="Campus"]')
driver.execute_script("return arguments[0].scrollIntoView();", btnDanforth)
print('Just clicked')
driver.execute_script("arguments[0].click();", btnDanforth)

print('Danforth clicked')

btnAttest = driver.find_element_by_xpath('//*[@id="chk_Attestation"]')
driver.execute_script("return arguments[0].scrollIntoView();", btnAttest)
driver.execute_script("arguments[0].click();", btnAttest)
print('Attest clicked')

btnSubmit = driver.find_element_by_xpath('//*[@id="btnSubmit"]')
driver.execute_script("return arguments[0].scrollIntoView();", btnSubmit)
driver.execute_script("arguments[0].click();", btnSubmit)
print('Submit clicked')
