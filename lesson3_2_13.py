from selenium import webdriver
from selenium.webdriver.common.by import By
import time, pytest

def test_1():
    browser = webdriver.Chrome()
    url_link = "http://suninjuly.github.io/registration1.html"
    browser.get(url_link)
    # Ваш код, который заполняет обязательные поля
    # First name*
    frm_reg_first=browser.find_element(By.XPATH, value="//label[text()='First name*']/../input[@required]")
    frm_reg_first.send_keys("first")
    # Last name*
    frm_reg_second=browser.find_element(By.XPATH, value="//label[text()='Last name*']/../input")
    frm_reg_second.send_keys("second")
    # Email*
    frm_reg_second=browser.find_element(By.XPATH, value="//label[text()='Email*']/../input")
    frm_reg_second.send_keys("third@mail.ru")   

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert welcome_text=="Congratulations! You have successfully registered!", "Не удалось зарегистрироваться"
    browser.quit()

def test_2():
    browser = webdriver.Chrome()
    url_link = "http://suninjuly.github.io/registration2.html"
    browser.get(url_link)
    # Ваш код, который заполняет обязательные поля
    # First name*
    frm_reg_first=browser.find_element(By.XPATH, value="//label[text()='First name*']/../input[@required]")
    frm_reg_first.send_keys("first")
    # Last name*
    frm_reg_second=browser.find_element(By.XPATH, value="//label[text()='Last name*']/../input")
    frm_reg_second.send_keys("second")
    # Email*
    frm_reg_second=browser.find_element(By.XPATH, value="//label[text()='Email*']/../input")
    frm_reg_second.send_keys("third@mail.ru")   

    # Отправляем заполненную форму
    button = browser.find_element_by(By.CSS_SELECTOR, value="button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert welcome_text=="Congratulations! You have successfully registered!", "Не удалось зарегистрироваться"
    browser.quit()

#