import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def mail(To, CC, Subject, Content, mail_user, mail_pass, mail_host):
    try:
        mail_host = mail_host  # 设置第三方SMTP 服务器主机
        mail_user = mail_user  # 发件人 用户名
        mail_pass = mail_pass  # 发件人口令
        split = ','
        receivers = []
        if To:  # 收件人
            to_reciver = To.split(split)
            receivers += to_reciver
        if CC:  # 抄送
            cc_reciver = CC.split(split)
            receivers += cc_reciver

        message = MIMEMultipart()
        message['From'] = Header(mail_user, 'utf-8')
        message['To'] = split.join(to_reciver)
        if CC:
            message['Cc'] = split.join(cc_reciver)
        subject = Subject  # 邮件主题
        message['Subject'] = Header(subject, 'utf-8')
        content = Content  # 正文
        message.attach(MIMEText(content, 'html', 'gb18030'))

        smtpObj = smtplib.SMTP()  # 创建smtp示例
        smtpObj.connect(mail_host)  # 连接邮件主机
        smtpObj.login(mail_user, mail_pass)  # 登录
        smtpObj.sendmail(mail_user, receivers, message.as_string())  # 发送
        smtpObj.quit()  # 退出
    except:
        print("Error: SEND FAIL")
