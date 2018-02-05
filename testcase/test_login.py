#!/usr/bin/env python
#-*-coding:utf-8-*-
import unittest
from page.parklogin import *
from selenium import webdriver
class LoginTest(unittest.TestCase,Login):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.driver.get(self.getXmldata('url'))

    def tearDown(self):
        self.driver.quit()

    def test_login01(self, parent='login', nikename='nick'):
        '''验证:登录成功'''
        self.login()
        self.assertEquals(self.getNick(), self.getXmlUser(parent, nikename))
if __name__=='__main__':
     unittest.main()
