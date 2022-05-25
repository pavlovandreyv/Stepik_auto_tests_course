from selenium import webdriver
import math, time

# математический расчет от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    url_link="http://suninjuly.github.io/math.html"
    browser.get(url_link)

    # считываем x
    l_x=calc(browser.find_element_by_id("input_value").text)
    
    # вводим расчет в поле
    l_text=browser.find_element_by_id("answer")
    l_text.send_keys(l_x)

    # подтверждение робота
    l_robot=browser.find_element_by_xpath("//*[contains(text(),'I') and contains(text(),'m the robot')]")
    l_robot.click()

    # выбираем режим ввода роботом
    l_robot_rule=browser.find_element_by_css_selector("[for='robotsRule']")
    l_robot_rule.click()

    # завершаем
    l_submit=browser.find_element_by_css_selector("button.btn")
    l_submit.click()
    #

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла