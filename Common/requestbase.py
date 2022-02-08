#
import sys
sys.path.append(".")
import requests
import logging
import os
import time
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Utils.myLog import MyLog

class RequestsHandler():
    def __init__(self):
        self.logger = MyLog().getLog()
    ## '''封装一个get方法，发送get请求'''
    def get_Req(self,url,data,json,headers,params):
        self.logger.info(f'连通接口"{url}",接口header为:"{headers}",接口param为：{params}')
        try:
            start=datetime.now()
            res=requests.get(url=url,headers=headers,params=params,data=data,json=json,verify=False)
            end=datetime.now()
            self.logger.info(f'等待接口"{url}"时长:{end - start}')
        except:
             self.logger.exception(f'等待接口"{url}"失败')
        else:
            return res
    def post_Req(self,url,data,json,headers,params):
        # '''封装一个post方法，发送post请求'''
        self.logger.info(f'连通接口"{url}",接口data为:"{data}",接口json{json}')
        try:
            start=datetime.now()
            res=requests.post(url=url,headers=headers,data=data,json=json,params=params,verify=False)
            end=datetime.now()
            self.logger.info(f'等待接口"{url}"时长:{end - start}')
        except:
             self.logger.exception(f'等待接口"{url}"失败')
        else:
            return res
    def put_Req(self,url,data,json,headers,params):
         # '''封装一个put方法，发送put请求'''
        self.logger.info(f'连通接口"{url}",接口data为:"{data}",接口json{json}')
        try:
            start=datetime.now()
            res=requests.put(url=url,data=data,headers=headers,json=json,params=params,verify=False)
            end=datetime.now()
            self.logger.info(f'等待接口"{url}"时长:{end - start}')
        except:
             self.logger.exception(f'等待接口"{url}"失败')
        else:
            return res
    def delete_Req(self,url,data,json,headers,params):
        # '''封装一个delete方法，发送delete请求'''
        self.logger.info(f'连通接口"{url}",接口data为:"{data}",接口json{json}')
        try:
            start=datetime.now()
            res=requests.put(url=url,data=data,headers=headers,json=json,params=params,verify=False)
            end=datetime.now()
            self.logger.info(f'等待接口"{url}"时长:{end - start}')
        except:
             self.logger.exception(f'等待接口"{url}"失败')
        else:
            return res
    def patch_Req(self,url,data,json,headers,params):
         # '''封装一个patch方法，发送patch请求'''
        self.logger.info(f'连通接口"{url}",接口data为:"{data}",接口json{json}')
        try:
            start=datetime.now()
            res=requests.patch(url=url,data=data,headers=headers,json=json,params=params,verify=False)
            end=datetime.now()
            self.logger.info(f'等待接口"{url}"时长:{end - start}')
        except:
             self.logger.exception(f'等待接口"{url}"失败')
        else:
            return res