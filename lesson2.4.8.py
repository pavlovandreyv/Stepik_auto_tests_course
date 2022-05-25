from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

# математический расчет от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
browser.find_element_by_id("book").click()

# считываем x
l_x=calc(browser.find_element_by_id("input_value").text)
    
# вводим расчет в поле
l_text=browser.find_element_by_id("answer")
l_text.send_keys(l_x)

# завершаем
l_submit=browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", l_submit)
l_submit.click()
#
