from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()
mainWin=""
# Открываем веб-страницу
driver.get("https://ru.airbnb.com/")

# Максимизируем окно браузера
driver.maximize_window()
driver.find_element(By.XPATH, "//img[@class='itu7ddv atm_e2_idpfg4 atm_vy_idpfg4 atm_mk_stnw88 atm_e2_1osqo2v__1lzdix4 atm_vy_1osqo2v__1lzdix4 i1cqnm0r atm_jp_pyzg9w atm_jr_nyqth1 i1de1kle atm_vh_yfq0k3 dir dir-ltr']").click()


allTabs = driver.window_handles
print(allTabs)
'''for tab in allTabs:
    driver.switch_to.window(tab)
    print(driver.current_url)'''

for tab in allTabs:
    driver.switch_to.window(tab)
    if driver.current_url == "https://ru.airbnb.com/rooms/523783410417354397?adults=1&category_tag=Tag%3A8536&children=0&enable_m3_private_room=true&infants=0&pets=0&photo_id=1308799035&search_mode=flex_destinations_search&check_in=2024-04-07&check_out=2024-04-12&source_impression_id=p3_1711565742_95EkF%2BQiIOliMC%2F9&previous_page_section_name=1000&federated_search_id=ce5c08a4-aa9c-49ce-9855-30558cfd242f":
        driver.find_element(By.XPATH,
                            "//img[@class='itu7ddv atm_e2_idpfg4 atm_vy_idpfg4 atm_mk_stnw88 atm_e2_1osqo2v__1lzdix4 atm_vy_1osqo2v__1lzdix4 i1cqnm0r atm_jp_pyzg9w atm_jr_nyqth1 i1de1kle atm_vh_yfq0k3 dir dir-ltr']").click()

















