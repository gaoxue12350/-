#-*-coding:utf-8-*-
from base.base import *
from selenium.webdriver.common.by import By
from utils.helper import *
class AddUser(WebDriver,DataHelper):
    '''添加商户'''
    addBusiness_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/a')
    accountName = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[1]/div/input')
    businName = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[2]/div/input')
    businPassword = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[3]/div/input')
    save_loc = (By.XPATH, ".//*[@id='app']/div/div[1]/div/div[2]/div/div/div[9]/div/button")

    def clickAdd(self):
        self.wait()
        self.findElement(*self.addBusiness_loc).click()

    def typeAaccount(self, accountName):
        self.wait()
        self.findElement(*self.accountName).send_keys(accountName)

    def typeName(self, businName):
        self.wait()
        self.findElement(*self.businName).send_keys(businName)

    def typePasswd(self, businPassword):
        self.wait()
        self.findElement(*self.businPassword).send_keys(businPassword)

    def clickSave(self):
        self.wait()
        self.findElement(*self.save_loc).click()

    def addShop(self, accountName='123456', businName='123456', businPassword='123456'):
        self.clickAdd()
        self.typeAaccount(accountName)
        self.typeName(businName)
        self.typePasswd(businPassword)
        self.clickSave()

    '''查询商户'''
    so_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/div[2]/input')
    soButton_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/div[3]/button')
    shopName_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[1]/div/a')

    def typeSo(self, name):
        self.wait()
        self.findElement(*self.so_loc).send_keys(name)

    def clickSo(self):
        self.findElement(*self.soButton_loc).click()

    def getShopName(self):
        self.wait()
        return self.findElement(*self.shopName_loc).text

    def so(self, name='123456'):
        self.typeSo(name)
        self.clickSo()

    u'删除商户'
    sel_loc = (By.XPATH, ".//*[@id='app']/div/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/div/i")
    del_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[5]/div/ul/li[2]')
    delOk_loc = (By.XPATH, '/html/body/div[5]/div[2]/div/div/div/div/div[2]/button[1]')

    def delClickSel(self):
        self.wait()
        self.findElement(*self.sel_loc).click()

    def delClickDel(self):
        self.wait()
        self.findElement(*self.del_loc).click()

    def delClickOK(self):
        self.wait()
        self.findElement(*self.delOk_loc).click()

    def delShop(self):
        self.delClickSel()
        self.delClickDel()
        self.delClickOK()

    u'商户管理'
    manage_loc = (By.XPATH, '//*[@id="app"]/div/nav/div/div/ul[1]/li[1]/a')

    def clickManage(self):
        self.wait()
        self.findElement(*self.manage_loc).click()

    def isAddShop(self):
        try:
            self.so()
            assert self.getShopName() in u'123456'
            self.delShop()
        except:
            self.addShop()
        else:
            self.addShop()
        finally:
            pass