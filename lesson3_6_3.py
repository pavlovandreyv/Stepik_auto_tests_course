from ast import If
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_url(browser, url):
    # открываем страницу
    link = f"https://stepik.org/lesson/236{url}/step/1"
    browser.get(link)
    # ждем локатор для ввода значения
    WebDriverWait(browser, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".submit-submission")))
    # производим расчет и вводим значение
    l_answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']").send_keys(l_answer)
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    # ждем ответ
    WebDriverWait(browser, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"smart-hints__hint")))
    # считываем ответ
    l_response=browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    
    assert l_response == "Correct!"
#