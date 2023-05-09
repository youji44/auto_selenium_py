ˀ#-------------------------------------------------------------------------------
# Imports
import csv
import requests
from selenium import webdriver
import time

#-------------------------------------------------------------------------------
# Setup

email = 0

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://recreatingyourworld.org/pixpopup-item/download-popup/')

        time.sleep(10)

        email_field = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div[5]/div/div/form/div[2]/p/label/span/input')
        email_field.send_keys(line[0])

        submit = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div[5]/div/div/form/div[2]/p/input')
        submit.click()

        driver.close()

#-------------------------------------------------------------------------------
