# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

'''
这时封装好的的email发送类，可以发送各种email消息，使用方法见main中。
'''

import datetime
import smtplib
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

"""
smtp服务器参数
"""
smtp_host = 'smtp.163.com'
smtp_user = 'yunweiall@163.com'
smtp_port = 25
ssl_port = 465
tls_port = 587
smtp_password = 'SPSZUEPDSVTWVDTK'
from_user_name = 'ops_auto'
from_user = 'yunweiall@163.com'
to_user = 'lisonfan@lexin.com'

title = '这时测试邮件标题'
text = '这时测试邮件内容正文'
msg = MIMEText(text)
msg['Subject'] = title
# msg['From'] = from_user
msg['From'] = formataddr(['FLS', from_user])
msg['To'] = to_user


class SendMail():
    def __init__(self, receiver, subject, ssl=False, tls=False, debuglevel=0, encoding='utf-8'):
        '''
        初始化邮件发送对象：支持明文/ssl/tls 三种发送方式，注意，163的邮箱目前支持 tls 协议
        :param receiver:  收件人，list 类型 ['124@163.com','xxx@qq.com']
        :param subject:  邮件标题
        :param ssl: 是否开启 ssl 登陆
        :param tls 使用 tls 登陆
        :param  debuglevel： 设置 debug 级别，默认是 0 ，可以设置为 1、2、True
        :param encoding: 设置编码  默认的都是 utf-8
        '''
        self.receiver = receiver
        self.subject = subject
        self.ssl = ssl
        self.tls = tls
        self.debuglevel = debuglevel
        self.encoding = encoding

        self.msg = MIMEMultipart('mixed')
        '''
        默认值为 mixed。定义 mixed实现构建一个带附件的邮件体；
        定义related 实现构建内嵌资源的邮件体；
        定义alternative 则实现构建纯文本与超文本共存的邮件体；
        _subparts是有效负载的一系类初始部分，可以使用attach()方法将子部件附加到消息中。 
        '''
        self.msg['Subject'] = subject
        self.msg['From'] = '{} <{}>'.format(from_user_name, from_user)
        # self.msg['From'] = formataddr(['FLS', from_user])
        self.msg['To'] = ';'.join(receiver)
        self.msg['Date'] = '{}'.format(datetime.datetime.now())

    def add_text(self, text_plain):
        '''
        发送文本内容
        :param text_plain: 字符串文件，可以使用回车换行等符号
        :return:
        '''
        text_plain = MIMEText(text_plain, 'plain', self.encoding)
        self.msg.attach(text_plain)

    def add_img(self, img_name, sendimgfile):
        '''
        发送图片附件:
        示例：
            sendimgfile=open(img_path,'rb).read()
            send_img('img_name',sendimgfile)
        :param img_name: 图片文件名
        :param imgfile:  图片文件字节流
        :return:
        '''
        image = MIMEImage(sendimgfile)
        image.add_header('Content-ID', 'Image')
        image['Content-Disposition'] = 'attachment; filename="{}"'.format(img_name)
        self.msg.attach(image)

    def add_html(self, htmlfile):
        '''
        发送 html文件
        :param htmlfile: html文件路径
        :return:
        '''
        text_html = MIMEText(htmlfile, 'html', self.encoding)
        text_html['Content-Disposition'] = 'attachment; filename="{}"'.format(htmlfile)
        self.msg.attach(text_html)

    def add_file(self, filename, sendfile):
        '''
        发送文件:
        示例：
            sendfile=open(r'aaaa.txt','rb').read()
            add_file('filename',sendfile)
        :param filename:  附件名字
        :param sendfile:  附件内容，字节流
        :return:
        '''
        text_att = MIMEText(sendfile, 'bash64', self.encoding)
        text_att['Content_type'] = 'application/octet-stream'
        # text_att.add_header('Content-Disposition', 'attachment', filename=filename)
        text_att['Content-Disposition'] = 'attachment;filename="%s"' % (filename)

        self.msg.attach(text_att)

    def add_audio(self, audioname, audiofile):
        '''
        添加音频附件:
        示例：
            sendaudio=open('1.wav','rb).read()
            add_audio('audioname',auduifile)
        :param audioname: 音频文件名称
        :param audiofile: 音频文件的字节码
        :return:
        '''

        audio = MIMEAudio(audiofile, 'plain')
        audio.add_header('Content-Disposition', 'attachment', filename='{}'.format(audioname))
        self.msg.attach(audio)

    # 使用 MIMEBase基类来添加附件, 添加附件就是加上一个MIMEBase，
    def add_mimebase_file(self, filename, file):
        mimebase = MIMEBase('application', 'octet-stream')
        mimebase.add_header('Content-Disposition', 'attachment', filename='{}'.format(filename))
        mimebase.add_header('Content-ID', '<0>')
        mimebase.add_header('X-Attachment-Id', '0')
        mimebase.set_payload(file)
        encoders.encode_base64(mimebase)
        self.msg.attach(mimebase)

    # 将图片插在正文的html中，
    def add_img_to_text(self, imgname, imgfile, text):
        mimebase = MIMEBase('application', 'octet-stream')
        mimebase.add_header('Content-Disposition', 'attachment', filename='{}'.format(imgname))
        mimebase.add_header('Content-ID', 'Image')
        mimebase.add_header('X-Attachment-Id', '0')
        mimebase.set_payload(imgfile)
        encoders.encode_base64(mimebase)
        self.msg.attach(mimebase)

        text_plain = MIMEText('<html><body><p>' + text + '</p>'
                                                         '<p><img src="cid:Image"></p>'
                                                         '</body></html>', 'html', self.encoding)
        self.msg.attach(text_plain)

    def add_html_to_text(self, html):
        msg = MIMEText(html, 'html', self.encoding)

    def send(self):
        if self.tls:
            smtp = smtplib.SMTP(smtp_host, tls_port)
            smtp.starttls()
        elif self.ssl:
            smtp = smtplib.SMTP_SSL(smtp_host, ssl_port)
        else:
            smtp = smtplib.SMTP(smtp_host, smtp_port)
        smtp.set_debuglevel(self.debuglevel)
        try:
            smtp.login(smtp_user, smtp_password)
            smtp.sendmail(from_user, self.receiver, self.msg.as_string())
        except smtplib.SMTPException as e:
            raise Exception('发送邮件失败: %s' % e)
        smtp.quit()
        print('发送邮件完成.')


if __name__ == '__main__':
    s = SendMail(['lisonfan@lexin.com'], '日报')
    sendfile = open('shuju.xlsx', 'rb').read()
    # s.add_file('shujutongji.xlsx',sendfile)
    s.add_mimebase_file('数据统计.xlsx', sendfile)
    s.send()
