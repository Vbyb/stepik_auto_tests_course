from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
but = browser.find_element(By.CLASS_NAME, 'btn')
but.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element(By.ID, 'input_value').text
y = calc(x)

inp = browser.find_element(By.ID, 'answer')
inp.send_keys(y)

but = browser.find_element(By.CLASS_NAME, 'btn')
but.click()

time.sleep(6)
