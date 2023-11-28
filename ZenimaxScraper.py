#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

#Website: https://jobs.zenimax.com/jobs

#Create driver
driver = webdriver.Chrome()

#Connect to browser
driver.get("https://jobs.zenimax.com/jobs")

#Wait
driver.implicitly_wait(2)

#Lists are parallel
#Create a list of all jobtitles
job_titles = driver.find_elements(By.CLASS_NAME, "job-title")
title_list = []
for title in job_titles:
    title_list.append(title.text)
title_list.pop(0)

#Create list of departments
departments = driver.find_elements(By.CLASS_NAME, "job-department.pl-md-3")
department_list = []
i = 0
for dept in departments:
    if i % 2 == 0:    #I had to do this because the class name of the dept and location elements are the same.
        department_list.append(dept.text)
    i += 1

#Create list of locations
locations = driver.find_elements(By.CLASS_NAME, "job-department.pl-md-3")
locations_list = []
x = 0
for location in locations:
    if x % 2 != 0:
        locations_list.append(location.text)
    x += 1

#create list of studios
studios = driver.find_elements(By.CLASS_NAME, "job-location.pl-md-3")
studio_list = []
for studio in studios:
    studio_list.append(studio.text)

#Close the driver
driver.close()

#Testing
#Note that the formatting issues are a visual bug not a code issue. The lists are the main thing.
y = 0
for job in title_list:
    print(title_list[y])
    print(department_list[y])
    print(locations_list[y])
    print(studio_list[y])
    print("\n")
    y += 1