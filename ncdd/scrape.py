# Selenium WebDriver Python coding
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
# The Select library operates the drop down list.
from selenium.webdriver.support.ui import Select
import time

import pandas as pd

wait_time_out = 10

url = 'http://mis.ncdd.gov.kh/dmk/View/Report/Report8.aspx'
driver = webdriver.Chrome()
driver.get(url)
wait_variable = W(driver, wait_time_out)


'''
*** Selector IDs ** 
StartYearID = ContentPlaceHolder1_ddlYear
NAME = ctl00$ContentPlaceHolder1$ddlYear

EndYearID = ContentPlaceHolder1_ddlYear 
NAME = ctl00$ContentPlaceHolder1$ddlYearEnd

dropdownID = ContentPlaceHolder1_ddlDistrict

clickID = ContentPlaceHolder1_Button1
'''

year_start = Select(wait_variable.until(E.presence_of_element_located((By.NAME, 'ctl00$ContentPlaceHolder1$ddlYear'))))
year_end = Select(wait_variable.until(E.presence_of_element_located((By.NAME, 'ctl00$ContentPlaceHolder1$ddlYearEnd'))))
dropdown = Select(wait_variable.until(E.presence_of_element_located((By.NAME, 'ctl00$ContentPlaceHolder1$ddlDistrict'))))
#btn_result = wait_variable.until(E.presence_of_element_located((By.NAME, 'ctl00$ContentPlaceHolder1$Button1')))
#btn_result = wait_variable.until(E.presence_of_element_located((By.CSS_SELECTOR, "input.submit[name = 'ctl00$ContentPlaceHolder1$Button1']")))

year_start.select_by_visible_text('2015')
time.sleep(1)
year_end.select_by_visible_text('2021')
time.sleep(1)

# change i for starting page to scrape
# unworking page numbers - 31,51,54,58,132
i = 133
max_file = 198

while i < max_file:
    for option in dropdown.options:
        #print(option.text)
        #dropdown.select_by_visible_text(option.text)
        #name = option.text 
        print("Page: "+ str(i))
        dropdown = Select(wait_variable.until(E.presence_of_element_located((By.NAME, 'ctl00$ContentPlaceHolder1$ddlDistrict'))))
        dropdown.select_by_index(i)
        time.sleep(1)
        #btn_result.click()
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(1)
        driver.find_element(By.ID, "ContentPlaceHolder1_LinkButtonWord").click()
        time.sleep(1)
        Html_file = open(str(i)+".html", "w" ,encoding='utf-8')
        time.sleep(4)
        Html_file.write(driver.page_source)
        Html_file.close()
            
        i += 1
driver.close()
