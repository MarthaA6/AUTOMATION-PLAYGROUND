from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver using WedDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()
time.sleep(5)

# LOGIN PAGE ----------------------------------------------------------------------------------------------------------
# Locate the email address and password
EmailAddress = driver.find_element(By.XPATH,
                                   '//*[@id="email-id"]')
EmailAddress.send_keys("asdfg@test.com")
time.sleep(5)

Password = driver.find_element(By.XPATH,
                               '//*[@id="password"]')
Password.send_keys("12345")
time.sleep(5)

RememberMe_CheckBox = driver.find_element(By.XPATH,
                                          '//*[@id="remember"]')
RememberMe_CheckBox.click()
time.sleep(5)

Submit_Button = driver.find_element(By.XPATH,
                                    '//*[@id="submit-id"]')
Submit_Button.click()
time.sleep(5)

# SEARCH FIELD --------------------------------------------------------------------------------------------------------
Search = driver.find_element(By.CSS_SELECTOR,
                             'body > nav > input')
Search.send_keys("Mark")
time.sleep(5)

# ACTION COLUMN -------------------------------------------------------------------------------------------------------
# EDIT BUTTON ---------------------------------------------------------------------------------------------------------
Edit_Button = driver.find_element(By.CSS_SELECTOR,
                                  '#customers > tbody > tr:nth-child(1) > td:nth-child(5) > a:nth-child(1) > i')
Edit_Button.click()
time.sleep(5)

BackToCustomer_Button = driver.find_element(By.CSS_SELECTOR,
                                            '#customers')
BackToCustomer_Button.click()
time.sleep(5)

# DELETE BUTTON -------------------------------------------------------------------------------------------------------
Delete_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#customers > tbody > tr:nth-child(1) > td:nth-child(5) > a:nth-child(2) > i')
Delete_Button.click()
time.sleep(5)

# PAGE NAVIGATION BUTTON ----------------------------------------------------------------------------------------------
# NEXT BUTTON ---------------------------------------------------------------------------------------------------------
Next_Button = driver.find_element(By.CSS_SELECTOR,
                                  'body > div > div > nav > ul > li:nth-child(5) > a')
Next_Button.click()
time.sleep(5)

# PREVIOUS BUTTON -----------------------------------------------------------------------------------------------------
Previous_Button = driver.find_element(By.CSS_SELECTOR,
                                      'body > div > div > nav > ul > li:nth-child(1) > a')
Previous_Button.click()
time.sleep(5)

# 1 NEW CUSTOMER PAGE -------------------------------------------------------------------------------------------------
NewCustomer1_Button = driver.find_element(By.CSS_SELECTOR,
                                          '#new-customer')
NewCustomer1_Button.click()
time.sleep(5)

Cancel_Button = driver.find_element(By.XPATH,
                                    '//*[@id="loginform"]/div/div/div/div/form/a')
Cancel_Button.click()
time.sleep(5)

# 2 NEW CUSTOMER PAGE -------------------------------------------------------------------------------------------------
NewCustomer2_Button = driver.find_element(By.CSS_SELECTOR,
                                          '#new-customer')
NewCustomer2_Button.click()
time.sleep(5)

EnterEmail = driver.find_element(By.XPATH,
                                 '//*[@id="EmailAddress"]')
EnterEmail.send_keys("martha@test.com")
time.sleep(5)

FirstName = driver.find_element(By.XPATH,
                                '//*[@id="FirstName"]')
FirstName.send_keys("Martha")
time.sleep(5)

LastName = driver.find_element(By.XPATH,
                               '//*[@id="LastName"]')
LastName.send_keys("Sylvia")
time.sleep(5)

City = driver.find_element(By.XPATH,
                           '//*[@id="City"]')
City.send_keys("Lagos")
time.sleep(5)

State_Button = driver.find_element(By.XPATH,
                                   '//*[@id="StateOrRegion"]')
State_Button.click()
time.sleep(5)

GenderMale_Button = driver.find_element(By.XPATH,
                                        '//*[@id="loginform"]/div/div/div/div/form/div[6]/input[1]')
GenderMale_Button.click()
time.sleep(5)

GenderFemale_Button = driver.find_element(By.XPATH,
                                          '//*[@id="loginform"]/div/div/div/div/form/div[6]/input[2]')
GenderFemale_Button.click()
time.sleep(5)

# AddToPromotionalList_Checkbox = driver.find_element(By.XPATH,
#                                                     '//*[@id="loginform"]/div/div/div/div/form/div[7]/input')
# AddToPromotionalList_Checkbox.click()
# time.sleep(5)

Submit1_Button = driver.find_element(By.XPATH,
                                     '//*[@id="loginform"]/div/div/div/div/form/button')
Submit1_Button.click()
time.sleep(5)

# SIGN OUT BUTTON
SignOut_Button = driver.find_element(By.CSS_SELECTOR,
                                     'body > nav > ul > li > a')
SignOut_Button.click()
time.sleep(5)

# Close the browser
driver.quit()