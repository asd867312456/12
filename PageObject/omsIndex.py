
from Common.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
class OmsIndex(BasePage):
    """
    页面元素
    """
    #帐号
    zhanghao=((By.XPATH,"//*[@id='app']/div/div[1]/div[2]/form/div[2]/div/div/input"))
    #密码
    mi=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/form/div[3]/div/div/input")
    #点击登录
    deng=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/form/button")
    #点击供应链管理
    #//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span
    A1=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div")
    #点击品项管理
    A2=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li")
    #点击门店管理
    A4=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[2]/a/li")
    #点击供应商管理
    A5=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[3]/a/li")
    #点击员工餐管理
    A6=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[6]/li/div")
    #盘点模板管理
    A7=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[9]/a/li")
    #展开模块
    b3=(By.CLASS_NAME,"hamburger-container")
    #登录
    def OMS_deng(self,search_key,a):
        #输入帐号
        self.input_text(self.zhanghao,text=search_key,model="输入账号")
        #输入密码
        self.input_text(self.mi,text=a,model="输入密码")
        #点击登录
        self.click_element(self.deng,model="点击登录")
        self.driver.implicitly_wait(10)
        sleep(2)
    #点击品项管理
    def OMS_p(self,a):
        self.OMS_deng("oms1212","Qq123456")
        #点击品项管理
        # try:
        #     self.click_element(self.A1,model="供应链管理")
        # except:
        # self.click_element(self.b3,model="展开模块")
        # self.driver.implicitly_wait(10)
        sleep(1)
        self.click_element(self.A1,model="供应链管理")
        if a=="A2":
            #点击品项管理
            self.click_element(self.A2,model="品项管理")
            self.driver.implicitly_wait(10)
            sleep(2)
        elif a=="A4":
             #点击门店管理
            self.click_element(self.A4,model="门店管理")
            self.driver.implicitly_wait(10)
            sleep(2)
        elif a=="A5":
            #点击供应商管理
            self.click_element(self.A5,model="供应商管理")
            self.driver.implicitly_wait(10)
        elif a=="A6":
            #员工餐管理
            self.click_element(self.A6,model="员工餐管理")
            self.driver.implicitly_wait(10)
        elif a=="A7":
            #盘点模板管理
            self.click_element(self.A7,model="盘点模板管理")
            self.driver.implicitly_wait(10)
            sleep(2)
