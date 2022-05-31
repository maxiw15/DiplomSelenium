from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем добавить в корзину
    button = browser.find_element(by=By.CSS_SELECTOR, value="btn btn-lg btn-primary btn-add-to-basket")
    button.click()

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.first")
    input1.send_keys("Ivan")



    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.browser.find_element(by=By.TAG_NAMENAME,value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

