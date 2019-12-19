from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('localhost:5000')
e1 = driver.find_element_by_name('web')
e2 = driver.find_element_by_name('url')
e3=driver.find_element_by_name('submit')

e1.send_keys("bilibili")
e2.send_keys("javascript:alert('notsafe');")
e3.send_keys("",Keys.ARROW_DOWN)
