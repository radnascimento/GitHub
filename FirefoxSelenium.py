from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

options = Options()
options.binary_location  = r'C:\Program Files\Mozilla Firefox\firefox.exe'
fp = webdriver.FirefoxProfile(r'C:\\Users\\gero_\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\pj30g8pw.default-release')
driver = webdriver.Firefox(options=options, firefox_profile=fp)



for window_handle in range(len(driver.window_handles)) :
    driver.switch_to.window(driver.window_handles[window_handle])
    driver.get('https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher')

for window_handle in range(len(driver.window_handles)) :
    driver.switch_to.window(driver.window_handles[window_handle])
    time.sleep(1)
    elem = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
    elem.send_keys("lojinha.do.salim")
    password = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
    password.send_keys('')   
    password.send_keys(Keys.RETURN)



time.sleep(10000)

driver.quit()