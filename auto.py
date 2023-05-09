#!/usr/bin/env python
# coding: utf-8

# In[17]:


#!/usr/bin/env python
# coding: utf-8

# In[69]:


#-------------------------------------------------------------------------------
# Imports
import csv
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#-------------------------------------------------------------------------------
# Setup
# Read CSV file from here
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
#-------------------------------------------------------------------------------
# # Web Automation


        driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://techvision.qubators.org/enroll')
        #chrome driver setup
        
        time.sleep(5)
        
        #Finding email id block
        email_form = driver.find_element(By.ID,"rg_email")
        #Inserting email id into the email id block
        email_form.send_keys(line[4])
        
        #Finding Name Blcok
        name_form = driver.find_element(By.ID,"rg_name")
        #Insert name into name block
        name_form.send_keys(line[1])
        
        phone_form = driver.find_element(By.ID,"rg_phone")
        phone_form.send_keys(line[5])
        
        comment_form = driver.find_element(By.ID,"rg_comment")
        comment_form.send_keys(line[6])
        
        title_form = driver.find_element(By.ID,"rg_title")
        select = Select(title_form)
        
        #########################################################################################
        ##### We are selecting gender dropdown and selecting gender on basis of value from csv
        try:
            print(line[0])
            if line[0] == 'ï»¿Mr.':
                line[0]="Mr."
            select.select_by_visible_text(line[0])
        except:
            select.select_by_visible_text("N/A")
        
        gender_form = driver.find_element(By.ID,"rg_gender")
        select = Select(gender_form)
        try:
            select.select_by_visible_text(line[2])
        except:
            select.select_by_visible_text("Male")
        ####################################################################
        
        ###################################################################
        ##### Selecting category on basis of input from csv###############
        category_form = driver.find_element(By.ID,"rg_tech_cate")
        select = Select(category_form)
        try:
            if line[3].startswith("Tech Developer"):
                select.select_by_visible_text("Tech Developer (software & hardware)")
            elif line[3].startswith("Media Professional"):
                select.select_by_visible_text("Media Professional (in all fields)")
            else:
                select.select_by_visible_text(line[3])
        except:
            select.select_by_visible_text("Tech Enthusiast")
        ################################################################################
        
        
        #selecting register button and clicking it    
        submit = driver.find_element(By.ID,"techvisionFormBtn").submit()
#         driver.execute_script("arguments[0].click();", submit)
        time.sleep(10)
        driver.close()

#-------------------------------------------------------------------------------


# In[ ]:




