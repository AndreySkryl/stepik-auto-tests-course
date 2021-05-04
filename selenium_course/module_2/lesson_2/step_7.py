import os
from selenium import webdriver
import time


browser = None
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_css_selector('[name="firstname"]')
    lastname = browser.find_element_by_css_selector('[name="lastname"]')
    email = browser.find_element_by_css_selector('[name="email"]')
    file = browser.find_element_by_css_selector('[type="file"]')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, 'file.txt')

    firstname.send_keys('firstname')
    lastname.send_keys('lastname')
    email.send_keys('email')
    file.send_keys(filename)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    if browser:
        browser.quit()
