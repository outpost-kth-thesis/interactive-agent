from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_experimental_option("detach", True)
os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# options.add_argument("--proxy-server=http://127.0.0.1:8080")

driver = webdriver.Chrome(options=options)

driver.get("https://kth.se/")

driver.maximize_window()

combined_regex = '''//button | 
//input[@type='button' or @type='submit' or @type='reset' or @type='text'] | 
//textarea'''
elements = driver.find_elements(By.XPATH, combined_regex)

for el in elements:
    parent1 = el.find_element(By.XPATH, "..")
    parent2 = el.find_element(By.XPATH, "../..")
    
    print("---")
    print("Element HTML:")
    print(el.get_attribute("outerHTML"))
    
    print("Parent 1 HTML:")
    print(parent1.get_attribute("outerHTML"))

    print("Parent 2 HTML:")
    print(parent2.get_attribute("outerHTML"))

