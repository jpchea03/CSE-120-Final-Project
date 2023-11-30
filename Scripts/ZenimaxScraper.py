#Authors: Joseph Cheatham, Liz Overly, Erlden Manalili
#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

#Website: https://jobs.zenimax.com/jobs

def scrape_job_information():
    #Create driver
    driver = webdriver.Chrome()

    try:
        #Connect to browser
        driver.get("https://jobs.zenimax.com/jobs")

        #Wait
        driver.implicitly_wait(2)

        #Lists are parallel
        #Create a list of all job titles
        job_titles = driver.find_elements(By.CLASS_NAME, "job-title")
        title_list = [title.text for title in job_titles[1:]]  #Ignoring the first element (for some reason it was pulling the count of jobs as a title)

        #Create list of departments
        departments = driver.find_elements(By.CLASS_NAME, "job-department.pl-md-3")
        department_list = [dept.text for i, dept in enumerate(departments) if i % 2 == 0]

        #Create list of studios
        studios = driver.find_elements(By.CLASS_NAME, "job-location.pl-md-3")
        studio_list = [studio.text for studio in studios]

        #Create list of locations
        locations = driver.find_elements(By.CLASS_NAME, "job-department.pl-md-3")
        locations_list = [location.text for i, location in enumerate(locations) if i % 2 != 0]

        return title_list, department_list, studio_list, locations_list

    finally:
        #Close the driver in any case
        driver.quit()

def write_to_csv(title_list, department_list, locations_list, studio_list, file_path):
    #Filter jobs by department (engineering/programming)
    filtered_indices = [i for i, dept in enumerate(department_list) if 'Engineering' in dept or 'Programming' in dept]

    #Apply the filter to all lists
    filtered_title_list = [title_list[i] for i in filtered_indices]
    filtered_department_list = [department_list[i] for i in filtered_indices]
    filtered_studio_list = [studio_list[i] for i in filtered_indices]
    filtered_locations_list = [locations_list[i] for i in filtered_indices]

    #Create DataFrame with filtered data
    df = pd.DataFrame(
        np.column_stack([filtered_title_list, filtered_department_list, filtered_studio_list, filtered_locations_list]),
        columns=['Title', 'Department', 'Studio', 'Locations'])
    
    #Write to CSV
    df.to_csv(file_path, index=False)

if __name__ == '__main__':
    #Creates lists using function
    job_titles, departments, studios, locations = scrape_job_information()
    #sets filepath and writes to csv with input lists from above
    file_path = r"C:\Users\jpche\CSE 120\CSE 120 Final Project\Data\JobData.csv"
    write_to_csv(job_titles, departments, studios, locations, file_path)

