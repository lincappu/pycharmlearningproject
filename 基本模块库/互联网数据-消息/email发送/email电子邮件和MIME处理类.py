# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


'''
python内置的发送邮件的方式。主要使用smtplib和email：
email用来构造邮件结构体
smtplib来发送邮件
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

'''
在下面提前定义 smtp 服务器需要的参数
'''
smtp_host = 'smtp.163.com'
smtp_user = 'lincappu1@163.com'
smtp_port = 25
ssl_port = 465
tls_port = 587
smtp_password = 'lin111555'
from_user_name = 'Test'
from_user = 'lincappu1@163.com'
to_user = 'fanliusong@whrhkj.com'

title = '这时测试邮件标题'
text = '这时测试邮件内容正文'
msg = MIMEText(text)
msg['Subject'] = title
# msg['From'] = from_user
msg['From'] = formataddr(['FLS',from_user])
msg['To'] = to_user

# 简单写法：
# mail_server = smtplib.SMTP()
# mail_server.connect(host=smtp_host, port=smtp_port)

# mail_server = smtplib.SMTP(host=smtp_host,port=smtp_port)
# mail_server.login(user=from_user,password=smtp_password)
# mail_server.sendmail(from_addr=from_user,to_addrs=to_user,msg=msg.as_string())
# mail_server.quit()
# print("发送成功。")



'''
MIME实例对象的方法：
as_string() ：返回字符串信息，相当于__str__(),str(msg)
as_bytes() ：返回字节信息，相当于__bytes__(),bytes(msg)
is_multipart() ：判断是否为有效载荷的列表message对象，是返回True,否则返回False
set_unixfrom(unixfrom) ：将消息的信封头设置为unixfrom为字符串
get_unixfrom() ：返回消息的信封头。默认为None
attach(payload) ：将给定的有效负载添加到当前有效负载
get_payload(i=None, decode=False) ：返回当前的有效载荷，这将是一个列表 Message
set_payload(payload, charset=None) :将整个消息对象的有效载荷设置为有效载荷
set_charset(charset) ；将有效负载的字符集设置为charset
get_charset() :返回Charset与消息有效负载相关的实例
__len__() :返回标题的总数，包括重复项
__contains__(name) :如果消息对象具有名为name的字段，则返回true
__getitem__(name) :返回指定标题字段的值
__setitem__(name, val) :将字段添加到带有字段名称和值val的消息中
__delitem__(name) :从消息的标题中删除所有出现的具有名称name的字段
keys() :返回所有消息标题字段名称的列表
values() :返回所有消息字段值的列表
items() ：返回包含所有消息的字段标题和值
add_header(_name, _value, **_params) :扩展标题设置,_name为要添加的标题字段，_value为标题的值。



msg.add_header('Content-ID','imgid')   #设置图片ID
msg.add_header('Content-Disposition','attachment',filename='test.xlsx') #为附件添加一个标题
msg.add_header('Content-Disposition','attachment',filename=('utf-8','','中文标题')) #添加非ASCII字符时需指定编码


email.header.Header(s=None,charset=None)：创建一个可以包含不同字符集中的字符串，并符合MIME的标头。
可选参数:s是初始标题值默认为None,可以使用append()方法追加到标题，charset指定字符集
from email.header import Header
msg['From'] = Header("测试邮件来自",'utf-8')


附加工具：email.utils
email.utils.localtime(dt=None) ：返回当前时间，dt参数为datetime实例
email.utils.formataddr(pair,charset='utf-8')　　：pair是一个元祖或列表返回分割的标题和地址如邮箱收件人昵称和邮箱账号
from email.utils import formataddr
msg['From'] = formataddr(['Meslef','92066@163.com'])
msg['To'] = formataddr(['Anybody','92066@163.com'])
'''




# 创建 related 类型的 mutilpart 对象来定义内嵌资源邮件体
msg=MIMEMultipart('related')

def addimg(self,src,imgid):
    with open(src,'rb') as f:
        msgimage=MIMEImage(f.read())
    msgimage.add_header('Content-ID',imgid)
    return msgimage


def  relate_html(self):
    text = """  
    <table width="600" border="0" cellspacing="0" cellpadding="4">
        <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
            <td colspan=2>*系统性能数据 <a href="10.0.0.10"> 更多 >></a></td>
        </tr>
        <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
                <img src="cid:io">   #图片地址由MIMEMultipart通过ID传递
            </td>
            <td>
                <img src="cid:key_hit">
            </td>
        </tr>
        <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
                <img src="cid:men">
            </td>
            <td>
                <img src="cid:swap">
            </td>
        </tr>
    </table>
    """

    msgtext=MIMEText(text,'html','utf-8')

    msg.attach(msgtext)
    msg.attach(addimg('1.jpg','io'))
    msg.attach(addimg('2.jpg','key_hit'))
    msg.attach(addimg('3.jpg','men'))
    msg.attach(addimg('4.jpg','swap'))







# 封装发送邮件的类
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

    # 将图片插在邮件正文中。
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
        except Exception as e:
            raise Exception('发送邮件失败: %s' % e)
        smtp.quit()
        print('发送邮件完成.')


if __name__ == '__main__':
    em_obj = SendMail(['fanliusong@whrhkj.com'], '测试邮件')

    em_obj.add_text('测试邮件，无需回复')
    # try:
    #     sendfile = open('1.log', 'rb').read()
    # except Exception as e:
    #     raise Exception('附件打不开.%s' % e)
    #
    # try:
    #     sendimgfile = open('1.jpg', 'rb').read()
    # except Exception as e:
    #     raise Exception("图片打不开. %s" % e)

    # em_obj.add_img('1.jpg', sendimgfile)
    # em_obj.add_file('1.log', sendfile)
    # em_obj.add_html('1.html')
    # with open('1.docx', 'rb') as f:
    #     em_obj.add_mimebase_file('1.docx', f.read())

    # imgfile=open('1.jpg', 'rb').read()
    # em_obj.add_img_to_text('1.jpg',imgfile, 'nihaoma?')

    # with open('1.wav', 'rb') as f:
    #     audiofile = f.read()
    # em_obj.add_audio('1.wav', audiofile)

    em_obj.send()
