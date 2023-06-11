#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/16 18:47
# @Project  : pycharmlearningproject
# @File     : check-HK-ssr-ip-alive.py

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/4/23 15:48
# @Project  : pycharmlearningproject
# @File     : check_ip_and_port_alive.py


import telnetlib
import sendemail
import time
import sys
import json
import time
import uuid

import urllib3
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkecs.v2 import *
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion
# 导入指定云服务的库 huaweicloudsdk{service}
from huaweicloudsdkeip.v2 import *
from huaweicloudsdkeip.v2.region.eip_region import EipRegion

urllib3.disable_warnings()



failure=0

# 查询服务器的既有的弹性ip地址
def query_ecs_ip(ecs):
    ecs_client = EcsClient.new_builder() \
        .with_credentials(credentials) \
        .with_http_config(config) \
        .with_region(EcsRegion.value_of("ap-southeast-1")) \
        .build()
    try:
        request = ShowServerRequest()
        request.server_id = ecs['ecs_id']
        response = ecs_client.show_server(request)
        address = response.server.addresses
        for add in address:
            for ips in address[add]:
                ips_dict = json.loads(str(ips))
                port_id = ips_dict['OS-EXT-IPS:port_id']
                ip = ips_dict['addr']
                if ip.startswith("192") or ip.startswith("10") or ip.startswith("172"):
                    pass
                else:
                    ecs["ip"] = ip
                    ecs["port_id"] = port_id
        print("查询服务器信息成功 %s" % (ecs))
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

    time.sleep(3)

def emailsend(info):
    server = sendemail.SendMail(['lisonfan@lexin.com'], 'AWS prod服务器端口检测异常')
    # server.add_text()
    server.add_text(info)
    server.send()


def telnet(host,port):
    global failure
    try:
        telnetlib.Telnet(host=host, port=port, timeout=5)
        print('端口正常')
    except:
        # emailsend('服务器：%s  端口: %s  检测异常' %(host,port))
         failure+=1

def detect_port(ips):
    for host in ips:
        for port in [22,]:
            telnet(host,port)
            time.sleep(3)

if __name__ == '__main__':
    # 华为云主账号的认证信息
    AK = "95ZVLTICGRGD7SWOBO2S"
    SK = "3Y17sD9VZUoABpgL1vtoZGhjpQmotUe9e6BtEP9F"

    # 认证信息
    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    config.timeout = (60, 120)
    config.max_retries = 10
    credentials = BasicCredentials(AK, SK)

    ecs_ip=[]

    old_ecc_info = {
        "ssr_01": {
            "alias": "ssr_01",
            "ecs_id": "dcf78762-b133-416f-853a-208593a4502d",
            "port_id": '',
            "ip": '',
            "ip_id": '',
            "new_ip": '',
            "new_ip_id": '',
        },
        "ssr_02": {
            "alias": "ssr_02",
            "ecs_id": "deeabc2d-8837-4cf5-bc9f-0caccbf09cb1",
            "port_id": None,
            "ip": None,
            "ip_id": None,
            "new_ip": None,
            "new_ip_id": None,
        },
        "ssr_03": {
            "alias": "ssr_03",
            "ecs_id": "4bbe20c7-baf3-43b5-8878-ac0017735b86",
            "port_id": None,
            "ip": None,
            "ip_id": None,
            "new_ip": None,
            "new_ip_id": None,
        },
    }

    for ecs in old_ecc_info:
        query_ecs_ip(old_ecc_info[ecs])

    for ecs in old_ecc_info:
        ecs_ip.append(old_ecc_info[ecs]['ip'])


    detect_port(ecs_ip)

    if failure ==3:
        emailsend('hw HK SSR 3台机器全部ping不通。')
