from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

myStudentID = "311551137"

# launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# navigate to NYCU home page(https://www.nycu.edu.tw/)
driver.get("https://www.nycu.edu.tw/")

# maximize the window
driver.maximize_window()

# click 新聞
driver.find_element(By.LINK_TEXT, '新聞').click()

# click first new
driver.find_element(By.XPATH, '//li[@class="su-post"]/a[1]').click()

# print the title and content
print(driver.find_element(
    By.XPATH, '//header[@class="entry-header clr"]/h1').text)
contents = driver.find_elements(
    By.XPATH, '//div[@class="entry-content clr"]/p')
for content in contents:
    print(content.text)

# open a new tab and switch to it
driver.switch_to.new_window('tab')

# navigate to google
driver.get("https://www.google.com")

# input your student number and submit
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys(myStudentID)
search_box.send_keys(Keys.RETURN)

# print the title of second result
WebDriverWait(driver, 5).until(EC.new_window_is_opened)
print(driver.find_element(
    By.XPATH, '//div[@class = "v7W49e"]/div[2]/div/div/div/div/a/h3').text)

# close the browser
driver.close()
