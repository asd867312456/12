# -*- coding: utf-8 -*-
import os
import time
import pytest
import shutil

if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    
    # report_path = os.path.join(cur_path, f'Report\\{now_time}')
    # #暂时定死
    #运行前先删除再新增
    shutil.rmtree("Report")
    report_path = os.path.join(cur_path, "Report")

    # -s : 打印信息
    # -m ：运行含标签的用例
    pytest.main(["--alluredir", report_path])
    # 解析测试报告，执行: allure serve {report_path}
    os.system(f"allure serve {report_path}")

