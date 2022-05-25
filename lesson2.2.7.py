from ast import Try
from selenium import webdriver
import os, time

# данные
url_link="http://suninjuly.github.io/file_input.html"

try:
    browser=webdriver.Chrome()
    browser.get(url_link)

    # все локаторы
    l_text=browser.find_elements_by_css_selector("[type=text]")
    for element in l_text:
        element.send_keys("Text")  

    # загружаем файл
    browser.find_element_by_css_selector("[type=file]").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)),"text.txt"))     

    # завершаем
    browser.find_element_by_css_selector("button.btn").click() 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    #