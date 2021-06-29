# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# open Chrome
browser = webdriver.Safari()

# Open URL
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSf8YpYARoy9Y9YFk_osxN415K-BAELiz3dOAtXjrnv6eX-u3A/viewform?usp=sf_link')

# wait for one second, until page gets fully loaded
time.sleep(1)

# Data
datas = [
	['Mihir', 'Deshpande', '10th'],
	['Apoorv', 'Kakade', '10th'],
	['Mayuresh', 'Pingale', '10th']
]

# Iterate through each data
for data in datas:
	
	# Initialize count is zero
	count = 0

	# contain input boxes
	textboxes = browser.find_elements_by_class_name(
		"quantumWizTextinputPaperinputInput")

	# contain textareas
	textareaboxes = browser.find_elements_by_class_name(
		"quantumWizTextinputPapertextareaInput")

	# Iterate through all input boxes
	for value in textboxes:
		# enter value
		value.send_keys(data[count])
		# increment count value
		count += 1

	# Iterate through all textareas
	for value in textareaboxes:
		# enter vlaue
		value.send_keys(data[count])
		# increment count value
		count += 1

	# click on submit button
	submit = browser.find_element_by_xpath(
		'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
	submit.click()
	
	time.sleep(5)
	#fill another response
	another_response = browser.find_element_by_xpath(
		'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')

	another_response.click()

# close the window
browser.close()
