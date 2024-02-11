import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
input1.send_keys('Михаил')
input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
input2.send_keys('Соболев')
input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
input3.send_keys('sobolev@mail.ru')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
but = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
but.click()
time.sleep(6)