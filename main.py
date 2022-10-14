import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

# params = {
#     "latitude": 21.427526,
#     "longitude": 39.271313,
#     "accuracy": 100
# }

# driver.execute_cdp_cmd("Page.setGeolocationOverride", params)

#options = Options()
# options.add_argument("--window-size=1920,1200")
#options.headless = True
#chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
#driver = webdriver.Chrome(service=chrome_service,options=options)
# driver.quit()



# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

driver.set_page_load_timeout(5000)
#driver.get("https://www.google.com/maps/@21.5495652,39.1973127,11.65z/data=!5m1!1e1")
driver.get("https://www.gps-coordinates.net/my-location")
time.sleep(3)
with open("page_source.html", "w") as f:
  f.write(driver.page_source)



driver.quit()

