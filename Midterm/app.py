from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          # remove options if running locally
                          # options=options
                          )

PYTHON_URL = 'https://docs.python.org/3/tutorial/index.html'
wait = WebDriverWait(driver, 10)

# Go to https://docs.python.org/3/tutorial/index.html.
driver.get(PYTHON_URL)

# Select the language options on the navigation bar.
# Choose the Traditional Chinese option.
# Note that any selenium operation is legal except for changing the URL directly.

# why is this not working?
# select = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#language_select'))))

switchers = driver.find_element(By.CLASS_NAME, 'switchers')
placeholder = switchers.find_element(By.CLASS_NAME, 'language_switcher_placeholder')
language_select = placeholder.find_element(By.ID, 'language_select')
Select(language_select).select_by_value('zh-tw')

# Wait for lanugage translation.
wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Python 教學'))

# Use find_element to get the title and the first paragraph.
tutorial = driver.find_element(By.ID, 'the-python-tutorial')
title = tutorial.find_element(By.TAG_NAME, 'h1')
paragraphs = tutorial.find_elements(By.TAG_NAME, 'p')

# Print the title and the first paragraph.
print(title.text)
print(paragraphs[0].text)

print()

# Find the search box on the navigation bar.
inline_search = driver.find_element(By.CLASS_NAME, 'inline-search')
search_box = inline_search.find_element(By.NAME, 'q')

# Send keys to search for class.
# Note that any selenium operation is legal except for changing the URL directly.
search_box.send_keys('class')
search_box.submit()

# Use implicit or explicit wait in Selenium to wait for the searching result.
search_results = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search')))
wait.until(lambda _: len(search_results.find_elements(By.TAG_NAME, 'li')) >= 5)

# Print the top five listed titles.
# Note that you will get no point if you use sleep().
items = search_results.find_elements(By.TAG_NAME, 'li')
for item in items[:5]:
    print(item.find_element(By.TAG_NAME, 'a').text)

driver.close()
