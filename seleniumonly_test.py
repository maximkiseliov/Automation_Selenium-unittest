from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://google.com')

assert 'Google' in browser.title

elem = browser.find_element_by_name('q')
elem.send_keys('cats' + Keys.RETURN)

assert 'Google' in browser.title

browser.quit()
