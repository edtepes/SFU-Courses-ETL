#! python3
# *************************************************************************
# 
# Chrome CourseDiggers Scraper:
# 	Uses Python - Selenium - BeautifulSoup to scrape coursediggers.com 
# 	for data on Course Names, Fail Rates, Difficulty, Workload, Median Grade
#	and turns that data into a csv file
#
# *************************************************************************

#TODO: Create output csv
#TODO: Scrape Fail Rate - 
#TODO: Scrape Median Grade - 


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re
import json

courses_csv_file = open("CD_Spring2019Data.csv", "w+")
courses_csv_file.write("Course Name, Difficulty, Workload, Dig Percentage, Median Grade, Fail Rate\n")

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  
driver.get('http://coursediggers.com/pages/explore');
# time.sleep(5) # let the tester see

bfs1 = BeautifulSoup(driver.page_source, 'html.parser') 
course_links_list = [] #stores course table's element ids 
num_of_courses = 0 #tally of how many courses are on the page


for link in bfs1.find_all(re.compile("^tr")):
	course_links_list.append(link.get('id'))
	num_of_courses += 1

del course_links_list[0] #discard first element (header row of the table)

# while True:
# 	try:
# 		course_page = driver.find_element_by_id(str(course_links_list[0]))
# 		course_page.click()
# 		driver.switch_to_window(driver.window_handles[1]) #driver looks at new tab
# 		time.sleep(10) #let page fully load
# 		bfs2 = BeautifulSoup(driver.page_source, 'html.parser')
# 		coursename = bfs2.body.contents[41].contents[1].contents[3].contents[3].contents[1]
# 		print(coursename.string) 
# 		#print course name
# 		difficulty = str(bfs2.body.contents[41].contents[3].contents[3].contents[5].contents[3].contents[3].contents[1].contents[3])
# 		print("Difficulty: " + difficulty[37:40] + "/5.0")
# 		#print difficulty
# 		workload = str(bfs2.body.contents[41].contents[3].contents[3].contents[5].contents[3].contents[3].contents[3].contents[3])
# 		print("Workload: " + workload[37:40] + "/5.0")
# 		#print workload
# 		digg_percentage = bfs2.body.contents[41].contents[3].contents[3].contents[5].contents[3].contents[3].contents[5].contents[1].contents[1]
# 		print("Dig Percentage: " + digg_percentage.string)
# 		#print dig percentage
# 		driver.close() #driver closes currently focused tab and decrements window_handles[]
# 		driver.switch_to_window(driver.window_handles[0]) #driver looks at main list tab
# 		driver.get('http://www.coursediggers.com/data/' + str(course_links_list[0])[18:] + '.json')
# 		json_text = str(driver.find_element_by_css_selector('html').get_attribute('innerText'))
# 		parsed_json = json.loads(json_text)
# 		median_grade = parsed_json['data'][0][0]
# 		print("Median Grade: " + parsed_json['data'][0][0])
# 		#print median grade
# 		fail_rate = round(float(parsed_json['data'][0][1]),1)
# 		print("Fail Rate: " + str(fail_rate) + "%")
# 		#print fail rate
# 		time.sleep(3)
# 		driver.execute_script("window.history.go(-1)")	
# 		time.sleep(3)	
# 		break
# 	except (IndexError, AttributeError):
# 		driver.close() #driver closes currently focused tab and decrements window_handles[]
# 		driver.switch_to_window(driver.window_handles[0]) #driver looks at new tab
# 		continue


for i in range(len(course_links_list)):
	while True:
		try:
			course_page = driver.find_element_by_id(str(course_links_list[i]))
			
			# course_page = driver.find_element_by_id("explore-table-row-148")
			# course_page.location_once_scrolled_into_view
			# driver.execute_script("window.scrollTo(0,{})".format(course_page.location_once_scrolled_into_view['y']+80))
			# # print(driver.get_window_position())


			course_page.click()
			driver.switch_to_window(driver.window_handles[1]) #driver looks at new tab
			time.sleep(5) #let page fully load
			bfs2 = BeautifulSoup(driver.page_source, 'html.parser')
			
			#gather the stats 
			coursename = bfs2.body.contents[41].contents[1].contents[3].contents[3].contents[1]
			difficulty = str(bfs2.body.contents[41].contents[3].contents[3].contents[5].contents[3].contents[3].contents[1].contents[3])
			workload = str(bfs2.body.contents[41].contents[3].contents[3].contents[5].contents[3].contents[3].contents[3].contents[3])
			digg_percentage = bfs2.body.contents[41].contents[3].contents[3].contents[5].contents[3].contents[3].contents[5].contents[1].contents[1]
			
			print(coursename.string) 
			print("Difficulty: " + difficulty[37:40] + "/5.0")
			print("Workload: " + workload[37:40] + "/5.0")
			print("Dig Percentage: " + digg_percentage.string)
			#parse json for the current course
			driver.get('http://www.coursediggers.com/data/' + str(course_links_list[i])[18:] + '.json')
			json_text = str(driver.find_element_by_css_selector('html').get_attribute('innerText'))
			parsed_json = json.loads(json_text)
			median_grade = parsed_json['data'][0][0]
			print("Median Grade: " + parsed_json['data'][0][0])
			fail_rate = round(float(parsed_json['data'][0][1]),1)
			print("Fail Rate: " + str(fail_rate) + "%")
			courses_csv_file.write(coursename.string+", "+difficulty[37:40]+", "+workload[37:40]+", "+digg_percentage.string+", "+median_grade+", "+str(fail_rate)+"%"+"\n")
			driver.close() #driver closes currently focused tab and decrements window_handles[]
			driver.switch_to_window(driver.window_handles[0]) #driver looks at main list tab
			
			driver.execute_script("window.scrollTo(0,{}*80)".format(i))
			time.sleep(5)	
			break
		except (IndexError, AttributeError):
			driver.close() #driver closes currently focused tab and decrements window_handles[]
			driver.switch_to_window(driver.window_handles[0]) #driver looks at new tab
			time.sleep(5)	
			continue
		except():
			print("OTHER ERROR")
			driver.execute_script("window.scrollTo(0,{}*80)".format(i))
			time.sleep(5)				
courses_csv_file.close()
driver.quit()

