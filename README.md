# SFUCourse-ETL-Pipeline

Language: Python3
Libaries: Chromedriver, Selenium, BeautifulSoup4, 

 The purpose of this open source, self-directed project is to gain better understanding of SFU course data through the following process:
 1. EXTRACT SFU course data from Course Diggers using the Selenium library, 
 2. TRANSFORM the data using the Pandas library, and eventually 
 3. LOAD the data into a database for tracking changes over time.

 Current Status: Limited Functionality 

# TO-DO: 
 - Run some basic statistics on the resulting csv file after extraction
 - Load data into a database and make the process seamless

# BUGS:
 - need to fix a bug were an ad on the page pops up and interrupts mouse clicks 
   (maybe scroll the page a set amount automatically after each time returning to the master course list)
