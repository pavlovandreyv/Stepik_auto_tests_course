from select import select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, math

browser=webdriver.Chrome()
url_link="http://suninjuly.github.io/selects2.html"
browser.get(url_link)

try:
    # математические вычисления
    l_a=browser.find_element_by_id("num1").text
    l_b=browser.find_element_by_id("num2").text
    c=str(int(l_a)+int(l_b))

    # выбор значения из раскрывающегося списка
    select=Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_visible_text(c)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
#