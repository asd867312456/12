# -*- coding: utf-8 -*-
"""
封装Assert方法
"""
import json
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

class Assertions:
    def __init__(self):
      self.logger = MyLog().getLog()
    
    def assert_code(self,code,url_code):
        """
        验证response状态码
        """
        self.logger.info(f'预计接口返回code为"{code}",实际返回code为:"{url_code}"')
        try:
            assert code == url_code
            self.logger.info(f'预计接口返回code为"{code}",实际返回code为:"{url_code}"')
        except:
            self.logger.error(f'预计接口返回code为"{code}",实际返回code为:"{url_code}",失败')   
            raise
    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            self.logger.info(
                "Response body msg == expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body[body_msg]))
            # return True

        except:
            self.logger.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body[body_msg]))

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            # return True

        except:
            self.logger.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            # return True

        except:
            self.logger.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
 

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            # return True

        except:
            self.logger.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))

            raise
    