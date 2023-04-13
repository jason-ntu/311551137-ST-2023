from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Q2-1
# Go to https: // docs.python.org/3/tutorial/index.html. (2 %)
# Select the language options on the navigation bar (Fig. 1), and choose the Traditional Chinese option. Note that any selenium operation is legal except for changing the URL directly. (10 %)
# Wait for lanugage translation, then use find_element to get the title and the first paragraph (Fig. 2). Print the title and the first paragraph. (3 %)

PYTHON_URL = "https://docs.python.org/3/tutorial/index.html"

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
# remove options if running locally
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 5)

driver.get(PYTHON_URL)

# 找到语言选择下拉菜单元素并点击
language_menu = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//select[@id="language_select"]/option[@value="zh-tw"]')))
language_menu.click()

# 找到繁体中文选项并点击
# traditional_option = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//option[@value='zh-tw']")))
# traditional_option.click()