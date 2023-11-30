import numpy as np
df = pd.DataFrame(np.column_stack([title_list, department_list, locations_list, studio_list]),
                  columns=['Title', 'Department', 'Locations', 'Studio'])

df.to_csv("C:/Users/eover/OneDrive/Fall 2023/CSE 120-01/Final Project/zeni_jobs.csv", index = False)
