import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(new_report_file):
    # 发送邮箱服务器
    smtpserver = 'smtp.126.com'
    # 发送邮箱用户和密码
    user = '***@126.com'
    password = '****'     # 授权码，不是邮箱密码

    # 发送邮箱
    sender = '***@126.com'
    # 接受邮箱
    receiver = '***@qq.com'
    # 发送邮件主题
    subject = '自动化测试报告'

    # 报告以html文件发送报告邮件
    a = open(new_report_file, 'rb')
    sendfile = a.read()
    a.close()

    # 编写HTML类型的邮件正文
    # msg = MIMEText('<html><h1>自动化测试学习发邮件，这是正经的邮件</h1></html>', 'html', 'utf-8')
    msg = MIMEText(sendfile, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    '''
    # 以附件形式发送报告
    sendfile = open(new_report_file, 'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['content-Disposition'] = 'attachment; filename="测试报告"'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    msgRoot.attach(att)
'''

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())     # 发送正文使用
    # smtp.sendmail(sender, receiver, msgRoot.as_string())   # 发送附件使用
    smtp.quit()
    print("邮件已经发送")

