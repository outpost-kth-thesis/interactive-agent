from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def get_all_form_elements(source_url):
    options = Options()
    options.add_experimental_option("detach", False)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-data-dir=/tmp/chrome-data-new") 
    options.add_argument("--enable-logging")
    options.add_argument("--v=1")
    options.add_argument("--disable-features=IdentityConsistency,SignInProfile,Signin")
    options.add_argument("--no-first-run")
    # options.add_argument("--proxy-server=http://localhost:8080")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    driver.get(source_url)



    combined_regex = '''//button | 
    //input[@type='button' or @type='submit' or @type='reset' or @type='text'] | 
    //textarea'''.strip()
    elements = driver.find_elements(By.XPATH, combined_regex)
    tags = []
    for el in elements:
        tag = el.find_element(By.XPATH, ".").get_attribute("outerHTML")
        tags.append(tag)

    driver.close()
    return tags

    # for el in elements:
    #     parent1 = el.find_element(By.XPATH, "..")
    #     parent2 = el.find_element(By.XPATH, "../..")
        
    #     print("---")
    #     print("Element HTML:")
    #     print(el.get_attribute("outerHTML"))




if __name__ == "__main__":
    print(get_all_form_elements("https://test-frontend-ssr.vercel.app/v2/v2/json"))