from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest


@pytest.fixture()
def environment_setup():
    global driver
    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome()
    # Открываем веб-страницу
    driver.get("https://thetestingworld.com/")
    # Максимизируем окно браузера
    driver.maximize_window()
    yield
    driver.quit()

def test_openingFile(environment_setup):
    driver.find_element_by_xpath("//a[@title='CorporateTraining']").click()










