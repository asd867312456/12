import sys 
sys.path.append("..")
import os
import time
import pytest
import allure
from time import sleep
from selenium import webdriver
from PageObject.baiduIndex import BaiduIndex
from Common.basePage import BasePage
from selenium.webdriver.common.by import By
@allure.feature("登录模块")
class Test_1:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://iadmin.staging.jmj1995.com/login")
        self.driver.implicitly_wait(10)
        self.basepage=BasePage(self.driver)
        self.bai=BaiduIndex(self.driver)
    @allure.story("登录")
    @pytest.mark.test_001
    @pytest.mark.parametrize(
    "usr,password",[("pengjie","Qq123456"),("pengjie32","Qq123456"),("pengjie","qq123")],)
    def test_001(self,usr,password):
        #登录
        self.bai.OMS_deng(usr,password)
        if usr=="pengjie" and password=="Qq123456":
            self.basepage.wait_eleVisible((By.XPATH,"//*[@id='app']/div/div[2]/div/div[1]/div[3]/div[2]/span/span/button/span"))
        elif usr=="pengjie32" and password=="Qq123456":
            self.basepage.wait_eleNoVisible((By.XPATH,"//*[@id='app']/div/div[2]/div/div[1]/div[3]/div[2]/span/span/button/span"))
        else:
            self.basepage.wait_eleNoVisible((By.XPATH,"//*[@id='app']/div/div[2]/div/div[1]/div[3]/div[2]/span/span/button/span"))
        self.driver.implicitly_wait(10)
    @pytest.mark.parametrize()
    @allure.story("品项管理查看/编辑")
    @pytest.mark.test_002
    # @pytest.skip()
    def test_002(self):
        #品项管理查看/编辑 操作
        self.bai.OMS_p()


    def teardown(self):
        time.sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(cur_path, f'Report\\{now_time}')

    # -s : 打印信息
    # -m ：运行含标签的用例
    pytest.main(["--alluredir", report_path])
    # 解析测试报告，执行: allure serve {report_path}
    os.system(f"allure serve {report_path}")
