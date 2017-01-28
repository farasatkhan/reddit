import unittest
from directory import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class OpenReddit(unittest.TestCase):

    username = ''
    password = ''

    url = ''
    title = ''
    subreddit_set = file_to_set('path/subreddit.txt')

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver

        driver.get('http://www.reddit.com/login')

        driver.implicitly_wait(30)

        inputUser = driver.find_element_by_xpath('//*[@id="user_login"]')
        inputPass = driver.find_element_by_xpath('//*[@id="passwd_login"]')

        inputUser.clear()
        inputPass.clear()

        driver.implicitly_wait(30)

        inputUser.send_keys(OpenReddit.username)
        inputPass.send_keys(OpenReddit.password)

        driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()

        driver.implicitly_wait(30)
        # submit click
        driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/a').click()

        i = 0
        if i <= len(OpenReddit.subreddit_set):
            if len(OpenReddit.subreddit_set) > 0:
                while i <= len(OpenReddit.subreddit_set):
                    driver.implicitly_wait(30)
                    url = driver.find_element_by_xpath('//input[@id="url" and @class="input"]')
                    title = driver.find_element_by_xpath('//*[@id="title-field"]/div/textarea')
                    subreddit = driver.find_element_by_xpath('//input[@id="sr-autocomplete" and @name="sr"]')

                    url.clear()
                    title.clear()
                    subreddit.clear()

                    url.send_keys(OpenReddit.url)
                    title.send_keys(OpenReddit.title)
                    subreddit.send_keys(OpenReddit.subreddit_set[i])
                    driver.implicitly_wait(20)

                    driver.find_element_by_xpath('//*[@id="newlink"]/div[4]/button').click()
                    time.sleep(2)
                    try:
                        driver.switch_to.alert.accept()
                    except Exception as e:
                        pass


                    try:
                        error = driver.find_element_by_xpath('//*[@id="newlink"]/div[4]/span[2]')
                        val = [int(s) for s in error.split() if s.isdigit()]

                        if(error):
                            time.sleep(val*60 +10)
                            driver.find_element_by_xpath('//*[@id="newlink"]/div[4]/button').click()
                            try:
                                driver.switch_to.alert.accept()
                            except Exception as e:
                                pass

                    except Exception as e:
                        pass

                    driver.implicitly_wait(10)
                    driver.get('http://www.reddit.com/submit')
                    i += 1
                    time.sleep(10*60)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()