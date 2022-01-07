# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 19:32
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : baiduIndex.py
from Common.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class BaiduIndex(BasePage):
    """
    页面元素
    """
    # 百度首页链接
    baidu_index_url = "https://www.baidu.com/"
    # 搜索框
    search_input = (By.ID, "kw")
    # "百度一下"按钮框
    search_button = (By.ID, "su")
    #帐号
    zhanghao=((By.XPATH,"//*[@id='app']/div/div[1]/div[2]/form/div[2]/div/div/input"))
    #密码
    mi=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/form/div[3]/div/div/input")
    #点击登录
    deng=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/form/button")
    #点击集团品项管理
    A1=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/div")
    #点击品项管理
    A2=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[11]/li/ul/div[1]")
    # 查询操作
    def search_key(self, search_key):
        self.logger.info("【===搜索操作===】")
        # 等待用户名文本框元素出现
        self.wait_eleVisible(self.search_input, model='搜索框')
        # 输入内容
        self.input_text(self.search_input, "阿崔", model="搜索框")
        # 清除文本框内容
        self.clean_inputText(self.search_input, model='搜索框')
        # 输入用户名
        self.input_text(self.search_input, text=search_key, model='搜索框')
        # 等待搜索按钮出现
        self.wait_eleVisible(self.search_button, model='"百度一下"搜索按钮')
        # 点击搜索按钮
        self.click_element(self.search_button, model='"百度一下"搜索按钮')
        # 搜索后等待界面加载完成
        self.driver.implicitly_wait(10)
        sleep(3)
    #登录
    def OMS_deng(self,search_key,a):
        #输入帐号
        self.input_text(self.zhanghao,text=search_key,model="输入账号")
        #输入密码
        self.input_text(self.mi,text=a,model="输入密码")
        #点击登录
        self.click_element(self.deng,model="点击登录")
        self.driver.implicitly_wait(10)
        sleep(3)
    #点击品项管理
    def OMS_p(self):
        self.OMS_deng("pengjie","Qq123456")
        #点击品项管理
        self.click_element(self.A1,model="供应链管理")
        #点击品项管理
        self.click_element(self.A2,model="品项管理")
        self.driver.implicitly_wait(10)
        sleep(3)
