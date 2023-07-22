# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:58:26 2020

@author: Tyler A Bershad
Last Modified: 6/27/2020
Code Sample:
    This code was written to show that we can export data in an automated fashion.
    The code will open google chrome, go to our slack analytics dashboard, and
    export data from the last 30 days. 
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#choose your web driving browser - it must be in the path.
driver = webdriver.Chrome('./chromedriver')

#Go to the page of interest
driver.get("*****Workspace Admin Login******") #Ex: https://<workspacename>.slack.com/admin/stats 
print(driver.title)

#Find elements of interest within source code
user_bar = driver.find_element_by_name("email")
user_bar.clear()
user_bar.send_keys("*******YOUR EMAIL*********") #Change
pwrd_bar = driver.find_element_by_name("password")
pwrd_bar.clear()
pwrd_bar.send_keys("******YOU PASSWORD GOES HERE******") #Change
pwrd_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.maximize_window();

#Downloads 
export = driver.find_element_by_class_name('ent_csv_popover__btn.btn_outline.btn')
export.send_keys(Keys.RETURN)

#After 15 seconds close the window
time.sleep(15)
driver.close()
