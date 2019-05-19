import unittest,time
from common import HTMLTestRunner

# 定义测试用例的目录为当前目录
# test_dir = 'D:\\test_project\\test_case'
test_dir = './test_case/'
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