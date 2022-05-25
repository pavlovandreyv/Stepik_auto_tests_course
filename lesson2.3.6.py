from time import time
from selenium import webdriver
import time, math

# математический расчет от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# данные
url_link="http://suninjuly.github.io/redirect_accept.html"

try:
    browser=webdriver.Chrome()
    browser.get(url_link)

    # нажимаем на конпку submit
    browser.find_element_by_css_selector("[type=submit]").click()

    # переход на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # считываем x
    l_x=calc(browser.find_element_by_id("input_value").text)
    
    # вводим расчет в поле
    l_text=browser.find_element_by_id("answer")
    l_text.send_keys(l_x)

    # завершаем
    l_submit=browser.find_element_by_css_selector("button.btn")
    l_submit.click()

finally:
    # ожидание копирования
    time.sleep(5)
    # закрываем вкладку
    browser.quit()
    #