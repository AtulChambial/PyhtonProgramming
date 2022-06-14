# Test Case 2
# -----------
# 1) Open Web Browser(Chrome/firefox/IE).
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Provide Username (Admin).
# 4) Provide Password (admin123)
# 5) Click on Login.
# 6) Capture title of the dashboard page. (Actual title)
# 7) Verify title of the page: OrangeHRM (Expected)
# 8) Close browser

#Selenium 3
# from selenium import webdriver
#
#
# driver=webdriver.Chrome("D:\SDET- QA Automation Techie\Selenium with Python\Drivers\chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_name("txtPassword").send_keys("admin123")
# driver.find_element_by_name("btnLogin").click()
#
# act_title=driver.title
# excp_title="OrangeHRM"
#
# if act_title==excp_title:
#     print("Title is correct")
# else:
#     print("Title is incorrect")
#
# driver.close()


#selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\SDET- QA Automation Techie\Selenium with Python\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()

act_title=driver.title
excp_title="OrangeHRM"

if act_title==excp_title:
    print("Title is correct")
else:
    print("Title is incorrect")

driver.close()





