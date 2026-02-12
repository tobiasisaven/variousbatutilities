
####### 2/12/26 TIN ###################
"""
1. Write the name of the folder within the external hard drive that contains unsorted video files here:
""" 

to_sort = "/2026-2-2" 


"""
2. Put this python file (surveillance_sort.py) one level above that folder, 
probably in the auto-generated folder called "N863A6" 

3. Run this file; it should make a new folder called "output" that contains
folders for each date and automatically move videos into those folders.

"""
#######################################

import shutil
import os

# Relative path of output folder
output = "/output"

# Go through all of the unsorted files 
for filename in os.listdir(os.getcwd()+to_sort):
    # Skip files not formatted like a surveillance video
    if not filename.startswith("N863A6_"):
        continue

    # Grab the date - by default in format YYYYMMDD
    date = filename.split("_")[3][:8]
    # Reformat date to YYYY-MM-DD
    date_reformat = date[0:4] + "-" + date[4:6] + "-" + date[6:8]
    newpath = os.getcwd()+output+"/"+date_reformat

    # Create a new folder for the date if it doesn't exist
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    # Move the file to the new folder & print the new path of the file
    print(shutil.move(os.getcwd()+to_sort+"/"+filename, newpath+"/"+filename))

