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
        final_data=Doexcel().get_test_data(data_list, "test_001")
        self.oms.OMS_deng(usr,password)
        if usr=="pengjie" and password=="Qq123456":
            self.basepage.wait_eleVisible(eval(final_data[0]["element1"]),model="断言")
            print(final_data[0]["element1"])
        elif usr=="pengjie32" and password=="Qq123456":
            self.basepage.wait_eleNoVisible(eval(final_data[0]["element2"]),model="断言")
        else:
            self.basepage.wait_eleNoVisible(eval(final_data[0]["element3"]),model="断言")
        self.driver.implicitly_wait(10)
    @pytest.mark.parametrize("a",["1","2"])
    #当A=1时为查看，当A等于2时为编辑
    @allure.story("品项管理查看/编辑（当A=1时为查看，当A等于2时为编辑）")
    @pytest.mark.test_002
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_002(self,a):
        #品项管理查看/编辑 操作
        final_data=Doexcel().get_test_data(data_list, "test_002")
        self.oms.OMS_p("A2")
        self.driver.implicitly_wait(10)
        if a=="1":
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element1"]),model="点击查看")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.wait_eleVisible(eval(final_data[0]["element2"]),model="断言")
        else:
            #点击编辑
            self.basepage.click_element(eval(final_data[0]["element3"]),model="点击编辑")
            self.driver.implicitly_wait(10)
            #输入标签
            self.basepage.input_text(eval(final_data[0]["element4"]),number)
            self.driver.implicitly_wait(10)
            #点击添加
            self.basepage.click_element(eval(final_data[0]["element5"]),model="点击添加")
            self.driver.implicitly_wait(10)
            #点击保存
            self.basepage.click_element(eval(final_data[0]["element6"]),model="点击确定")
            self.driver.implicitly_wait(10)
            #断言
            self.basepage.wait_text(eval(final_data[0]["element7"]),"提交成功",model="断言")
    @allure.story("门店管理-编辑门店")
    @pytest.mark.test_003
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_003(self):
        #门店管理/编辑 操作
        final_data=Doexcel().get_test_data(data_list, "test_003")
        self.oms.OMS_p("A4")
        self.driver.implicitly_wait(10)
        self.basepage.click_element(eval(final_data[0]["element1"]),model="点击编辑")
        self.driver.implicitly_wait(10)
        self.basepage.click_element(eval(final_data[0]["element2"]),model="点击修改")
        self.driver.implicitly_wait(10)
        self.basepage.wait_eleVisible(eval(final_data[0]["element3"]),model="断言")
        self.driver.implicitly_wait(10)
    @pytest.mark.parametrize("a",["1","2"])
    #当A=1时为查看，当A等于2时为编辑
    @allure.story("供应商查看/编辑（当A=1时为查看，当A等于2时为编辑）")
    @pytest.mark.test_004
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_004(self,a):
        #供应商管理查看/编辑 操作
        final_data=Doexcel().get_test_data(data_list, "test_004")
        self.oms.OMS_p("A5")
        self.driver.implicitly_wait(10)
        if a=="1":
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element1"]),model="点击查看")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.wait_eleVisible(eval(final_data[0]["element2"]),model="断言")
        else:
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element3"]),model="点击编辑")
            self.driver.implicitly_wait(10)
            self.basepage.click_element(eval(final_data[0]["element4"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element5"]),eval(final_data[0]["element6"]),model="更新供应商详情成功断言")
            time.sleep(2)
    @pytest.mark.parametrize("a",["1","2","3","4"])
    #当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为删除。
    @allure.story("员工餐新增/查看/编辑/删除，当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为删除。")
    @pytest.mark.test_005
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_005(self,a):
        #员工餐新增/查看/编辑/删除
        final_data=Doexcel().get_test_data(data_list, "test_005")
        self.oms.OMS_p("A6")
        self.driver.implicitly_wait(10)
        time.sleep(2)
        #//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[6]/li/ul/div[1]/a/li/span
        self.basepage.click_element(eval(final_data[0]["element1"]),model="点击员工餐模板")
        self.driver.implicitly_wait(10)
        if a=="1":
            self.basepage.click_element(eval(final_data[0]["element2"]),model="点击新增员工餐模板")
            self.driver.implicitly_wait(10)
            self.basepage.input_text(eval(final_data[0]["element3"]),number,model="输入模板名称")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element4"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element5"]),eval(final_data[0]["element6"]),model="新增员工餐模板断言")
        elif a=="2":
            time.sleep(1)
            element=self.driver.find_elements_by_class_name(eval(final_data[0]["element17"]))
            self.driver.implicitly_wait(10)
            element[0].find_element_by_xpath(eval(final_data[0]["element18"])).click()
            # self.basepage.click_element(eval(final_data[0]["element7"]),model="查看第一个模板")
            self.driver.implicitly_wait(10)
            self.basepage.wait_eleVisible(eval(final_data[0]["element8"]),model="查看员工餐模板断言")
        elif a=="3":
            time.sleep(1)
            element=self.driver.find_elements_by_class_name(eval(final_data[0]["element17"]))
            self.driver.implicitly_wait(10)
            element[0].find_element_by_xpath(eval(final_data[0]["element19"])).click()
            # self.basepage.click_element(eval(final_data[0]["element9"]),model="点击编辑员工餐模板")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element10"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element11"]),eval(final_data[0]["element12"]),model="修改员工餐模板断言")
        else:
            time.sleep(1)
            self.basepage.click_element(eval(final_data[0]["element13"]),model="点击删除员工餐模板")
            self.driver.implicitly_wait(10)
            # //*[@id="el-popover-6488"]
            self.basepage.click_element(eval(final_data[0]["element14"]),model="二次确定删除")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element15"]),eval(final_data[0]["element16"]),model="删除断言")
    @pytest.mark.parametrize("a",["1","2","3","4","5","6"])
    #当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为停用，当A=5时为启用，当A等于6时为删除，。
    @allure.story("盘点模板新增/查看/编辑/删除当A=1时为新增 当A等于2时为查看 当A等于3时为编辑 当A等于4时为停用 当A=5时为启用 当A等于6时为删除。")
    @pytest.mark.test_006
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_006(self,a):
        #盘点新增/查看/编辑/删除/停用/启用
        final_data=Doexcel().get_test_data(data_list, "test_006")
        self.oms.OMS_p("A7")
        self.driver.implicitly_wait(10)
        if a == "1":
            #(By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/header/div[2]/button")
            self.basepage.click_element(eval(final_data[0]["element1"]),model="点击新增盘点模板模板")
            self.driver.implicitly_wait(10)
            #(By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/div/div/div[2]/form/div[2]/div/div/input")
            self.basepage.input_text(eval(final_data[0]["element2"]),number,model="输入模板名称")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element3"]),model="选择品项")
            self.driver.implicitly_wait(10)
            time.sleep(3)
            ELE=self.driver.find_elements_by_class_name(eval(final_data[0]["element4"]))
            #/html/body/div[2]/div/div[2]/section/section/main/div/div
            #/html/body/div[2]/div/div[2]/section/section/main/div/div/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span
            #先定位唯一class——name,再根据下标去确定唯一XPATH
            ELE[1].find_element_by_xpath(eval(final_data[0]["element5"])).click()
            self.driver.implicitly_wait(10)
            ELE1=self.driver.find_elements_by_class_name(eval(final_data[0]["element6"]))
            #先定位唯一class——name,再根据下标去确定唯一XPATH
            #点击确定
            ELE1[1].find_element_by_xpath(eval(final_data[0]["element7"])).click()
            self.driver.implicitly_wait(10)
            # (By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/div/div/div[3]/div/button[2]/span")
            self.basepage.click_element(eval(final_data[0]["element8"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element9"]),eval(final_data[0]["element10"]),model="新增盘点餐模板断言")
        elif a=="2":
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element11"]),model="查看第二个模板")
            self.driver.implicitly_wait(10)
            self.basepage.wait_eleVisible(eval(final_data[0]["element12"]),model="查看盘点模板断言")
        elif a=="3":
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element13"]),model="点击编辑盘点模板")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element14"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element15"]),eval(final_data[0]["element16"]),model="修改盘点模板断言")
        elif a == "4" :
            time.sleep(1)
            self.basepage.click_element(eval(final_data[0]["element17"]),model="点击停用盘点模板")
            self.driver.implicitly_wait(10)
            time.sleep(1)
            self.basepage.wait_text(eval(final_data[0]["element18"]),eval(final_data[0]["element19"]),model="停用盘点模板断言")
        elif a == "5" :
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element20"]),model="点击启用盘点模板")
            self.driver.implicitly_wait(10)
            time.sleep(1)
            self.basepage.wait_text(eval(final_data[0]["element21"]),eval(final_data[0]["element22"]),model="启用盘点模板断言")
        else:
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element23"]),model="点击删除盘点模板")
            self.driver.implicitly_wait(10)
            self.basepage.click_element(eval(final_data[0]["element24"]),model="二次确定删除")
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.basepage.wait_text(eval(final_data[0]["element25"]),eval(final_data[0]["element26"]),model="删除盘点模板断言")
    @pytest.mark.parametrize("a",["1","2"])
    #配送中心管理的查看和编辑，当A=1时为查看，当A等于2时为编辑
    @allure.story("配送中心查看/编辑（当A=1时为查看，当A等于2时为编辑）")
    @pytest.mark.test_007
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_007(self,a):
        final_data=Doexcel().get_test_data(data_list, "test_007")
        self.oms.OMS_p("A8")
        self.driver.implicitly_wait(10)
        if a =="1":
            time.sleep(2)
            ELE=self.driver.find_elements_by_class_name(eval(final_data[0]["element1"]))
            time.sleep(1)
            #先定位唯一class——name,再根据下标去确定唯一XPATH
            ELE[0].find_element_by_xpath(eval(final_data[0]["element2"])).click()
            self.driver.implicitly_wait(10)
            self.basepage.wait_eleVisible(eval(final_data[0]["element3"]),model="断言")
        else:
            time.sleep(2)
            ELE=self.driver.find_elements_by_class_name(eval(final_data[0]["element1"]))
            #先定位唯一class——name,再根据下标去确定唯一XPATH
            time.sleep(1)
            ELE[0].find_element_by_xpath(eval(final_data[0]["element4"])).click()
            #self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/main/div/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/button[2]/span"),model="点击编辑")
            self.driver.implicitly_wait(10)
            self.basepage.click_element(eval(final_data[0]["element5"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element6"]),eval(final_data[0]["element7"]),model="断言")
    #,"2","3"
    @pytest.mark.parametrize("a",["1","2","3"])
    #成本卡管理菜品成本卡的新增/所属门店/ 编辑 当A=1时为新增，当A等于2时为所属门店，当A=3时为编辑
    @allure.story("成本卡管理查看/编辑（当A=1时为新增，当A等于2时为所属门店，当A=3时为编辑）")
    @pytest.mark.test_008
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_008(self,a):
        final_data=Doexcel().get_test_data(data_list, "test_008")
        self.oms.OMS_p("A9")
        self.driver.implicitly_wait(10)
        if a == "1":
            time.sleep(2)
            self.basepage.click_element(eval(final_data[0]["element1"]),model="点击新增成本卡")
            self.driver.implicitly_wait(10)
            self.basepage.input_text(eval(final_data[0]["element2"]),number,model="输入成本卡名称")
            self.driver.implicitly_wait(10)
            self.basepage.click_element(eval(final_data[0]["element3"]),model="取消默认成本卡的勾选")
            self.driver.implicitly_wait(10)
            self.basepage.click_element(eval(final_data[0]["element4"]),model="选择品项")
            self.driver.implicitly_wait(10)
            time.sleep(3)
            ELE=self.driver.find_elements_by_class_name(eval(final_data[0]["element5"]))
            #/html/body/div[2]/div/div[2]/section/section/main/div/div
            #/html/body/div[2]/div/div[2]/section/section/main/div/div/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span
            #先定位唯一class——name,再根据下标去确定唯一XPATH
            ELE[1].find_element_by_xpath(eval(final_data[0]["element6"])).click()
            self.driver.implicitly_wait(10)
            ELE1=self.driver.find_elements_by_class_name(eval(final_data[0]["element7"]))
            #先定位唯一class——name,再根据下标去确定唯一XPATH
            #点击确定
            ELE1[1].find_element_by_xpath(eval(final_data[0]["element8"])).click()
            self.driver.implicitly_wait(10)
            self.basepage.input_text(eval(final_data[0]["element9"]),"10",model="输入净量")
            self.driver.implicitly_wait(10)
            self.basepage.click_element(eval(final_data[0]["element10"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element11"]),eval(final_data[0]["element12"]),model="断言")
        elif a == "2" :
            time.sleep(2)
            #//*[@id="app"]/div/div[2]/section/div/section/main/div[2]/section/main/div/div[1]/div[3]/table/tbody/tr[2]/td[5]/div/button[1]
            #self.basepage.click_element((By.XPATH,"//*[@id='app']/div/div[2]/section/div/section/main/div[2]/section/main/div/div[1]/div[3]/table/tbody/tr[2]/td[5]/div/button"),model="点击所属门店")
            ELE=self.driver.find_elements_by_class_name(eval(final_data[0]["element13"]))
            #先定位唯一class——name,再根据下标去确定唯一XPATH
            ELE[0].find_element_by_xpath(eval(final_data[0]["element14"])).click()
            self.driver.implicitly_wait(10)
            ELE1=self.driver.find_elements_by_class_name(eval(final_data[0]["element15"]))
            self.driver.implicitly_wait(10)
            self.basepage.click_element(eval(final_data[0]["element16"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element17"]),eval(final_data[0]["element18"]),model="断言")
        else:
            time.sleep(2)
            ELE=self.driver.find_elements_by_class_name(eval(final_data[0]["element19"]))
            #先定位唯一class——name,再根据下标去确定唯一XPATH
            ELE[0].find_element_by_xpath(eval(final_data[0]["element20"])).click()
            self.driver.implicitly_wait(10)
            self.basepage.clean_inputText(eval(final_data[0]["element21"]),model="清除净量")
            self.driver.implicitly_wait(10)
            self.basepage.input_text(eval(final_data[0]["element22"]),"10",model="输入净量")
            self.driver.implicitly_wait(10)
            self.basepage.click_element(eval(final_data[0]["element23"]),model="点击确定")
            self.driver.implicitly_wait(10)
            self.basepage.wait_text(eval(final_data[0]["element24"]),eval(final_data[0]["element25"]),model="断言")    
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(cur_path, f'../Report\\{now_time}')

    # -s : 打印信息
    # -m ：运行含标签的用例
    pytest.main(["--alluredir", report_path])
    # 解析测试报告，执行: allure serve {report_path}
    os.system(f"allure serve {report_path}")
