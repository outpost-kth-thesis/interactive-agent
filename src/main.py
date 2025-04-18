from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver_path = "/usr/bin/chromedriver"
options = Options()
options.add_experimental_option("detach", False)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-data-dir=/tmp/chrome-data") 
options.add_argument("--enable-logging")
options.add_argument("--v=1")
options.add_argument("--disable-infobars")  # Disables the info bars
options.add_argument("--disable-extensions")  # Disables extensions

service = Service(executable_path=chromedriver_path)

options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

driver.get("https://kth.se/")


driver.close()
# combined_regex = '''//button | 
# //input[@type='button' or @type='submit' or @type='reset' or @type='text'] | 
# //textarea'''
# elements = driver.find_elements(By.XPATH, combined_regex)

# for el in elements:
#     parent1 = el.find_element(By.XPATH, "..")
#     parent2 = el.find_element(By.XPATH, "../..")
    
#     print("---")
#     print("Element HTML:")
#     print(el.get_attribute("outerHTML"))
    
#     print("Parent 1 HTML:")
#     print(parent1.get_attribute("outerHTML"))

#     print("Parent 2 HTML:")
#     print(parent2.get_attribute("outerHTML"))

