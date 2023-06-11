# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import difflib

# tex1 = """tex1:
# this is a test for difflib ,just try to get difference of the log
# 现在试试功能是否可行 好呀
# goodtest
# 那么试试吧好人
"""
# tex1_lines = tex1.splitlines()
# tex2 =
# this is a test for difflib ,just try to get difference of the log
# 现在试试功能是否可行
# goodtast
# 那么试试吧
# """
text1='''
spring:
  mail:
    host: smtp.whrhkj.com
    username: mainadmin@whrhkj.com
    password: 'mainadmin@2019'
    properties.mail.smtp.auth: true
    properties.mail.smtp.port: 465
    properties.mail.display.sendmail: 重置密码
    properties.mail.display.sendname: 仁和会计企业管理平台
    properties.mail.smtp.starttls.enable: true
    properties.mail.smtp.starttls.required: true
    properties.mail.smtp.ssl.enable: true
    default-encoding: utf-8
    from: mainadmin@whrhkj.com
  datasource:
    url: jdbc:mysql://172.16.1.122:3669/rh-cas-pro?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&useSSL=false
    username: root
    password: redhat2019@
    type: com.alibaba.druid.pool.DruidDataSource
    druid:
      initial-size: 5
      min-idle: 5
      max-active: 20
      max-wait: 60000
      test-while-idle: true
      time-between-eviction-runs-millis: 60000
      min-evictable-idle-time-millis: 30000
      validation-query: select 'x'
      test-on-borrow: false
      test-on-return: false
      max-pool-prepared-statement-per-connection-size: 20
      #      filters: stat,wall
      # 状态监控
      filter:
        stat:
          enabled: true
          db-type: mysql
          log-slow-sql: true
          slow-sql-millis: 2000
      connect-properties: druid.stat.mergeSql=true;druid.stat.slowSqlMillis=5000
      use-global-data-source-stat: true
      # 监控过滤器
      web-stat-filter:
        enabled: true
        exclusions:
          - "*.js"
          - "*.gif"
          - "*.jpg"
          - "*.png"
          - "*.css"
          - "*.ico"
          - "/druid/*"
      # druid 监控页面
      stat-view-servlet:
        enabled: true
        url-pattern: /druid/*
        reset-enable: false
        login-username: admin
        login-password: admin
      aop-patterns: com.whrhkj.casspringservice.service.*
  redis:
    database: 10
    host: 172.16.8.175
    port: 6379
    password: UZ8CBGjifqdM5m0sInQ2
    timeout: 10000ms
    lettuce:
      pool:
        max-active: 16
        max-idle: 8
        max-wait: 1000ms
        min-idle: 0

server:
  port: 10077
  servlet:
    context-path: /cas

###OKHTTP
ok-http:
  connect-timeout: 30
  read-timeout: 30
  write-timeout: 30
  max-idle-connections: 200
  keep-alive-duration: 5

#SF
sf-api:
  sf_api_url: https://api15.sapsf.cn/odata/v2/
  username: ODATAADMIN
  company: wuhanrongc
  password: 123456qwerty
  #正式
  synced: 520
  unsync: 521

#SF
onb-api:
  onb_api_url: https://onboarding15.sapsf.cn/ONBPREM/odata/v2
  username: ODATAADMIN
  password: 12345qwert


#MD5config
md5:
  secret: whrhkj

#SSO
custom-sso:
  #SF
  sf_enabled: true
  sf_base_url: https://hrmtest.whrhkj.com
  sf_token: WHRHKJ
  sf_secret_key: rh12345
  sf_company: wuhanrongc
  #COHO 劳勤-考勤
  coho_enabled: false
  coho_base_url: http://a6.coho.net.cn:82/WebForms/SSO/WtsLoginSSO
  coho_cust_code: RenHeJY
  coho_sys_name: OA
  coho_bus_code: Home
  #UAT 易路-薪酬
  uat_enabled: false
  uat_base_url: https://renheuat.peoplus.cn/renhe/login
  #OA 泛微-OA
  oa_enabled: true
  oa_base_url: http://oa.whrhkj.com:8099/com/rhkj/OALogin.jsp
  oa_secret: renhe@oa
  #CRM 神州云动-CRM
  crm_enabled: true
  crm_base_url: https://cloudcrm.whrhkj.com/customize/page/62234016b/rhsslogin.jsp?name=rhsslogin
  #HR MOKA-招聘
  hr_enabled: true
  hr_base_url: https://app.mokahr.com/login_by/sf/whrhkj
  #任务目标管理
  assess_enabled: true
  assess_base_url: http://assesspre.whrhkj.com
  #文件共享管理
  nas_enabled: true
  nas_base_url_sh: http://nas.whrhkj.com:5000
  nas_base_url_wh: http://rhnas.whrhkj.com:5000
  #SF-外挂页面
  sf_web_enabled: true
  sf_web_base_url: http://fsweb.whrhkj.com/sf_login
  #企业邮箱
  mail_enabled: true
  mail_base_url: http://mail.whrhkj.com/mail/
  mail_api_url: https://www.cndnsapi.com/email/
  mail_key: a9509a46742885ee51dcd97994c7fe40
  mail_token: d29613a48c95a1fc1c09c9230e24bef7
  #云课堂
  class_enabled: true
  class_base_url_sh: https://rhkj.yunxuetang.cn/login.htm
  #eoms管理平台
  eoms_enabled: true
  eoms_base_url: https://eomstest.whrhkj.com


console-admin:
  username: admin
  password: 54cc820ce6325f68f3a60a7f68039ca8ec2d7a59f885c4c43a44247168e3c27bbb0214b11c0d413c

cloudcc:
  host: "http://cloudcrm.whrhkj.com"
  userName: "interface@whrh.com"
  passWord: "46dc3220b03ec4c80c53451e1ad88134"
  isMD5: "true"
hrm:
  host: https://hrm-apitest.whrhkj.com
'''
text2='''
spring:
  mail:
    host: smtp.whrhkj.com
    username: mainadmin@whrhkj.com
    password: 'mainadmin@2019'
    properties.mail.smtp.auth: true
    properties.mail.smtp.port: 465
    properties.mail.display.sendmail: 重置密码
    properties.mail.display.sendname: 仁和会计企业管理平台
    properties.mail.smtp.starttls.enable: true
    properties.mail.smtp.starttls.required: true
    properties.mail.smtp.ssl.enable: true
    default-encoding: utf-8
    from: mainadmin@whrhkj.com
  datasource:
    url: jdbc:mysql://172.16.1.122:3669/rh-cas-pro?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&useSSL=false
    username: root
    password: redhat2019@
    type: com.alibaba.druid.pool.DruidDataSource
    druid:
      initial-size: 5
      min-idle: 5
      max-active: 20
      max-wait: 60000
      test-while-idle: true
      time-between-eviction-runs-millis: 60000
      min-evictable-idle-time-millis: 30000
      validation-query: select 'x'
      test-on-borrow: false
      test-on-return: false
      max-pool-prepared-statement-per-connection-size: 20
      #      filters: stat,wall
      # 状态监控
      filter:
        stat:
          enabled: true
          db-type: mysql
          log-slow-sql: true
          slow-sql-millis: 2000
      connect-properties: druid.stat.mergeSql=true;druid.stat.slowSqlMillis=5000
      use-global-data-source-stat: true
      # 监控过滤器
      web-stat-filter:
        enabled: true
        exclusions:
          - "*.js"
          - "*.gif"
          - "*.jpg"
          - "*.png"
          - "*.css"
          - "*.ico"
          - "/druid/*"
      # druid 监控页面
      stat-view-servlet:
        enabled: true
        url-pattern: /druid/*
        reset-enable: false
        login-username: admin
        login-password: admin
      aop-patterns: com.whrhkj.casspringservice.service.*
  redis:
    database: 10
    host: 172.16.8.175
    port: 6379
    password: UZ8CBGjifqdM5m0sInQ2
    timeout: 10000ms
    lettuce:
      pool:
        max-active: 16
        max-idle: 8
        max-wait: 1000ms
        min-idle: 0

server:
  port: 10077
  servlet:
    context-path: /cas

###OKHTTP
ok-http:
  connect-timeout: 30
  read-timeout: 30
  write-timeout: 30
  max-idle-connections: 200
  keep-alive-duration: 5

#SF
sf-api:
  sf_api_url: https://api15.sapsf.cn/odata/v2/
  username: ODATAADMIN
  company: wuhanrongc
  password: 123456qwerty
  #正式
  synced: 520
  unsync: 521

#SF
onb-api:
  onb_api_url: https://onboarding15.sapsf.cn/ONBPREM/odata/v2
  username: ODATAADMIN
  password: 12345qwert


#MD5config
md5:
  secret: whrhkj

#SSO
custom-sso:
  #SF
  sf_enabled: true
  sf_base_url: https://hrmtest.whrhkj.com
  sf_token: WHRHKJ
  sf_secret_key: rh12345
  sf_company: wuhanrongc
  #COHO 劳勤-考勤
  coho_enabled: false
  coho_base_url: http://a6.coho.net.cn:82/WebForms/SSO/WtsLoginSSO.aspx
  coho_cust_code: RenHeJY
  coho_sys_name: OA
  coho_bus_code: Home
  #UAT 易路-薪酬
  uat_enabled: false
  uat_base_url: https://renheuat.peoplus.cn/renhe/login
  #OA 泛微-OA
  oa_enabled: true
  oa_base_url: http://oa.whrhkj.com:8099/com/rhkj/OALogin.jsp
  oa_secret: renhe@oa
  #CRM 神州云动-CRM
  crm_enabled: true
  crm_base_url: https://cloudcrm.whrhkj.com/customize/page/62234016b/rhsslogin.jsp?name=rhsslogi
  #HR MOKA-招聘
  hr_enabled: true
  hr_base_url: https://app.mokahr.com/login_by/sf/whrhkj
  #任务目标管理
  assess_enabled: true
  assess_base_url: http://assesspre.whrhkj.com
  #文件共享管理
  nas_enabled: true
  nas_base_url_sh: http://nas.whrhkj.com:5000
  nas_base_url_wh: http://rhnas.whrhkj.com:5000
  #SF-外挂页面
  sf_web_enabled: true
  sf_web_base_url: http://fsweb.whrhkj.com/sf_login
  #企业邮箱
  mail_enabled: true
  mail_base_url: http://mail.whrhkj.com/mail/
  mail_api_url: https://www.cndnsapi.com/email/
  mail_key: a9509a46742885ee51dcd97994c7fe40
  mail_token: d29613a48c95a1fc1c09c9230e24bef7
  #云课堂
  class_enabled: true
  class_base_url_sh: https://rhkj.yunxuetang.cn/login.htm
  #eoms管理平台
  eoms_enabled: true
  eoms_base_url: https://eomstest.whrhkj.com


console-admin:
  username: admin
  password: 54cc820ce6325f68f3a60a7f68039ca8ec2d7a59f885c4c43a44247168e3c27bbb0214b11c0d413c

cloudcc:
  host: "http://cloudcrm.whrhkj.com"
  userName: "interface@whrh.com"
  passWord: "46dc3220b03ec4c80c53451e1ad88134"
  isMD5: "true"
hrm:
  host: https://hrm-apitest.whrhkj.com
'''

