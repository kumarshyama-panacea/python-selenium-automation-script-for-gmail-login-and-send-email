###################################################
#
# FIle Name:  Python + Selenium based code for Gmail Sending email Automation Script
# Author:     Kumar Shyama
# Version:     1.0
#
###################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Maximize window of chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Driver Load & providing path of chromedriver where I have placed this
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=options)

browser.get('http://gmail.com')

action = webdriver.ActionChains(browser)

emailElem = browser.find_element_by_id('identifierId').send_keys('testuserone90@gmail.com')
nextButton = browser.find_element_by_id('identifierNext').click()
time.sleep(1)

passwordElem = browser.find_element_by_name('password').send_keys('Account@123')
signinButton = browser.find_element_by_id('passwordNext').click()
time.sleep(10)

# Open compose email
composeEmail = browser.find_element_by_css_selector('.z0 div').click()
time.sleep(1)

# Class name of "to" field of email composer might be changed
browser.execute_script("var ele=document.getElementsByClassName('vO')[0];  ele.innerHTML = 'shyam123.ckp@gmail.com';")
time.sleep(1)

# Email Subject
subject = browser.find_element_by_name('subjectbox').send_keys('Test Email via selenium automation')
time.sleep(1)

# Email Content
browser.execute_script("var ele2=document.getElementsByClassName('editable')[0];  ele2.innerHTML = 'my new content123';")
time.sleep(1)

# Class name of "send" button on email composer might be changed
composeEmail9 = browser.find_element_by_css_selector('div.aoO')
composeEmail9.click()
time.sleep(1)




