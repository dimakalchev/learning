import os
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ["PATH"] += r"C:/SeleniumDrivers"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://demo.automationtesting.in/JqueryProgressBar.html")
driver.implicitly_wait(3)
my_element = driver.find_element(By.ID, "downloadButton")
my_element.click()



WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"), # Element filtration
        "Complete!"# The expected text
    )
)

