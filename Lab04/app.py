from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

myStudentID = "311551137"
NYCU_URL = "https://www.nycu.edu.tw/"
GOOGLE_URL = "https://www.google.com"

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          # remove options if running locally
                          options=options
                          )

wait = WebDriverWait(driver, 5)

driver.get(NYCU_URL)

driver.maximize_window()

news = wait.until(EC.presence_of_element_located((By.LINK_TEXT, '新聞')))
news.click()

all_news = wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, '.su-post > a')))
all_news[0].click()

title = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
contents = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'p')))
print(title.text)
for content in contents:
    print(content.text)

driver.switch_to.new_window('tab')
wait.until(EC.new_window_is_opened)

driver.get(GOOGLE_URL)

search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
search_box.send_keys(myStudentID)
search_box.submit()

all_titles = wait.until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, 'LC20lb.MBeuO.DKV0Md')))
print(all_titles[1].text)

driver.close()
