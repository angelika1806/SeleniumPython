from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

driver = Firefox()

path = "C://Users//DSRL//Desktop//geckodriver-v0.34.0-win-aarch64//geckodriver.exe"

driver.get("https://thetestingworld.com/testings/")

# Максимизируем окно браузера
driver.maximize_window()

driver.find_element(By.NAME, "fld_username").send_keys("Helloworld")
driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys("testingworld@gmail.com")
driver.find_element(By.NAME, "fld_password").send_keys("Hhg1254")
driver.find_element(By.NAME, "fld_username").clear()
driver.find_element(By.NAME, "fld_username").send_keys("Angela")

# Working on Radio button
driver.find_element(By.XPATH, "fld_password")
