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
excel_file = "C:\\Users\Sharm\OneDrive\Desktop\sprint\entryValues.xlsx"  # Replace with the actual file path
df = pd.read_excel(excel_file, sheet_name="nonDocSave")  # Adjust sheet name if needed
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
chrome_service = Service(r"C:\Users\Sharm\Downloads\chromedriver-win64 1\chromedriver-win64\chromedriver.exe")
tm = 5
# Initialize the WebDriver with the service object
driver = webdriver.Chrome(service=chrome_service)

# Open a website
driver.get("https://dev-cams.azurewebsites.net/login") 
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

driver.get("https://dev-cams.azurewebsites.net/users")
time.sleep(tm)
#open save user page
driver.find_element(By.XPATH, "//button[contains(., 'Create')]").click()
time.sleep(tm)
driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSecondary").click()
time.sleep(tm)
driver.find_element(By.XPATH, "//button[contains(., 'Clear')]").click()
time.sleep(tm)
wait = WebDriverWait(driver, 10)
# doctor Nondoctor
non_doctor_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[span[text()='Non Doctor']]")))
non_doctor_label.click()
# user title
dropdownTitle = wait.until(EC.element_to_be_clickable((By.ID, "usrTitle")))
dropdownTitle.click()
xpath_expression = f"//li[contains(text(), '{df.iloc[2, 1]}')]"
option = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
option.click()
# firstname
driver.find_element(By.ID, 'usrFirstName').send_keys(df.iloc[3, 1])
# last name
driver.find_element(By.ID, 'usrLastName').send_keys(df.iloc[4, 1])
# gender
dropdownTitle = wait.until(EC.element_to_be_clickable((By.ID, "gender")))
dropdownTitle.click()
xpath_expression = f"//li[contains(text(), '{df.iloc[5, 1]}')]"
option = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
option.click()
#  email
driver.find_element(By.ID, 'usrEmailId').send_keys(df.iloc[6, 1])
#  usrcode
driver.find_element(By.ID, 'usrCode').send_keys(df.iloc[7, 1])
# department
dropdownTitle = wait.until(EC.element_to_be_clickable((By.ID, "departmentId")))
dropdownTitle.click()
xpath_expression = f"//li[contains(text(), '{df.iloc[8, 1]}')]"
option = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
option.click()
# designation
dropdownTitle = wait.until(EC.element_to_be_clickable((By.ID, "designationId")))
dropdownTitle.click()
xpath_expression = f"//li[contains(text(), '{df.iloc[9, 1]}')]"
option = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
option.click()
# usercode
dropdownRole = wait.until(EC.element_to_be_clickable((By.ID, "userRole")))
dropdownRole.click()
wait.until(EC.presence_of_element_located((By.XPATH, "//ul/li")))
management_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(., 'Management')]")))
management_checkbox.click()
actions = ActionChains(driver)
actions.move_by_offset(0, 100).click().perform()  
# Branch
dropdownbranch = wait.until(EC.element_to_be_clickable((By.ID, "branches")))
dropdownbranch.click()
xpath_expression = f"//li[contains(text(), '{df.iloc[11, 1]}')]"
option = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
option.click()
#  address
driver.find_element(By.ID, 'usrAddress').send_keys(df.iloc[12, 1])
time.sleep(tm)
# # save
# driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSecondary").click()
# time.sleep(tm)

create_Back = driver.find_element(By.XPATH, "//button[contains(., 'Back')]")
create_Back.click()

time.sleep(tm)
driver.quit()







# remove from here
# #ASK AI
# try:
#     lnkAskMe =  WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID, 'lnkBtnAskMe'))) #driver.find_element(By.ID, 'lnkBtnAskMe')
#     lnkAskMe.click()
#     time.sleep(tm)

#     textSearch = driver.find_element(By.ID, 'txt_Search')
#     textSearch.send_keys("Academy at CTC")
#     btnTextSearch = driver.find_element(By.ID, 'txtSearchButton')
#     btnTextSearch.click();
#     time.sleep(20)

#     clearbtn = driver.find_element(By.ID, 'ClearAllSearchFiltersBtn')
#     clearbtn.click();
#     time.sleep(3)

#     fileSearch = driver.find_element(By.ID, 'txt_Search')
#     fileSearch.send_keys("Dartmouth Hitchcock")
#     btnfileSearch = driver.find_element(By.ID, 'fileSearchButton')
#     btnfileSearch.click();
#     time.sleep(15)

