from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get("https://thetestingworld.com/testings/")

# Максимизируем окно браузера
driver.maximize_window()

# Ждем, пока поле ввода имени пользователя не станет видимым
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "fld_username"))
)

# Вводим текст в поле ввода имени пользователя
username_input.send_keys("Abhfgy")

# Очищаем поле ввода
username_input.clear()

# Ждем, пока поле ввода адреса электронной почты не станет видимым
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='fld_email']"))
)

# Вводим текст в поле ввода адреса электронной почты
email_input.send_keys("Gjjkhj")

# Вводим текст в поле ввода имени пользователя
username_input.send_keys("Angela")

# Находим радиокнопку "office" и выбираем ее
radiobutton_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@value='office']"))
)
radiobutton_input.click()

#Working on Checkbox
checkbox_inp

