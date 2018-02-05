#!/usr/bin/env python
#-*-coding:utf-8-*-
from base.base import *
from selenium.webdriver.common.by import  By
from utils.helper import *
class Login(WebDriver,DataHelper):
    login_loc = (By.XPATH, '//*[@id="app"]/div/section[1]/div/div[2]/button')
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    loginButton_loc=(By.XPATH,'//*[@id="app"]/div/div/div[2]/form/div[4]/button')
    txt_loc=(By.XPATH,'//*[@id="app"]/div/nav/div/div/ul[2]/li/a/div')
    def clickLogin(self):
        self.findElement(*self.login_loc).click()
    def typeUsername(self,username):
        self.findElement(*self.username_loc).send_keys(username)
    def typePassword(self,password):
        self.findElement(*self.password_loc).send_keys(password)
    def clickLoginButton(self):
        self.findElement(*self.loginButton_loc).click()
    def login(self,parent='login',username='username',password='password'):
        self.clickLogin()
        self.wait()
        self.typeUsername(self.getXmlUser(parent,username))
        self.typePassword(self.getXmlUser(parent,password))
        self.clickLoginButton()
        self.wait()
    def getNick(self):
        '''获取昵称'''
        return self.findElement(*self.txt_loc).text





