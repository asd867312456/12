# -*- coding: utf-8 -*-
import requests
from inspect import modulesbyfile
import sys 
sys.path.append("..")
import os
import time
import pytest
import allure
from time import sleep
from Common.basePage import BasePage
from Common.excel_base import Doexcel
from Common.requestbase import RequestsHandler
from Common.assertbase import Assertions
from Common.token_base import headerdata
import random
data_list=Doexcel().excel_data_list('Config/oms_request.xls',"Sheet1")
asser=Assertions()
header_list=headerdata().header()
final_data1=Doexcel().get_test_data(data_list, "all")
class Test_request():
    def setup(self):
        print("1")
    @pytest.mark.parametrize("data",final_data1)
    def test_010(self,data):

        print(data["url"])
        if data["method"] == "get":
            if data["params"] != "" :
                requestdata=RequestsHandler().get_Req(url=data["url"],params=eval(data["params"]),headers=header_list,json=data["json"],data=data["data"])
                asser.assert_code(data['status_code'],requestdata.status_code)
            else:
                requestdata=RequestsHandler().get_Req(url=data["url"],params=data["params"],headers=header_list,json=data["json"],data=data["data"])
                asser.assert_code(data['status_code'],requestdata.status_code)
        elif data["method"] == "patch" :
             requestdata=RequestsHandler().patch_Req(url=data["url"],params=data["params"],headers=header_list,json=eval(data["json"]),data=data["data"])
             asser.assert_code(data['status_code'],requestdata.status_code)

         

    # @pytest.mark.parametrize("a",["1","2","3"])
    # #当A=1时为品项搜索，当A等于2时为品项查看，当A等于3时为品项编辑。。
    # @allure.story("品项管理接口搜索/查看/编辑，当A=1时为品项搜索，当A等于2时为品项查看，当A等于3时为品项编辑。")
    # @pytest.mark.test_001
    # @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    # def test_001(self,a):
    #     final_data=Doexcel().get_test_data(data_list, "test_001，test_002，test_003")
    #     if a == "1":
    #         requestdata=RequestsHandler().get_Req(url=final_data[0]['url'],params=eval(final_data[0]['params']),headers=header_list,json="",data="")
    #         print(requestdata.text)
    #         print(requestdata.url)
    #         print(requestdata.headers)
    #         asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
    #     elif a== "2":
    #         requestdata=RequestsHandler().get_Req(url=final_data[1]['url'],params="",headers=header_list,json="",data="")
    #         asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
    #     else:
    #         print(final_data[2]['url'])
    #         print(final_data[2]['bodys'])
    #         requestdata=RequestsHandler().patch_Req(url=final_data[2]['url'],params="",headers=header_list,json=eval(final_data[2]['json']),data="")
    #         asser.assert_code(final_data[2]['status_code'],requestdata.status_code)
    # @allure.story("接口门店管理-门店编辑")
    # @pytest.mark.test_002
    # @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    # def test_002(self):
    #     final_data=Doexcel().get_test_data(data_list,"test_004")
    #     requestdata=RequestsHandler().patch_Req(url=final_data[0]['url'],params="",headers=header_list,json=eval(final_data[0]['json']),data="")
    #     asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
    # @pytest.mark.parametrize("a",["1","2"])
    # #当A=1时为查看，当A等于2时为编辑
    # @allure.story("供应商接口查看/编辑（当A=1时为查看，当A等于2时为编辑）")
    # @pytest.mark.test_003
    # @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    # def test_003(self,a):
    #     final_data=Doexcel().get_test_data(data_list, "test_005，test_006")
    #     if a == "1":
    #         requestdata=RequestsHandler().get_Req(url=final_data[0]['url'],params="",headers=header_list,json="",data="")
    #         asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
    #     else:
    #         requestdata=RequestsHandler().patch_Req(url=final_data[1]['url'],params="",headers=header_list,json=eval(final_data[1]['json']),data="")
    #         asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
    def teardown(self):
        print("2")
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

