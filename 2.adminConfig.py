import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import selenium.webdriver
 
# Load the Excel file
# Fix the file path with a raw string
excel_file = r"C:/Users/Sharm/OneDrive/Desktop/sprint/entryValues.xlsx"
df = pd.read_excel(excel_file, sheet_name="adminConfig", engine='openpyxl')  # Adjust sheet name if needed
# print (df)
# if df.empty:
#     print("The Excel file is empty or the sheet name is incorrect.")
# else:
#     print("Excel Data Loaded Successfully!")
# Get the username value from a specific row and column
# username_value = df.iloc[0, 1]  # Replace "UserName" with your actual column name
# print(f"Username fetched from Excel: {username_value}")
# pwd_value = df.iloc[1, 1]  # Replace "UserName" with your actual column name
# Provide the path to the chromedriver executable using Service
chrome_service = Service(r"C:\Users\Sharm\Downloads\chromedriver-win64 1\chromedriver-win64\chromedriver.exe ")
tm = 5
# Initialize the WebDriver with the service object
driver = webdriver.Chrome(service=chrome_service)
 
# Open a website
driver.get("https://p-dev-cams.azurewebsites.net/login")
driver.maximize_window()
# Wait for the page to load
#time.sleep(tm)
# txtUserName = driver.find_element(By.ID, 'email')  # You can use By.NAME, By.XPATH, By.CSS_SELECTOR, etc.
# txtUserName.send_keys(username_value)  
driver.find_element(By.ID, 'email').send_keys(df.iloc[0, 1])
driver.find_element(By.ID, 'password').send_keys(df.iloc[1, 1])
# Locate the button and click it (replace 'button-id' with your button's actual ID)
driver.find_element(By.ID, ':r2:').click()  # You can also use By.XPATH, By.NAME, etc.
time.sleep(tm)
 
driver.get("https://p-dev-cams.azurewebsites.net/adminconfig")
time.sleep(tm)
wait = WebDriverWait(driver, 10)
dropdownTitle = wait.until(EC.element_to_be_clickable((By.ID, "controlled-demo")))
dropdownTitle.click()
 
xpath_expression = f"//li[contains(text(), '{df.iloc[2, 2]}')]"
print(f"fetched from Excel: {df.iloc[2, 2]}")
option = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
option.click()
 
driver.find_element(By.XPATH, "//button[contains(., 'Create')]").click()
time.sleep(tm)
# driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSecondary").click()
# time.sleep(tm)
 
# print(f"fetched from Excel: {df.iloc[3, 2]}")
# print(f"fetched from Excel: {df.iloc[4, 2]}")
driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[3, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[4, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)

driver.find_element(By.XPATH, "//button[contains(., 'Create')]").click()
time.sleep(tm)
driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[5, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[6, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)
 
driver.find_element(By.XPATH, "//button[contains(., 'Create')]").click()
time.sleep(tm)
driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[7, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[8, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)
 
driver.find_element(By.XPATH, "//button[contains(., 'Create')]").click()
time.sleep(tm)
driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[9, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[10, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)
 
driver.find_element(By.XPATH, "//button[contains(., 'Create')]").click()
time.sleep(tm)
driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[11, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[12, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)
 
driver.find_element(By.XPATH, "//button[contains(., 'Create')]").click()
time.sleep(tm)
driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[13, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[14, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)
 
designation = df.iloc[1, 5]
driver.find_element(By.ID, '').send_keys(designation)

dropdownTitle = wait.until(EC.element_to_be_clickable((By.ID, "controlled-demo")))
dropdownTitle.click()
xpath_expression = f"//li[contains(text(), '{df.iloc[15, 2]}')]"
print(f"fetched from Excel: {df.iloc[15, 2]}")
option = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
option.click()

driver.find_element(By.XPATH, "//button[contains(., 'Create')]").click()
time.sleep(tm)
driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[16, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[17, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)

driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[18, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[19, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)

driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[20, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[21, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)

driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[22, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[23, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)

driver.find_element(By.ID, 'sfmCode').send_keys(df.iloc[24, 2])
driver.find_element(By.ID, 'sfmValue').send_keys(df.iloc[25, 2])
time.sleep(tm)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']")))
close_button.click()
time.sleep(tm)


time.sleep(tm)
driver.quit()