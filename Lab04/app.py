from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

myStudentID = "311551137"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 2)

driver.get("https://www.nycu.edu.tw/")

driver.maximize_window()

news = wait.until(EC.presence_of_element_located((By.LINK_TEXT, '新聞')))
news.click()

first_news = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//li[@class="su-post"]/a[1]')))
first_news.click()

title = wait.until(EC.presence_of_element_located((
    By.XPATH, '//header[@class="entry-header clr"]/h1')))
contents = wait.until(EC.presence_of_all_elements_located((
    By.XPATH, '//div[@class="entry-content clr"]/p')))
print(title.text)
for content in contents:
    print(content.text)

driver.switch_to.new_window('tab')
wait.until(EC.new_window_is_opened)

driver.get("https://www.google.com")

search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
search_box.send_keys(myStudentID)
search_box.send_keys(Keys.RETURN)

second_title = wait.until(EC.presence_of_element_located((
    By.XPATH, '//div[@class = "v7W49e"]/div[2]/div/div/div/div/a/h3')))
print(second_title.text)

driver.close()
