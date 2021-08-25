#Screening.py - This file traverses through multiple webpages and clicks button to complete a COVID screening.
#A.Schwartz
#1.27.21

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
print('Sleeping for 5 sec')
time.sleep(6)
print('5 sec later')
#driver.get(driver.current_url)  # connect to re-directed site - duo

btnDanforth = driver.find_element_by_xpath('//*[@id="mat-radio-5"]/label/div[1]/div[1]')
driver.execute_script("return arguments[0].scrollIntoView();", btnDanforth)
print('Just clicked')
driver.execute_script("arguments[0].click();", btnDanforth)

print('Danforth clicked')

btnNone = driver.find_element_by_xpath('//*[@id="mat-checkbox-9"]/label/div')
driver.execute_script("return arguments[0].scrollIntoView();", btnNone)
driver.execute_script("arguments[0].click();", btnNone)
print('None of the above')

btnCovT = driver.find_element_by_xpath('//*[@id="mat-radio-8"]/label/div[1]/div[1]')
driver.execute_script("return arguments[0].scrollIntoView();", btnCovT)
driver.execute_script("arguments[0].click();", btnCovT)
print('CovT')

btnCloseContact = driver.find_element_by_xpath('//*[@id="mat-radio-10"]/label/div[1]/div[1]')
driver.execute_script("return arguments[0].scrollIntoView();", btnCloseContact)
driver.execute_script("arguments[0].click();", btnCloseContact)
print('CC')

btnAttest = driver.find_element_by_xpath('//*[@id="mat-radio-11"]/label/div[1]/div[1]')
driver.execute_script("return arguments[0].scrollIntoView();", btnAttest)
driver.execute_script("arguments[0].click();", btnAttest)
print('Attested')

btnSubmit = driver.find_element_by_xpath('/html/body/app-root/app-layout/div/div/app-symptom-screener/div/form/div[2]/div[7]/button')
driver.execute_script("return arguments[0].scrollIntoView();", btnSubmit)
driver.execute_script("arguments[0].click();", btnSubmit)
print('Submit clicked')
