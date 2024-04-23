from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get("https://thetestingworld.com/testings/")

# Максимизируем окно браузера
driver.maximize_window()

# Fatching Data
#print("Title of page is " + driver.title)

# Fatching URL of Page
#print("Page is " + driver.current_url)

# Fetch Complete Page HTML
#print("*************************************")
#print(driver.page_source)

# Fetching Element Text

#print("Text on Link is " + driver.find_element(By. CLASS_NAME, "displayPopup").text)
print("Value of Bottom is " + driver.find_element(By. XPATH , "//input[@type='submit']").get_attribute("value"))
time.sleep(10)
