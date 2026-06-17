
####### 6/17/26 Tobias N ###################
"""
1. Put this python file (surveillance_sort.py) in the auto-generated folder called "N863A6" 
(or change the 'dir' path below)

2. Rename the folder of raw videos you want to sort "to_sort"

3. Run this file; it should make a new folder called "output" that contains
folders for each date and automatically move videos into those folders.

"""

to_sort = "/to_sort" 
dir = "d:/N863A6"


#######################################

import shutil
import os


# FOR DEBUGGING
# dir =  os.path.dirname(os.path.realpath(__name__))


# Relative path of output folder
output = "/output"


# Go through all of the unsorted files 
for filename in os.listdir(dir+to_sort):
    print(dir+to_sort+"/"+filename)

    # Skip files not formatted like a surveillance video
    if not filename.startswith("N863A6_"):
        continue

    # Grab the date - by default in format YYYYMMDD
    date = filename.split("_")[3][:8]
    # Reformat date to YYYY-MM-DD
    date_reformat = date[0:4] + "-" + date[4:6] + "-" + date[6:8]
    newpath = dir+output+"/"+date_reformat
    print(newpath)

    # Create a new folder for the date if it doesn't exist
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print("Created directory: " + newpath)

    # Move the file to the new folder & print the new path of the file
    print(shutil.move(dir+to_sort+"/"+filename, newpath+"/"+filename))


# Confirm all the files have been moved out of to_sort
oldfolder = os.listdir(dir+to_sort)
if oldfolder:
  print("\nIssue - Not all files were successfully moved from to_sort:\n")
  print(oldfolder)
else:
  print("\nAll files sorted and removed from to_sort.")
      
    