# except TimeoutException:
#     try:
#         lnkAskMe =  WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div>ul>li.nav-item>a'))) #driver.find_element(By.ID, 'lnkBtnAskMe')
#         driver.get(lnkAskMe.get_attribute('href'))
#         time.sleep(tm)

#         textSearch = driver.find_element(By.ID, 'txt_Search')
#         textSearch.send_keys("Academy at CTC")
#         btnTextSearch = driver.find_element(By.ID, 'txtSearchButton')
#         btnTextSearch.click();
#         time.sleep(15)

#         clearbtn = driver.find_element(By.ID, 'ClearAllSearchFiltersBtn')
#         clearbtn.click();
#         time.sleep(3)

#         fileSearch = driver.find_element(By.ID, 'txt_Search')
#         fileSearch.send_keys("Dartmouth Hitchcock")
#         btnfileSearch = driver.find_element(By.ID, 'fileSearchButton')
#         btnfileSearch.click();
#         time.sleep(15)
#     except TimeoutException:
#         print("Timed out waiting for page to load")

# #Home Page
# lnkSubMenuHome =  driver.find_element(By.ID, 'SubMenuHome')
# lnkSubMenuHome.click()
# time.sleep(tm)
# #Task Open from Home

# # try:
# #     lnkSubMenuHome = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID, 'btnViewAllDeliverables')))
# #     #lnkSubMenuHome =  driver.find_element(By.ID, 'btnViewAllDeliverables')
# #     lnkSubMenuHome.click()
# #     time.sleep(tm)
# # except TimeoutException:
# #     print("Timed out waiting for page to load")

# #Project Details
# try:
#    lnkSubMenuDirectory =  WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID, 'SubMenuDirectory'))) #driver.find_element(By.ID, 'SubMenuDirectory')
#    lnkSubMenuDirectory.click()
#    time.sleep(tm)
# except TimeoutException:
#    print("Timed out waiting for page to load")

# lnkSubMenuProjects =  driver.find_element(By.ID, 'SubMenuProjects')
# lnkSubMenuProjects.click()
# time.sleep(tm)

# try:
#     prjEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.p0>a")))
#     driver.get(prjEle1.get_attribute('href'))
#     time.sleep(tm)

#     PrjEditBtn = driver.find_element(By.ID, 'editbtn')
#     PrjEditBtn.click()
#     time.sleep(tm)

#     PrjCancelBtn = driver.find_element(By.ID, 'editbtn')
#     PrjCancelBtn.click()
#     time.sleep(tm)
# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     prjEle2 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.hideOverflow>a")))
#     driver.get(prjEle2.get_attribute('href'))
#     time.sleep(tm)

#     PrjExpandBtn = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID, 'expandbtn')))#driver.find_element(By.ID, 'expandbtn')
#     PrjExpandBtn.click()
#     time.sleep(tm)

#     PrjCollBtn = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID, 'expandbtn'))) #driver.find_element(By.ID, 'expandbtn')
#     PrjCollBtn.click()
#     time.sleep(tm)

#     PrjEditBtn = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID, 'editbtn'))) #driver.find_element(By.ID, 'editbtn')
#     PrjEditBtn.click()
#     time.sleep(tm)

#     PrjCancelBtn = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID, 'editbtn'))) #driver.find_element(By.ID, 'editbtn')
#     PrjCancelBtn.click()
#     time.sleep(tm)

#     # try:
#     #   PrjAddFolder = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID, 'addDocuments'))) #driver.find_element(By.ID, 'addDocuments')
#     #   PrjAddFolder.click()
#     #   time.sleep(tm)
#     # except TimeoutException:
#     #   print("Timed out waiting for page to load")

#     # PrjCancelFolder = driver.find_element(By.ID, 'TabCancel')
#     # PrjCancelFolder.click()
#     # time.sleep(tm)

#     # try:
#     #   prjEle2 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-11.p0>a")))
#     #   prjEle2.click()
#     #   time.sleep(tm)
#     # except TimeoutException:
#     #   print("Timed out waiting for page to load")
# except TimeoutException:
#     print("Timed out waiting for page to load")


# #Employee Details 
# lnkSubMenuDirectory =  driver.find_element(By.ID, 'SubMenuDirectory')
# lnkSubMenuDirectory.click()
# time.sleep(tm)

# lnkSubMenuEmps =  driver.find_element(By.ID, 'SubMenuUsers')
# lnkSubMenuEmps.click()
# time.sleep(tm)

