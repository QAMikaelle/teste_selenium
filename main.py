from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.hml.lector.live/testesautomatizados/subscribe/login')
time.sleep(10)

usuario = driver.find_element(By.NAME, "login_username")

