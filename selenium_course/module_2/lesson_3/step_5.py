from math import *
from selenium import webdriver
import time


def calc(x):
    return log(abs(12 * sin(x)))


browser = None
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id('input_value').text)
    result = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    if browser:
        browser.quit()
