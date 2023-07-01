import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ["PATH"] += r"C:/SeleniumDrivers"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.automationtesting.in/Register.html")
driver.implicitly_wait(5)
name = driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/form/div[1]/div[1]/input")
name.send_keys("Dima")
surname = driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/form/div[1]/div[2]/input")
surname.send_keys("Kalchev")

phone = driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/form/div[4]/div/input")
phone.send_keys(Keys.ADD, Keys.NUMPAD3, Keys.NUMPAD8, Keys.NUMPAD0)
try:
    male = driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/form/div[5]/div/label[1]/input" )
    male.click()
except:
    print("Error")

btn = driver.find_element(By.CSS_SELECTOR, "button[name='signup']")
btn.click()