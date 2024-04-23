from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

path = "C:\\Users\\DSRL\\Desktop\\chromedriver-win64.zip\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://thetestingworld.com/testings/")
driver.find_element(By.NAME, "fld_username").send_keys("Hello")

act = ActionChains(driver)
#act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys('a').perform()
#act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()
time.sleep(10)