# 原始 Differ 文本行级 的比较。
# text1 = text1.splitlines()
# text2 = text2.splitlines()
# d = difflib.Differ()
# res = d.compare(text1, text2)
#
# print('\n'.join(list(res)))



# --------html对比方法----------

# d = difflib.HtmlDiff()
# q = d.make_file(text1, text2)
# print(q)
# old_str = 'charset=ISO-8859-1'
# new_str = 'charset=UTF-8'
# with open('diff.html','w') as f :
#     f.write(q.replace(old_str,new_str))



















# -------例子： 封装类：传入两个文件，return 一个 diff.html IO 及异步 IO及协程

import sys
import difflib
import os


class DiffFile():
    def __init__(self, first,second,is_file=True):
        """
        传入两个文件，比较这两个文件、字符串的差异，最后生成差异文件diff.html
        :param firstfile:
        :param secondfile:
        :return  diff.html
        """
        self.first = first
        self.second = second
        self.is_file=is_file
        self.old_str = 'charset=ISO-8859-1'
        self.new_str = 'charset=UTF-8'


        self.d = difflib.HtmlDiff()

    def readfile(self,file):
        try:
            with open(file,'r')as f:
                line=f.read().splitlines()
            return line
        except IOError as error:
            print('读取文件错误：' + str(error))
            sys.exit()

    def diff(self):
        if self.is_file:
            tfile1_lines = self.readfile(self.first)
            tfile2_lines = self.readfile(self.second)
        else:
            tfile1_lines = self.first.splitlines()
            tfile2_lines = self.second.splitlines()

        #为了生成html能识别中文，可用下面代码 #修改diff.html的编码，将ISO-8859-1改为UTF-8
        q = self.d.make_file(tfile1_lines, tfile2_lines)
        with open('../基本模块库/文件处理和目录访问/diff.html', 'w') as f_new:
            f_new.write(q.replace(self.old_str, self.new_str))

if __name__ == '__main__':
    d=DiffFile(text1,text2,False)
    d.diff()