# try:
#     empEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-11.p0>a")))
#     driver.get(empEle1.get_attribute('href'))
#     time.sleep(tm) 
#    #  empedit = driver.find_element(By.ID, 'EditAM')
#    #  empedit.click()
#    #  time.sleep(8)  
# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     empEle2 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-2.hideOverflow>a")))
#     driver.get(empEle2.get_attribute('href'))
#     time.sleep(tm)
#     empedit = driver.find_element(By.ID, 'EditAM')
#     empedit.click()
#     time.sleep(tm)
#     cancelaboutEmp = driver.find_element(By.ID, 'CancelAboutMe')
#     cancelaboutEmp.click()
#     canceloffEmp = driver.find_element(By.ID, 'CancelUserOfficeAddressUpdate')
#     canceloffEmp.click()    
# except TimeoutException:
#     print("Timed out waiting for page to load")


# #Contacts Details 
# lnkSubMenuDirectory =  driver.find_element(By.ID, 'SubMenuDirectory')
# lnkSubMenuDirectory.click()
# time.sleep(tm)

# lnkSubMenuConts =  driver.find_element(By.ID, 'SubMenuContacts')
# lnkSubMenuConts.click()
# time.sleep(tm)

# try:
#     contEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.p0>a")))
#     driver.get(contEle1.get_attribute('href'))
#     time.sleep(tm)   
# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     contEle2 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-3>a")))
#     driver.get(contEle2.get_attribute('href'))
#     time.sleep(tm)    
# except TimeoutException:
#     print("Timed out waiting for page to load")


# #Organization Details 
# lnkSubMenuDirectory =  driver.find_element(By.ID, 'SubMenuDirectory')
# lnkSubMenuDirectory.click()
# time.sleep(tm)

# lnkSubMenuOrgs =  driver.find_element(By.ID, 'SubMenuOrganizations')
# lnkSubMenuOrgs.click()
# time.sleep(tm)

# try:
#     orgEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-11.p0>a")))
#     driver.get(orgEle1.get_attribute('href'))
#     time.sleep(tm)   
# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     orgEle2 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-3>a")))
#     driver.get(orgEle2.get_attribute('href'))
#     time.sleep(tm)    
# except TimeoutException:
#     print("Timed out waiting for page to load")

# #Facilities Details 
# lnkSubMenuDirectory =  driver.find_element(By.ID, 'SubMenuDirectory')
# lnkSubMenuDirectory.click()
# time.sleep(tm)

# lnkSubMenuFacis =  driver.find_element(By.ID, 'SubMenuFacilities')
# lnkSubMenuFacis.click()
# time.sleep(tm)

# try:
#     facEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-3>a")))
#     driver.get(facEle1.get_attribute('href'))
#     time.sleep(tm)  
#     try:
#        subfaciele = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div>span.hideOverflow>a")))
#        driver.get(subfaciele.get_attribute('href'))
#        time.sleep(tm)
#        try:
#          faciGrpele = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.breaklinelarge>span.hideOverflow>a")))
#          driver.get(faciGrpele.get_attribute('href'))
#          time.sleep(tm)
#        except TimeoutException :
#          print("Timed out waiting for page to load") 
#     except TimeoutException:
#       print("Timed out waiting for page to load")  

# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     facEle2 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-3>a")))
#     driver.get(facEle2.get_attribute('href'))
#     time.sleep(tm)    
# except TimeoutException:
#     print("Timed out waiting for page to load")

# #WorkGroups Details
# lnkSubMenuWGs =  driver.find_element(By.ID, 'SubMenuWorkgroups')
# lnkSubMenuWGs.click()
# time.sleep(tm)

# try:
#     wgEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-3>a")))
#     driver.get(wgEle1.get_attribute('href'))
#     time.sleep(tm)  
#     try:
#         wgDF = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID,'btnDown')))
#         wgDF.click()
#         time.sleep(tm)

#         wgOpenFold = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.col-sm-11.p0>a")))
#         wgOpenFold.click()
#         time.sleep(tm)

#     except TimeoutException:
#         print("Timed out waiting for page to load")  
# except TimeoutException:
#     print("Timed out waiting for page to load")


# #Plans Details
# try:
#     lnkSubMenuPlans =  WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID,"SubMenuPlans"))) #driver.find_element(By.ID, 'SubMenuPlans')
#     lnkSubMenuPlans.click()
#     time.sleep(tm)
#     try:
#         planEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div>span>a")))
#         driver.get(planEle1.get_attribute('href'))
#         time.sleep(tm)

#         planlevelViewEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID,"planViewNextLevel")))
#         planlevelViewEle1.click()
#         time.sleep(tm) 

#         planbackEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div>span.breadcrumb-default>a")))
#         driver.get(planbackEle1.get_attribute('href'))
#         time.sleep(tm)  

