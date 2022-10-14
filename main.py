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

params = {
    "latitude": 21.427526,
    "longitude": 39.271313,
    "accuracy": 100
}

driver.execute_cdp_cmd("Page.setGeolocationOverride", params)

#options = Options()
# options.add_argument("--window-size=1920,1200")
#options.headless = True
#chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
#driver = webdriver.Chrome(service=chrome_service,options=options)
# driver.quit()



# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

for i in range(0,5):
  date = datetime.today()
  folder = r' '.join(['-'.join([str(date.year),str(date.month),str(date.day)])])
  folder
  driver.set_page_load_timeout(5000)
  driver.get("https://www.google.com/maps/@21.5495652,39.1973127,11.65z/data=!5m1!1e1")
  time.sleep(3)
  driver.execute_script('document.getElementById("omnibox-container").remove()')
  # driver.execute_script('document.getElementById("itamenu").remove()')
  driver.execute_script('x = document.evaluate("/html/body/div[3]/div[9]/div[4]/div/div/div/div[1]/div/div/div/div",document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue')
  driver.execute_script('x.remove()')
  driver.execute_script('x = document.evaluate("//div[@data-ogsr-up]",document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue')
  driver.execute_script('x.remove()')
  driver.execute_script('x = document.evaluate("/html/body/div[3]/div[9]/div[22]",document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue')
  driver.execute_script('x.remove()')
  driver.execute_script('x = document.evaluate("/html/body/div[3]/div[9]/div[24]",document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue')
  driver.execute_script('x.remove()')
  driver.execute_script('x = document.evaluate("/html/body/div[3]/div[9]/div[1]/div[2]",document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue')
  driver.execute_script('x.remove()')
  canvas = driver.find_element(By.XPATH,'//div[contains(@aria-label,"خريطة")]')
  # actions = ActionChains(driver)
  # actions.click_and_hold(canvas)
  # action.perform()
  # time.sleep(1.5)
  # time
  # get the canvas as a PNG base64 string
  # decode

  # save to a file
  path = os.getcwd()
  path = path.replace('\\','/')
  folder = '/'.join([path,folder])
  if not (os.path.exists(folder)):
    os.makedirs(folder)



  with open(folder+r"/"+'-'.join([str(date.hour),str(date.minute),str(date.second)])+".png", 'wb') as f:
      f.write(canvas.screenshot_as_png)
  print(datetime.today())
  if i != 4:
      time.sleep(55)
driver.quit()

