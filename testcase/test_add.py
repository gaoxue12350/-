#-*-coding:utf-8-*-
import unittest
from page.addUser import *
from page.parklogin import *
from selenium import webdriver
class AddTest(unittest.TestCase,AddUser,Login):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.driver.get(self.getXmldata('url'))
    def tearDown(self):
        self.driver.quit()
    def test_add(self):
        '''验证：添加用户'''
        self.login()
        self.isAddShop()
        self.clickManage()
        self.so()
        shopName = self.getShopName()
        self.delShop()
        self.assertEqual(shopName,u'123456')
    # @staticmethod
    # def suite():
    #     suite=unittest.TestSuite(unittest.makeSuite(AddTest))
    #     return suite

if __name__=='__main__':
     unittest.main()