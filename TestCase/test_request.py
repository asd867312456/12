# -*- coding: utf-8 -*-
from re import T
from tokenize import Token
import requests

from inspect import modulesbyfile
import sys 
sys.path.append(".")
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
data_list=Doexcel().excel_data_list('Config\oms_request.xls',"Sheet1")
asser=Assertions()
header_list=headerdata().header()
class Test_request():
    def setup(self):
        print("1")
    @pytest.mark.parametrize("a",["1","2","3"])
    #当A=1时为品项搜索，当A等于2时为品项查看，当A等于3时为品项编辑。
    @allure.story("品项管理接口搜索/查看/编辑，当A=1时为品项搜索，当A等于2时为品项查看，当A等于3时为品项编辑。")
    @pytest.mark.test_001
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    def test_001(self,a):
        final_data=Doexcel().get_test_data(data_list, "test_001，test_002，test_003")
        if a == "1":
            requestdata=RequestsHandler().get_Req(url=final_data[0]['url'],params=eval(final_data[0]['params']),headers=header_list,json="",data="")
            asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
        elif a== "2":
            requestdata=RequestsHandler().get_Req(url=final_data[1]['url'],params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
        else:
            print(final_data[2]['url'])
            print(final_data[2]['bodys'])
            requestdata=RequestsHandler().patch_Req(url=final_data[2]['url'],params="",headers=header_list,json=eval(final_data[2]['bodys']),data="")
            asser.assert_code(final_data[2]['status_code'],requestdata.status_code)
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

