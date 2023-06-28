from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from data import list
from data import counter
import time

url = "https://vertexprotocol.com/?utm_source=cypherhunter"
options = webdriver.ChromeOptions()

#отключение режима робота
options.add_argument("--disable-blink-features=AutomationControlled" )

#работа в фоновом режиме
options.add_argument("--headless")

#направление в хром
s=Service('/Users/juliapopruga/Desktop/test2_0/clicker/chromedriver 3')
driver = webdriver.Chrome(service=s, options=options)



try:

    driver.get(url=url)
    time.sleep(5)

    for i in list:
        email_input = driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/section[1]/div/div[1]/div/div[2]/div/input")
        time.sleep(2)
        email_input.send_keys(i)
        enter = driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/section[1]/div/div[1]/div/div[2]/div/button/span").click()
        time.sleep(3)
        counter+=1
        print(f"Заполнен {counter} email: ", i)

        #обновляем страницу
        driver.refresh()
        time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

print("Готово!")

