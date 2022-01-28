# -*- coding: utf-8 -*-
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
import random





url="https://supplychain.dev.jmj1995.com/items"
params={"pageNum":"1","pageSize":"20"}
hea={"authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJmMWQ0ZjA0MGJlY2U0NTQ1YTdkMGExZDUwYWE5MjM3MyIsImF1dGgiOiIiLCJpZCI6MTM2LCJzdWIiOiJwZW5namllIn0.y1U_gRL0wQ6h_8RTs-mrtaHd0x6LUQDvEXU3jHqDTvE4RtFPsoxuIyg01iwhk3nQhIC3ZoPZAjSs3x77IxSRTQ"}

data_list=Doexcel().excel_data_list('E:/12/Config/oms_request.xls',"Sheet1")
# print(data_list)
asser=Assertions()
# print(a.url)
# print(a.headers)

class Test_request():
    def setup(self):
        print("1")
    def test_001(self):
        final_data=Doexcel().get_test_data(data_list, "test_001")
        # print(final_data)
        # print(final_data[0]['url'])
        requestdata=RequestsHandler().get_Req(url=final_data[0]['url'],params=eval(final_data[0]['params']),headers=eval(final_data[0]['headers']),json="",data="")
        print(requestdata.text)
        print(requestdata.status_code)
        asser.assert_code(200,requestdata.status_code)
        # reques=requests.get(url=final_data[0]['url'],params=eval(final_data[0]['params']),headers=eval(final_data[0]['headers']))
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

