from selenium import webdriver
import time, math

# математический расчет от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    url_link="http://suninjuly.github.io/get_attribute.html"
    browser.get(url_link)

    # считываем значение для расчета
    l_valuex=browser.find_element_by_css_selector("[valuex]")
    l_valuex_attr=l_valuex.get_attribute("valuex")
    math_x=calc(l_valuex_attr)

    # вводим результат расчета в поле ввода
    l_text=browser.find_element_by_id("answer")
    l_text.send_keys(math_x)

    # подтверждение робота
    l_robot=browser.find_element_by_id("robotCheckbox")
    l_robot.click()

    # выбираем режим ввода роботом
    l_robot_rule=browser.find_element_by_id("robotsRule")
    l_robot_rule.click()

    # завершаем
    l_submit=browser.find_element_by_css_selector("button.btn")
    l_submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#