#coding=utf-8
# author:edwin

import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
from package.HTMLTestRunner import HTMLTestRunner
from public.models.newReport import new_report
from public.models.sendMail import send_mail

# 测试报告存放文件夹，如不存在，则自动创建一个report目录
if not os.path.exists(setting.TEST_REPORT):os.makedirs(setting.TEST_REPORT + '/' + "screenshot")

def add_case(test_path=setting.TEST_DIR):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='test_*.py')
    return discover

def run_case(all_case,result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""
    now = time.strftime("%Y%m%d%H%M%S")
    filename =  result_path + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='百度网站UI自动化测试报告demo',
                            description='环境：windows 10 浏览器：chrome',
                            tester='edwin')
    runner.run(all_case)
    fp.close()
    report = new_report(setting.TEST_REPORT) #调用模块生成最新的报告
    send_mail(report) #调用发送邮件模块

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)