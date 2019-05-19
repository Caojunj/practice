import unittest
import time
from common import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from common import send_mail
from common import find_file
import os


# 找到用例并执行用例
# test_dir = 'D:\\test_project\\test_case'
test_dir = './test_case/'   # 用例地址
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + 'result.html'
    ft = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=ft, title='测试报告', description='用例执行情况')
    runner.run(discover)
    ft.close()

    # -------找到最新的测试报告
    result_dir = 'D:\\test_project\\report'  # 报告地址
    a = find_file.new_report(result_dir)

    # -------定于发送邮件
    send_mail.send_mail(a)
