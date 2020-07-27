from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Start up webdriver for Chrome
browser = webdriver.Chrome(r'C:\Users\mcpik\Desktop\Visual Studio Practice\Py Projects\JobSearch\chromedriver')

#Open Indeed.com in the browser and assert the keyword "Indeed"
browser.get('http://www.indeed.com')
assert 'Indeed' in browser.title

#Find the Job Title HTML element and enter desired job title
elem = browser.find_element_by_name('q')
elem.send_keys('chemical engineer' + Keys.ENTER)