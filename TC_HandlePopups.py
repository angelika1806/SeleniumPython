from selenium.webdriver.common.by import By
from selenium import webdriver


# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get("https://us.shein.com/?url_from=usadgpm_womentopsblousestee_20240119_GPM&cid=20909327883&setid=&adid=&pf=GOOGLE&gad_source=1&gclid=CjwKCAjw5ImwBhBtEiwAFHDZx3D4MyWJFH8nmBRcvJDbvuK7URkgcb85ypljDtKPFAYaT4W6tSrOwxoCscAQAvD_BwE")

# Максимизируем окно браузера
driver.maximize_window()

Allwindows = driver.window_handles
#print(Allwindows)
for window in Allwindows:
    driver.switch_to.window(window)
    #print(driver.current_url)
    if (driver.current_url == "https://us.shein.com/?url_from=usadgpm_womentopsblousestee_20240119_GPM&cid=20909327883&setid=&adid=&pf=GOOGLE&gad_source=1&gclid=CjwKCAjw5ImwBhBtEiwAFHDZx3D4MyWJFH8nmBRcvJDbvuK7URkgcb85ypljDtKPFAYaT4W6tSrOwxoCscAQAvD_BwE"):
        print("This is my main window")
    else:
        driver.close()


