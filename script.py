from numpy.lib.shape_base import tile
from selenium import webdriver
from selenium import webdriver
import pandas as pd
from pymongo import MongoClient
from random import randint
# client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
# db=client.inde

# connection_string = "mongodb//172.20.0.1:27017/scrappingdb"
# client = MongoClient(connection_string)
# print(client.list_database_names)

connection_string = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false"
client = MongoClient(connection_string)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

import time


driver = webdriver.Chrome("/home/cheems/Downloads/chromedriver")



driver.get("https://in.indeed.com/jobs?q=python%20developer&l=india")
# driver.implicitly_wait(4)

try:
    pop= driver.find_element_by_class_name("[id='popover-x']")
    pop.click()
except:
    pass    

list_of_lists = []

list_of_page = ['title', 'company_location', 'job_location', 'rating', 'salary', 'short_description', 'date']

title =      []
company_location =    []
job_location = []
rating =     []
salary = []
short_description =   []
date =       []


# for i in range(len(list_of_page)):    
title = driver.find_elements_by_css_selector("[class='jobTitle jobTitle-color-purple']")
ti_new = []
print(len(title))
# print(ti_new)
# print(title)
for i in title:
    ti_new.append(i.text)
    print(i.text)
# print(title)
# for i in title:
#     print(i.text)

company_location = driver.find_elements_by_css_selector("[class='heading6 company_location tapItem-gutter']")
com_loc = []
print(len(company_location))
for i in company_location:
    com_loc.append(i.text)
    print(i.text)
job_location = driver.find_elements_by_css_selector("[class='companyLocation']")
print(len(job_location))
jo_l = []
for i in job_location:
    jo_l.append(i.text)
    print(i.text)
rating = driver.find_elements_by_css_selector("[class='ratingNumber']")
print(len(rating))
ra = []
for i in rating:
    ra.append(i.text)
    print(i.text)

salary = driver.find_elements_by_css_selector("[class='metadata salary-snippet-container']")
print(len(salary))
sal = []
for i in salary:
    sal.append(i.text)
    print(i.text)
short_description = driver.find_elements_by_css_selector("[class='job-snippet']")
print(len(short_description))
shor = []
for i in short_description:
    shor.append(i.text)
    print(i.text)
date = driver.find_elements_by_css_selector("[class='date']")
print(len(date))
de = []
for i in date:
    de.append(i)
    print(i)
        # long_description = driver.find_element_by_css_selector("[class='jobsearch-jobDescriptionText']").text
    # except as e:
    sleep(3)
    next_page = driver.find_element_by_css_selector("[aria-label='Next']").click()




    names = {'ti_new': ti_new,'com_loc': com_loc,'jo_l': jo_l, 'ra': ra, 'sal': sal,'shor': shor,'de': de}
    print(names)
    for x in names:
        inde = {
            'name' : names
        }
        print('data is inserting')
        db.collection.insert_one(inde)
        print('data is successfully going on db')





# # Creating the DataFrame
# df = pd.DataFrame(list_of_lists, columns=['ti_new', 'com_loc', 'jo_l', 'ra', 'sal', 'shor', 'de'])
# # Exporting the DataFrame as csv
# df.to_csv('indeed-new.csv', index=False, sep=';')


# mapped = zip(ti_new, com_loc, jo_l, ra, sal, shor, de)
# mapped = set(mapped)
# for i in mapped:
#     print(i)

# df = pd.DataFrame()

# df['title'] =      ti_new
# df['company_location'] =    com_loc
# df['job_location'] = jo_l
# df['rating'] =   ra
# df['salary'] =       sal
# df['short_description'] =    shor
# df['date'] =    de

# df.to_csv("Raw_Data.csv",index=None)

# for dataframe in dataframes:
#     if dataframe.columns.tolist() == ['Date', 'Price', 'Open', 'High', 'Low', 'Change%']:
#         df = dataframe
#         break

# frames.append(df)








































