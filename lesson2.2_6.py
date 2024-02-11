from selenium import webdriver
import time, math
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.CSS_SELECTOR, "span.nowrap#input_value").text
button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
browser.execute_script("window.scrollBy(0, 100);")
y = calc(x)
input1 = browser.find_element(By.ID, 'answer' )
input1.send_keys(y)
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = browser.find_element(By.ID, "robotsRule")
option2.click()
button.click()
time.sleep(4)
browser.quit()