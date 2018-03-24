from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest
import time
import random

class Registration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://demoqa.com/registration/')
        
    def test_fillingIn(self):
        browser = self.browser
        random_number = str(random.randint(0, 9999))
        
        first_name = browser.find_element_by_xpath('//*[@id="name_3_firstname"]')
        first_name.send_keys('Firstname')
        
        last_name = browser.find_element_by_xpath('//*[@id="name_3_lastname"]')
        last_name.send_keys('Lastname')
        
        browser.find_element_by_xpath('//*[@id="pie_register"]/li[3]/div/div[1]/input[1]').click()

        select_country = Select(browser.find_element_by_xpath('//*[@id="dropdown_7"]'))#drop-down menu
        select_country.select_by_visible_text('Moldova')

        select_month = Select(browser.find_element_by_xpath('//*[@id="mm_date_8"]'))#month
        select_month.select_by_value('5')

        select_month = Select(browser.find_element_by_xpath('//*[@id="dd_date_8"]'))#day
        select_month.select_by_value('24')

        select_month = Select(browser.find_element_by_xpath('//*[@id="yy_date_8"]'))#year
        select_month.select_by_value('1992')

        phone_number = browser.find_element_by_xpath('//*[@id="phone_9"]')#phone number
        phone_number.send_keys('1234567890')

        user_name = browser.find_element_by_xpath('//*[@id="username"]')#user name
        user_name.send_keys('SuperTester'+random_number)

        e_mail = browser.find_element_by_xpath('//*[@id="email_1"]')#email
        e_mail.send_keys('SuperTester'+random_number+'@test.test')

        password = browser.find_element_by_xpath('//*[@id="password_2"]')#password
        password.send_keys('123456789')

        password_confirm = browser.find_element_by_xpath('//*[@id="confirm_password_password_2"]')#confirm password
        password_confirm.send_keys('123456789')

        browser.find_element_by_xpath('//*[@id="pie_register"]/li[14]/div/input').click() #submit button

        time.sleep(5)

        successful_registration = browser.find_element_by_xpath('//*[@id="post-49"]/div/p')
        #assert 'Thank you for your registration' in successful_registration.text СПОСОБ 1
        self.assertIn('Thank you for your registration', successful_registration.text)#CПОСОБ 2
        
    """
    def test_errorMessage(self): #negative
        browser = self.browser
        first_name = browser.find_element_by_xpath('//*[@id="name_3_firstname"]')
        first_name.send_keys('Maxim')

        browser.find_element_by_xpath('//*[@id="pie_register"]/li[14]/div/input').click()

        firstname_secondname_error = browser.find_element_by_xpath('//*[@id="pie_register"]/li[1]/div[1]/div[2]/span')

        assert '* This field is required' in firstname_secondname_error.text

        time.sleep(2)       
    """               

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
        
