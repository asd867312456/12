from inspect import modulesbyfile
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
# import pytest_rerunfailures
#随机生成九位数
number=str(99)+"".join(random.sample(["0","1","2","3","4","5","6","7","8","9"],9))
@allure.feature("OMS品牌视角")
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
    @pytest.mark.parametrize(
    "usr,password",[("pengjie","Qq123456"),("pengjie32","Qq123456"),("pengjie","qq123")],)
    @pytest.mark.flaky(reruns=1,reruns_delay=10) 
    # @pytest.mark.skip(reason="调式")
    def test_001(self,usr,password):
        #登录
        self.oms.OMS_deng(usr,password)
        if usr=="pengjie" and password=="Qq123456":
            self.basepage.wait_eleVisible((By.XPATH,"//*[@id='app']/div/div[2]/div/div[1]/div[3]/div[2]/span/span/button/span"),model="断言")
        elif usr=="pengjie32" and password=="Qq123456":
            self.basepage.wait_eleNoVisible((By.XPATH,"//*[@id='app']/div/div[2]/div/div[1]/div[3]/div[2]/span/span/button/span"),model="断言")
        else:
            self.basepage.wait_eleNoVisible((By.XPATH,"//*[@id='app']/div/div[2]/div/div[1]/div[3]/div[2]/span/span/button/span"),model="断言")
        self.driver.implicitly_wait(10)
    @pytest.mark.parametrize("a",["1","2"])
    #当A=1时为查看，当A等于2时为编辑
    @allure.story("品项管理查看/编辑（当A=1时为查看，当A等于2时为编辑）")
    @pytest.mark.test_002
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_002(self,a):
        #品项管理查看/编辑 操作
        self.oms.OMS_p("A2")
        self.driver.implicitly_wait(10)
        if a=="1":
            time.sleep(2)
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/section/main/section/main/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[3]/div/button[1]/span"),model="点击查看")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.wait_eleVisible((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/div/div/div[3]/div/button/span"),model="断言")
        else:
            #点击编辑
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/section/main/section/main/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[3]/div/button[2]/span"),model="点击编辑")
            self.driver.implicitly_wait(10)
            #输入标签
            self.basepage.input_text((By.XPATH,"//*[@id='pane-basic']/div/form[1]/div[9]/div/div[1]/div/input"),number)
            self.driver.implicitly_wait(10)
            #点击添加
            self.basepage.click_element((By.XPATH,"//*[@id='pane-basic']/div/form[1]/div[9]/div/div[2]/button/span"),model="点击添加")
            self.driver.implicitly_wait(10)
            #点击保存
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/div/div/div[3]/div/button[2]/span"),model="点击确定")
            self.driver.implicitly_wait(10)
            #断言
            self.basepage.wait_text((By.XPATH,"/html/body/div[2]/p"),"提交成功",model="断言")
    @allure.story("门店管理-编辑门店")
    @pytest.mark.test_003
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_003(self):
        #门店管理/编辑 操作
        self.oms.OMS_p("A4")
        self.driver.implicitly_wait(10)
        self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/button"),model="点击编辑")
        self.driver.implicitly_wait(10)
        self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/div/div/form/div[3]/div/div/div/button[2]"),model="点击修改")
        self.driver.implicitly_wait(10)
        self.basepage.wait_eleVisible((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/button"),model="断言")
        self.driver.implicitly_wait(10)
    @pytest.mark.parametrize("a",["1","2"])
    #当A=1时为查看，当A等于2时为编辑
    @allure.story("供应商查看/编辑（当A=1时为查看，当A等于2时为编辑）")
    @pytest.mark.test_004
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_004(self,a):
        #供应商管理查看/编辑 操作
        self.oms.OMS_p("A5")
        self.driver.implicitly_wait(10)
        if a=="1":
            time.sleep(2)
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/section/main/section/main/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/button[1]"),model="点击查看")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.wait_eleVisible((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/div/div/div[3]/div/button"),model="断言")
        else:
            time.sleep(2)
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/section/main/section/main/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/button[2]"),model="点击查看")
            self.driver.implicitly_wait(10)
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/div/div/div/div[3]/div/button[2]"),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text((By.XPATH,"/html/body/div[2]/p"),"更新供应商详情成功",model="更新供应商详情成功断言")
            time.sleep(2)
    @pytest.mark.parametrize("a",["1","2","3","4"])
    #当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为删除。
    @allure.story("员工餐新增/查看/编辑/删除，当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为删除。")
    @pytest.mark.test_005
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_005(self,a):
        #员工餐新增/查看/编辑/删除
        self.oms.OMS_p("A6")
        self.driver.implicitly_wait(10)
        #//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[6]/li/ul/div[1]/a/li/span
        self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[6]/li/ul/div[1]/a/li"),model="点击员工餐模板")
        self.driver.implicitly_wait(10)
        if a=="1":
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/header/div[2]/button"),model="点击新增员工餐模板")
            self.driver.implicitly_wait(10)
            self.basepage.input_text((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/div/div/div[2]/div[3]/div[1]/div[2]/div/form/div[1]/div/div/input"),number,model="模板名称")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/div/div/div[3]/div/button[2]"),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text((By.XPATH,"/html/body/div[2]/p"),"新增员工餐模版成功",model="新增员工餐模板断言")
        elif a=="2":
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/main/section/main/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/button[1]/span"),model="查看第一个模板")
            self.driver.implicitly_wait(10)
            self.basepage.wait_eleVisible((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/div/div/div[3]/div/button"),model="查看员工餐模板断言")
        elif a=="3":
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/main/section/main/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/button[2]/span"),model="点击编辑员工餐模板")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/div/div/div[3]/div/button[2]"),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text((By.XPATH,"/html/body/div[2]/p"),"修改员工餐模版成功",model="修改员工餐模板断言")
        else:
            self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/main/section/main/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span/span/button/span"),model="点击删除员工餐模板")
            self.driver.implicitly_wait(10)
            # //*[@id="el-popover-6488"]
            self.basepage.click_element((By.XPATH,"/html/body/div[2]/div[1]/div/button[2]/span"),model="二次确定删除")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text((By.XPATH,"/html/body/div[3]/p"),"删除模板成功",model="删除断言")

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
