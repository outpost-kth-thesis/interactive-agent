# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Added import for Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
exe_path = '/usr/bin/vivaldi'
driver = webdriver.Chrome(executable_path=exe_path, options=options)

# Navigate to the GeeksforGeeks website
driver.get("https://www.geeksforgeeks.org/")

# Maximize the browser window
driver.maximize_window()
