from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//*[@placeholder='Enter first name']")
    input1.send_keys("Тест")

    input2 = browser.find_element_by_xpath("//*[@placeholder='Enter last name']")
    input2.send_keys("Тест")

    input3 = browser.find_element_by_xpath("//*[@placeholder='Enter email']")
    input3.send_keys("Тест")


    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()