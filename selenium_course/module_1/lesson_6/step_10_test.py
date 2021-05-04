from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, '//*[@placeholder="Input your first name"]')
    first_name.send_keys('vasa')
    last_name = browser.find_element(By.XPATH, '//*[@placeholder="Input your last name"]')
    last_name.send_keys('sovsemvasa')
    email = browser.find_element(By.XPATH, '//*[@placeholder="Input your email"]')
    email.send_keys('qwerty@qweerty.com')
    phone = browser.find_element(By.XPATH, '//*[@placeholder="Input your phone:"]')
    phone.send_keys('98833377766')
    address = browser.find_element(By.XPATH, '//*[@placeholder="Input your address:"]')
    address.send_keys('fgshfsdh 12 sdafhsldfjasd 34')
    btn = browser.find_element(By.XPATH, '//*[@type="submit"]')
    btn.click()
    text = browser.find_element(By.TAG_NAME, 'h1')
    text1 = text.text
    assert "Congratulations! You have successfully registered!" == text1

finally:
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