#         planlevelEditEle1 = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID,"planEditNextLevel")))
#         planlevelEditEle1.click()
#         time.sleep(tm)
#     except TimeoutException:
#         print("Timed out waiting for page to load")
# except TimeoutException:
#     print("Timed out waiting for page to load")

# #Shared Plans
# try:
#     lnkSubMenuPlans =  WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID,"SubMenuPlans")))
#     lnkSubMenuPlans.click()
#     time.sleep(tm)

#     sharedPlans =  driver.find_element(By.ID, 'DefaultSharedPlansTabId')
#     sharedPlans.click()
#     time.sleep(tm)

#     try:
#         sharedPlanele = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.short-text100>span.hideOverflow>a")))
#         driver.get(sharedPlanele.get_attribute('href'))
#         time.sleep(tm)
#         sharedPlanViewele = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.ID,"planViewNextLevel")))
#         sharedPlanViewele.click()
#         time.sleep(tm)
#     except TimeoutException:
#         print("Timed out waiting for page to load")
# except TimeoutException:
#     print("Timed out waiting for page to load")

# #Reports Details
# lnkSubMenuReports =  driver.find_element(By.ID, 'SubMenuSummary')
# lnkSubMenuReports.click()
# time.sleep(tm)

# #Home Page my posts
# lnkSubMenuHome =  driver.find_element(By.ID, 'SubMenuHome')
# lnkSubMenuHome.click()
# time.sleep(tm)

# try:
#     myposthome = WebDriverWait(driver, tm).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div>span>b>a')))
#     driver.get(myposthome.get_attribute('href'))
#     time.sleep(tm)
# except TimeoutException:
#     print("Timed out waiting for page to load")

# #Home Page my Connections
# lnkSubMenuHome =  driver.find_element(By.ID, 'SubMenuHome')
# lnkSubMenuHome.click()
# time.sleep(tm)

# try:
#     myConhome = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div>div.rightsidecontant>a')))
#     driver.get(myConhome.get_attribute('href'))
#     time.sleep(tm)
# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     contactAskAI = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.col-sm-3>ul>li>a#SubMenuSemantic')))
#     driver.get(contactAskAI.get_attribute('href'))
#     time.sleep(tm)

#     textSearch = driver.find_element(By.ID, 'txt_Search')
#     textSearch.send_keys("Text Search")
#     btnTextSearch = driver.find_element(By.ID, 'txtSearchButton')
#     btnTextSearch.click();
#     time.sleep(20)

#     clearbtn = driver.find_element(By.ID, 'ClearAllSearchFiltersBtn')
#     clearbtn.click();
#     time.sleep(3)

#     fileSearch = driver.find_element(By.ID, 'txt_Search')
#     fileSearch.send_keys("File Search")
#     btnfileSearch = driver.find_element(By.ID, 'fileSearchButton')
#     btnfileSearch.click();
#     time.sleep(15)

# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     contactHome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.col-sm-3>ul>li>a#SubMenuHome')))
#     driver.get(contactHome.get_attribute('href'))
#     time.sleep(tm)
# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     contactHome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.col-sm-3>ul>li>a#SubMenuProjects')))
#     driver.get(contactHome.get_attribute('href'))
#     time.sleep(tm)
# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     contactHome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.col-sm-3>ul>li>a#SubMenuWorkgroups')))
#     driver.get(contactHome.get_attribute('href'))
#     time.sleep(tm)
# except TimeoutException:
#     print("Timed out waiting for page to load")

# try:
#     contactHome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.col-sm-3>ul>li>a#SubMenuSummary')))
#     driver.get(contactHome.get_attribute('href'))
#     time.sleep(tm)
# except TimeoutException:
#     print("Timed out waiting for page to load")

# '''
# lnkPrjDV =  driver.find_element(By.ID, 'bt-detail-view')
# lnkPrjDV.click()
# time.sleep(tm)
# #bt-listgrid-view


# project_container = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.ID, 'projectContainer_175'))
# )
# time.sleep(tm)
# # Locate the button within the projectContainer_175 section
# btn_folder_file_group_drop = project_container.find_element(By.ID, 'PrjListrDirGroupDrop')
# time.sleep(tm)
# # Click the button
# btn_folder_file_group_drop.click()

# time.sleep(tm)

# '''



# #link = driver.find_element(By.XPATH, '//a[@href="https://www.targetwebsite.com"]')

# # Wait for some time to observe the action
# # time.sleep(tm)

# # Close the browser after some time
# #driver.quit()
