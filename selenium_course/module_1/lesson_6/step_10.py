from selenium import webdriver
import time

try:
    # link = "http://suninjuly.github.io/registration1.html" # OK
    link = "http://suninjuly.github.io/registration2.html" # selenium.common.exceptions.NoSuchElementException
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_input = browser.find_element_by_xpath('//input[contains(@class, "first") and @required]')
    last_name_input = browser.find_element_by_xpath('//input[contains(@class, "second") and @required]')
    email_input = browser.find_element_by_xpath('//input[contains(@class, "third") and @required]')

    first_name_input.send_keys('Фамилия')
    last_name_input.send_keys('Имя')
    email_input.send_keys('test@test.org')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
