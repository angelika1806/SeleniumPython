from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import pytest
import time
from TakeScreenshort import take_page_screenshot


@pytest.fixture()
def enviroment_setup():
    global driver
    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome()
    # Открываем веб-страницу
    driver.set_page_load_timeout(10)
    driver.get("https://thetestingworld.com/testings/")
    # Максимизируем окно браузера
    driver.maximize_window()
    yield
    driver.quit()

def test_verify_registration (enviroment_setup):

    # Ждем, пока поле ввода имени пользователя не станет видимым
    username_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "fld_username"))
    )
    # Вводим текст в поле ввода имени пользователя
    username_input.send_keys("Abhfgy")

    # Очищаем поле ввода
    username_input.clear()

    # Ждем, пока поле ввода адреса электронной почты не станет видимым
    email_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='fld_email']"))
    )
    # Вводим текст в поле ввода адреса электронной почты
    email_input.send_keys("Gjjkhj")

    # Вводим текст в поле ввода имени пользователя
    username_input.send_keys("Angela")

    time.sleep(5)  # Пауза в 15 секунд

    # Находим радиокнопку "office" и выбираем ее
    radiobutton_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='office']"))
    )
    radiobutton_input.click()

    # Working on Checkbox
    checkbox_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "terms"))
    )


    # Working on Button
    button_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))
    )
    button_input.click()

    # Вводим текст в поле ввода имени пользователя
    checkbox_input.click()

    # Working on link
    link_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Read Detail"))
    )
    link_input.click()

    # Find the close button by CSS selector

    close_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='X']"))
    )
    close_button.click()


    # Working on Dropdown
    select_element = Select(driver.find_element(By.NAME, "sex"))
    #elect_element.select_by_value("Male")
    # select_element.select_by_visible_text("Male")
    select_element.select_by_index(1)

    # Ждем, пока выпадающий список с ID 'countryId' станет видимым
    wait_element = WebDriverWait(driver, 10)
    wait_element.until(EC.presence_of_element_located((By.ID, 'countryId')))
    obj = Select(driver.find_element(By.ID, 'countryId'))
    obj.select_by_visible_text("India")

    # Ждем, пока выпадающий список с ID 'stateId' станет видимым
    '''wait_element = WebDriverWait(driver, 1000)
    wait_element.until(EC.presence_of_element_located((By.ID, 'stateId')))
    obj = Select(driver.find_element(By.ID, 'stateId'))
    obj.select_by_visible_text("Bihar")
    '''
    #driver.find_element(By.XPATH, "//input[@value='home']").click()



    assert driver.current_url == "https://thetestingworld.com/testings/"

    #take_page_screenshot(driver, "Second_Screenshot")


    #TakeScreenshort.take_page_screenshot(driver, "First_Screenshot")

    #driver.get_screenshot_as_file("C:/Users/DSRL/PycharmProjects/SeleniumAutomation/BeforeRegistration.png")

    driver.execute_script("window.scrollTo(0, 400);")
