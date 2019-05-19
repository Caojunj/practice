import os


def new_report(result_dir):
    # 定义文件目录
    # result_dir = 'D:\\test_project\\report'

    lists = os.listdir(result_dir)
    # 重新按时间对目录下文件进行排序
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + '\\' + fn))
    # print("最新的文件为：" + lists[-1])
    new_report_file = os.path.join(result_dir, lists[-1])
    print("最新文件路径为：" + new_report_file)
    return new_report_file
