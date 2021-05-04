from math import *
from selenium import webdriver
import time


def calc(x):
    return log(abs(12 * sin(x)))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('input_value').text)
    result = calc(x)

    answer = browser.find_element_by_id('answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
    answer.send_keys(str(result))

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    robot_checkbox.click()
    robots_rule_radiobutton = browser.find_element_by_id('robotsRule')
    robots_rule_radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
