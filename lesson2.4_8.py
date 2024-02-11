from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))

button = browser.find_element(By.ID, 'book')
button.click()
x = browser.find_element(By.CSS_SELECTOR, "span.nowrap#input_value").text
y = calc(x)
input1 = browser.find_element(By.ID, 'answer' )
input1.send_keys(y)
button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button1.click()
time.sleep(5)