from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_basket(browser):
    browser.get(link)
    # time.sleep(30)
    assert browser.find_elements(By.CSS_SELECTOR, value="button.btn-add-to-basket"), 'Кнопка добавления в корзину не найдена'