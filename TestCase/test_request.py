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
number=str(99)+"".join(random.sample(["0","1","2","3","4","5","6","7","8","9"],9))
data_list=Doexcel().excel_data_list('Config/oms_request.xls',"Sheet1")
asser=Assertions()
header_list=headerdata().header()
final_data1=Doexcel().get_test_data(data_list, "all")
class Test_request():
    def setup(self):
        print("1")
        self.g = globals()
    # @pytest.mark.parametrize("data",final_data1)
    # def test_010(self,data):
    #     if data["params"] != "":
    #         params=eval(data["params"])
    #     else:
    #         params=data["params"]
    #     if data["json"] != "":
    #         json=eval(data["json"])
    #     else:
    #         json=data["json"]
    #     if data["data"] != "":
    #         data1=eval(data["data"])
    #     else:
    #         data1=data["data"]
    #     if data["method"] == "get":
    #         requestdata=RequestsHandler().get_Req(url=data["url"],params=params,headers=header_list,json=json,data=data1)
    #         asser.assert_code(data['status_code'],requestdata.status_code)
    #     elif data["method"] == "patch" :
    #          requestdata=RequestsHandler().patch_Req(url=data["url"],params=params,headers=header_list,json=json,data=data1)
    #          asser.assert_code(data['status_code'],requestdata.status_code)
    #     elif data["method"] == "post" :
    #          requestdata=RequestsHandler().post_Req(url=data["url"],params=params,headers=header_list,json=json,data=data1)
    #          asser.assert_code(data['status_code'],requestdata.status_code)
    #          datas=requestdata.json()
             
    #     elif data["method"] == "put" :
    #          requestdata=RequestsHandler().put_Req(url=data["url"],params=params,headers=header_list,json=json,data=data1)
    #          asser.assert_code(data['status_code'],requestdata.status_code)
    #     elif data["method"] == "delete" :
    #          requestdata=RequestsHandler().delete_Req(url=data["url"],params=params,headers=header_list,json=json,data=data1)
    #          asser.assert_code(data['status_code'],requestdata.status_code)
         

    @pytest.mark.parametrize("a",["1","2","3"])
    #当A=1时为品项搜索，当A等于2时为品项查看，当A等于3时为品项编辑。。
    @allure.story("品项管理接口搜索/查看/编辑，当A=1时为品项搜索，当A等于2时为品项查看，当A等于3时为品项编辑。")
    @pytest.mark.test_001
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_001(self,a):
        final_data=Doexcel().get_test_data(data_list, "test_001，test_002，test_003")
        if a == "1":
            requestdata=RequestsHandler().get_Req(url=final_data[0]['url'],params=eval(final_data[0]['params']),headers=header_list,json="",data="")
            print(requestdata.text)
            print(requestdata.url)
            print(requestdata.headers)
            asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
        elif a== "2":
            requestdata=RequestsHandler().get_Req(url=final_data[1]['url'],params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
        else:
            requestdata=RequestsHandler().patch_Req(url=final_data[2]['url'],params="",headers=header_list,json=eval(final_data[2]['json']),data="")
            asser.assert_code(final_data[2]['status_code'],requestdata.status_code)
    @allure.story("接口门店管理-门店编辑")
    @pytest.mark.test_002
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_002(self):
        final_data=Doexcel().get_test_data(data_list,"test_004")
        requestdata=RequestsHandler().patch_Req(url=final_data[0]['url'],params="",headers=header_list,json=eval(final_data[0]['json']),data="")
        asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
    @pytest.mark.parametrize("a",["1","2"])
    #当A=1时为查看，当A等于2时为编辑
    @allure.story("供应商接口查看/编辑（当A=1时为查看，当A等于2时为编辑）")
    @pytest.mark.test_003
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_003(self,a):
        final_data=Doexcel().get_test_data(data_list, "test_005，test_006")
        if a == "1":
            requestdata=RequestsHandler().get_Req(url=final_data[0]['url'],params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
        else:
            requestdata=RequestsHandler().patch_Req(url=final_data[1]['url'],params="",headers=header_list,json=eval(final_data[1]['json']),data="")
            asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
    @pytest.mark.parametrize("a",["1","2","3","4"])
    #当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为删除。
    @allure.story("员工餐新增/查看/编辑/删除，当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为删除。")
    @pytest.mark.test_004
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_004(self,a):
        final_data=Doexcel().get_test_data(data_list,"test_007,test_008,test_009,test_010,test_011,test_012,test_013,test_014")
        if a == "1" :
            json={"itemGroupInfo":{"name":number,"remark":""},"itemIdList":[1],"relatedOrganizationList":[{"organizationType":"SHOP","organizationId":"31","organizationName":"太二广州海珠万达分店"}]}
            requestdata=RequestsHandler().post_Req(url=final_data[0]['url'],params="",headers=header_list,json=json,data="")
            id=requestdata.json()
            self.g['a'] = id
            asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
        elif a == "2" :
            id1=str(self.g['a'])
            print(id1)
            #查看模板名称
            url1=final_data[1]['url']+id1
            print(url1)
            requestdata=RequestsHandler().get_Req(url=url1,params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
            #查看模板所属门店
            url2=final_data[0]['url']+id1+"/relatedOrganizations"
            requestdata=RequestsHandler().get_Req(url=url2,params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[2]['status_code'],requestdata.status_code)
            #查看模板所属品项
            url3=final_data[0]['url']+id1+"/items"
            requestdata=RequestsHandler().get_Req(url=url3,params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[3]['status_code'],requestdata.status_code)
        elif a =="3":
            id1=str(self.g['a'])
            print(id1)
            #编辑模板名称
            url1=final_data[4]['url']+id1
            print(url1)
            json1={"name":number,"remark":"655555"}
            requestdata=RequestsHandler().put_Req(url=url1,params="",headers=header_list,json=json1,data="")
            asser.assert_code(final_data[4]['status_code'],requestdata.status_code)
            #编辑模板所属门店
            url2=final_data[5]['url']+id1+"/relatedOrganizations"
            requestdata=RequestsHandler().put_Req(url=url2,params="",headers=header_list,json=eval(final_data[5]["json"]),data="")
            asser.assert_code(final_data[5]['status_code'],requestdata.status_code)
            #编辑模板所属品项
            url3=final_data[6]['url']+id1+"/items"
            requestdata=RequestsHandler().put_Req(url=url3,params="",headers=header_list,json=eval(final_data[6]["json"]),data="")
            asser.assert_code(final_data[6]['status_code'],requestdata.status_code)
        else :
            id1=str(self.g['a'])
            print(id1)
            #删除模板
            print(number)
            url1=final_data[7]['url']+id1
            requestdata=RequestsHandler().delete_Req(url=url1,params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[7]['status_code'],requestdata.status_code)
    @pytest.mark.parametrize("a",["1","7","2","3","4","5","6"])
    #盘点模板新增/查看/编辑/停用/启用/删除，当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为停用，当A=5时为启用，当A=6时为删除
    @allure.story("盘点模板新增/查看/编辑/停用/启用/删除，当A=1时为新增，当A等于2时为查看，当A等于3时为编辑，当A等于4时为停用，当A=5时为启用，当A=6时为删除,当A=7时为查询")
    @pytest.mark.test_005
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_005(self,a):
        final_data=Doexcel().get_test_data(data_list,"test_015,test_016,test_017,test_018,test_019,test_020,test_021")
        if a == "1" :
            json1={"name":number,"type":"WEEK_INVENTORY","inventoryDay":"MONDAY","remark":"121212","enable":"true","itemList":[{"itemId":1,"remark":""}],"shopList":[{"shopId":1}]}
            requestdata=RequestsHandler().post_Req(url=final_data[0]['url'],params="",headers=header_list,json=json1,data="")
            asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
            print(number)
        #查询列表所有模板取最后一条模板ID
        elif a == "7":
            requestdata=RequestsHandler().get_Req(url=final_data[6]['url'],params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[6]['status_code'],requestdata.status_code)
            # print(requestdata.text)
            data=requestdata.json()
            id=data["list"][data["total"]-1]["id"]
            self.g['a']=id
        elif a == "2" :
            id1=str(self.g['a'])
            #查看模板名称
            url1=final_data[1]['url']+id1
            requestdata=RequestsHandler().get_Req(url=url1,params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
        elif a == "3":
            id1=str(self.g['a'])
            json2={"id":id1,"name":number,"type":"WEEK_INVENTORY","inventoryDay":"MONDAY","remark":number,"enable":"true","defaultTemplate":"false","itemList":[{"itemId":1,"remark":""}],"shopList":[{"shopId":1}]}
            url2=final_data[2]['url']
            requestdata=RequestsHandler().put_Req(url=url2,params="",headers=header_list,json=json2,data="")
            asser.assert_code(final_data[2]['status_code'],requestdata.status_code)
        elif a == "4":
            id1=str(self.g['a'])
            url3=final_data[3]['url']+id1+"/enable/false"
            requestdata=RequestsHandler().post_Req(url=url3,params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[3]['status_code'],requestdata.status_code)
        elif a == "5":
            id1=str(self.g['a'])
            url3=final_data[4]['url']+id1+"/enable/true"
            requestdata=RequestsHandler().post_Req(url=url3,params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[4]['status_code'],requestdata.status_code)
        elif a == "6":
            id1=str(self.g['a'])
            url3=final_data[5]['url']+id1
            requestdata=RequestsHandler().delete_Req(url=url3,params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[5]['status_code'],requestdata.status_code)
    @pytest.mark.parametrize("a",["1","2"])
    #配送中心管理的查看和编辑，当A=1时为查询，当A等于2时为编辑
    @allure.story("配送中心查看/编辑（当A=1时为查询，当A等于2时为编辑）")
    @pytest.mark.test_006
    @pytest.mark.flaky(reruns=1,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_006(self,a):
        final_data=Doexcel().get_test_data(data_list,"test_022,test_023")
        if a == "1" : 
            requestdata=RequestsHandler().get_Req(url=final_data[0]['url'],params="",headers=header_list,json="",data="")
            asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
        else:
            requestdata=RequestsHandler().put_Req(url=final_data[1]['url'],params="",headers=header_list,json=eval(final_data[1]["json"]),data="")
            asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
    @pytest.mark.parametrize("a",["1","2","3"])
    #成本卡管理菜品成本卡的新增/所属门店/ 编辑 当A=1时为新增，当A等于2时为所属门店，当A=3时为编辑
    @allure.story("成本卡管理菜品成本卡的新增/所属门店/ 编辑 当A=1时为新增，当A等于2时为所属门店，当A=3时为编辑")
    @pytest.mark.test_007
    @pytest.mark.flaky(reruns=0,reruns_delay=10)
    # @pytest.mark.skip(reason="调式")
    def test_007(self,a):
        final_data=Doexcel().get_test_data(data_list,"test_024,test_025,test_026")
        if a == "1":
            json={"dishId":529,"name":number,"preferred":"false","seasoningCost":12,"specification":"小粉","list":[{"rank":1,"grossUsage":10,"itemId":1,"netFeedRate":100,"netUsage":10}]}
            requestdata=RequestsHandler().post_Req(url=final_data[0]['url'],params="",headers=header_list,json=json,data="")
            asser.assert_code(final_data[0]['status_code'],requestdata.status_code)
        elif a =="2":
            requestdata=RequestsHandler().post_Req(url=final_data[1]['url'],params="",headers=header_list,json=eval(final_data[1]["json"]),data="")
            asser.assert_code(final_data[1]['status_code'],requestdata.status_code)
            print(requestdata.status_code)
        else:
            requestdata=RequestsHandler().post_Req(url=final_data[2]['url'],params="",headers=header_list,json=eval(final_data[2]["json"]),data="")
            asser.assert_code(final_data[2]['status_code'],requestdata.status_code)
            print(requestdata.status_code)
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

