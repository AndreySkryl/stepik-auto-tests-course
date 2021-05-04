from math import *
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return log(abs(12 * sin(x)))


browser = None
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    book = browser.find_element_by_id('book')
    book.click()

    x = int(browser.find_element_by_id('input_value').text)
    result = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))

    # Отправляем заполненную форму
    button = browser.find_element_by_id('solve')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    if browser:
        browser.quit()
