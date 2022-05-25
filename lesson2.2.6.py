from selenium import webdriver
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    #математические расчеты
    x=calc(browser.find_element_by_id("input_value").text)

    # ввод текста в поле ввода
    l_text=browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", l_text)
    l_text.send_keys(x)

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