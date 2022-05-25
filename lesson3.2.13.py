from multiprocessing.connection import wait
from selenium import webdriver
import unittest, time

def test_base(url_link):
    browser.get(url_link)
     # Ваш код, который заполняет обязательные поля
    # First name*
    frm_reg_first=browser.find_element_by_xpath("//label[text()='First name*']/../input[@required]")
    frm_reg_first.send_keys("first")
    # Last name*
    frm_reg_second=browser.find_element_by_xpath("//label[text()='Last name*']/../input")
    frm_reg_second.send_keys("second")
    # Email*
    frm_reg_second=browser.find_element_by_xpath("//label[text()='Email*']/../input")
    frm_reg_second.send_keys("third@mail.ru")   

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

     # ждем загрузки страницы
    time.sleep(1)

  

class Test(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        test_base(link)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Не удалось зарегистрироваться")
    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        test_base(link)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Не удалось зарегистрироваться")


    
browser = webdriver.Chrome()
if __name__ == "__main__":
    unittest.main()
browser.quit()