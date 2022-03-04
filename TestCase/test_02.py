import sys
sys.path.append("..")
import os
import time
import pytest
import allure
from time import sleep
from selenium import webdriver
from PageObject.omsIndex import OmsIndex
from Common.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
from Common.excel_base import Doexcel
# import pytest_rerunfailures
#随机生成九位数
number=str(99)+"".join(random.sample(["0","1","2","3","4","5","6","7","8","9"],9))
sys.path.append(".")
data_list=Doexcel().excel_data_list("Config/oms_ur.xls","Sheet1")
@allure.feature("OMS配送中心视角")
class Test_1:
    def setup(self):  
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1080') #指定浏览器分辨率
        self.driver=webdriver.Chrome(chrome_options=chrome_options)
        # self.driver=webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://iadmin.staging.jmj1995.com/login")
        self.driver.implicitly_wait(10)
        self.basepage=BasePage(self.driver)
        self.oms=OmsIndex(self.driver)
    @allure.story("登录")
    @pytest.mark.test_001
    @pytest.mark.parametrize("a",["1","2"])
    @pytest.mark.flaky(reruns=1,reruns_delay=10) 
    # @pytest.mark.skip(reason="调式")
    def test_001(self):
        self.oms.OMS_s("B1")
        self.driver.implicitly_wait(10)
        self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/li/ul/div[1]/a/li"),model="点击门店品项")
        self.driver.implicitly_wait(10)
        


