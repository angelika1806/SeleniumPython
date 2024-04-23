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
# Working on Dropdown

obj = Select(driver.find_element(By.NAME, "sex"))
#select_element.select_by_value("Male")
#select_element.select_by_visible_text("Male")
obj.select_by_index(1)

# Fetch Selected option
print(obj.first_selected_option.text)

for op in obj.options:
    print(op.text)

time.sleep(10)