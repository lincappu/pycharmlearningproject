#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/4/26 16:27
# @Project  : pycharmlearningproject
# @File     : faker-模拟数据.py
'''
流行的Python虚拟数据生成工具有Mimesis（https://github.com/lkgeimfari/mimesis）和Faker，后者同时支持Python2和Python3，而且文档
中包含丰富的示例，所以这里将选用Faker。


语系：
简体中文：zh_CN
繁体中文：zh_TW
美国英文：en_US
英国英文：en_GB
德文：de_DE
日文：ja_JP
韩文：ko_KR
法文：fr_FR


faker包含生成20多种生成的数据，



地址相关
        fake.address()            # 地址
        # '江西省广州县大兴苏街t座 231839'
        fake.building_number()    # 楼名
        # 'U座'
        fake.city()               # 完整城市名
        # '广州市'
        fake.city_name()          # 城市名字(不带市县)
        # '广州'
        fake.city_suffix()        # 城市后缀名
        # '市'
        fake.country()            # 国家名称
        # '厄立特里亚'
        fake.country_code(representation="alpha-2")
        # 'BZ'                    # 国家编号
        fake.district()           # 地区
        # '沙湾'
        fake.postcode()           # 邮编
        # '332991'
        fake.province()           # 省
        # '河北省'
        fake.street_address()     # 街道地址
        # '武汉街D座'
        fake.street_name()        # 街道名称
        # '广州路'
        fake.street_suffix()      # 街道后缀名
        # '路'
汽车相关
    fake.license_plate()      # 牌照
    # 'ZCO 000'
银行相关
        fake.bank_country()          # 银行所属国家
        # 'GB'
        fake.bban()                  # 基本银行账号
        # 'TPET9323218579379'
        fake.iban()                  # 国际银行代码
        # 'GB82IRVM1531009974701'
条形码相关
        fake.ean(length=13)    # EAN条形码
        # '5456457843465'
        fake.ean13()           # EAN13条形码
        # '2689789887590'
        fake.ean8()            # EAN8条形码
        # '52227936'
颜色相关
        fake.color_name()        # 颜色名称
        # 'Orange'
        fake.hex_color()         # 颜色十六进制值
        # '#a5cb7c'
        fake.rgb_color()         # 颜色RGB值
        # '15,245,42'
        fake.rgb_css_color()     # CSS颜色值
        # 'rgb(15,70,13)'
        fake.safe_color_name()   # 安全色
        # 'aqua'
        fake.safe_hex_color()    # 安全色十六进制值
        # '#881100'
公司相关
        fake.bs()                 # 商业用词
        # 'synthesize strategic vortals'
        fake.catch_phrase()       # 妙句(口号)
        # 'Robust even-keeled service-desk'
        fake.company()            # 公司名称
        # '富罳科技有限公司'
        fake.company_prefix()     # 公司名称前缀
        # '商软冠联'
        fake.company_suffix()     # 公司名称后缀
        # '网络有限公司'
信用卡相关
        fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")    # 过期年月
        # '11/20'
        fake.credit_card_full(card_type=None)            # 完整信用卡信息
        # 'VISA 16 digit\n秀珍 卢\n4653084445257690 11/19\nCVC: 935\n'
        fake.credit_card_number(card_type=None)          # 信用卡卡号
        # '4339481813664365360'
        fake.credit_card_provider(card_type=None)        # 信用卡提供商
        # 'VISA 19 digit'
        fake.credit_card_security_code(card_type=None)   # 信用卡安全码
        # '597'
货币相关
        fake.cryptocurrency()           # 加密货币代码+名称
        # ('TRX', 'TRON')
        fake.cryptocurrency_code()      # 加密货币代码
        # 'MZC'
        fake.cryptocurrency_name()      # 加密货币名称
        # 'Ripple'
        fake.currency()                 # 货币代码+名称
        # ('GNF', 'Guinean franc')
        fake.currency_code()            # 货币代码
        # 'SOS'
        fake.currency_name()            # 货币名称
        # 'Lebanese pound'
时间相关
        fake.am_pm()        # AM或PM
        # 'PM'
        fake.century()      # 世纪
        # 'XII'
        fake.date(pattern="%Y-%m-%d", end_datetime=None)            # 日期字符串(可设置格式和最大日期)
        # '1998-05-13'
        fake.date_between(start_date="-30y", end_date="today")      # 日期(可设置限定范围)
        # datetime.date(2014, 8, 17)
        fake.date_between_dates(date_start=None, date_end=None)     # 同上
        # datetime.date(2019, 10, 14)
        fake.date_object(end_datetime=None)                         # 日期(可设置最大日期)
        # datetime.date(1981, 12, 20)
        fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)    # 出生日期
        # datetime.date(1931, 12, 8)
        fake.date_this_century(before_today=True, after_today=False)       # 本世纪日期
        # datetime.date(2003, 5, 4)
        fake.date_this_decade(before_today=True, after_today=False)        # 本年代中的日期
        # datetime.date(2014, 1, 29)
        fake.date_this_month(before_today=True, after_today=False)         # 本月中的日期
        # datetime.date(2019, 10, 10)
        fake.date_this_year(before_today=True, after_today=False)          # 本年中的日期
        # datetime.date(2019, 3, 6)
        fake.date_time(tzinfo=None, end_datetime=None)                     # 日期和时间
        # datetime.datetime(1990, 8, 11, 22, 25)
        fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None)    # 日期和时间(从001年1月1日到现在)
        # datetime.datetime(244, 12, 17, 9, 59, 56)
        fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)    # 日期时间(可设置限定范围)
        # datetime.datetime(1995, 4, 19, 17, 23, 51)
        fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)    # 同上
        # datetime.datetime(2019, 10, 14, 14, 15, 36)
        fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)     # 本世纪中的日期和时间
        # datetime.datetime(2009, 8, 26, 18, 27, 9)
        fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)      # 本年代中的日期和时间
        # datetime.datetime(2019, 2, 24, 22, 18, 44)
        fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)       # 本月中的日期和时间
        # datetime.datetime(2019, 10, 3, 9, 20, 44)
        fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)        # 本年中的日期和时间
        # datetime.datetime(2019, 2, 10, 7, 3, 18)
        fake.day_of_month()   # 几号
        # '23'
        fake.day_of_week()    # 星期几
        # 'Tuesday'
        fake.future_date(end_date="+30d", tzinfo=None)        # 未来日期
        # datetime.date(2019, 10, 28)
        fake.future_datetime(end_date="+30d", tzinfo=None)    # 未来日期和时间
        # datetime.datetime(2019, 10, 28, 21, 4, 35)
        fake.iso8601(tzinfo=None, end_datetime=None)          # iso8601格式日期和时间
        # '1995-04-10T00:45:01'
        fake.month()                                          # 第几月
        # '07'
        fake.month_name()                                     # 月份名称
        # 'December'
        fake.past_date(start_date="-30d", tzinfo=None)        # 过去日期
        # datetime.date(2019, 10, 3)
        fake.past_datetime(start_date="-30d", tzinfo=None)    # 过去日期和时间
        # datetime.datetime(2019, 9, 30, 20, 25, 43)
        fake.time(pattern="%H:%M:%S", end_datetime=None)      # 时间(可设置格式和最大日期时间)
        # '14:26:44'
        fake.time_delta(end_datetime=None)                    # 时间间隔
        # datetime.timedelta(0)
        fake.time_object(end_datetime=None)                   # 时间(可设置最大日期时间)
        # datetime.time(4, 41, 39)
        fake.time_series(start_date="-30d", end_date="now", precision=None, distrib=None, tzinfo=None)
        # <generator object Provider.time_series at 0x7fadf51e0930>
        fake.timezone()    # 时区
        # 'Asia/Baku'
        fake.unix_time(end_datetime=None, start_datetime=None)    # UNIX时间戳
        # 393980728
        fake.year()        # 某年
        # '2016'
文件相关
        fake.file_extension(category=None)                # 文件扩展名
        # 'avi'
        fake.file_name(category=None, extension=None)     # 文件名
        # '专业.pptx'
        faker.file_path(depth=1, category=None, extension=None)    # 文件路径
        # '/的话/以上.ods'
        fake.mime_type(category=None)                     # MIME类型
        # 'application/xop+xml'
        fake.unix_device(prefix=None)                     # UNIX设备
        # '/dev/xvdq'
        fake.unix_partition(prefix=None)                  # UNIX分区
        # '/dev/xvdc6'
坐标相关
        fake.coordinate(center=None, radius=0.001)        # 坐标
        # Decimal('147.543284')
        fake.latitude()                                   # 纬度
        # Decimal('66.519139')
        fake.latlng()                                     # 经纬度
        # (Decimal('55.3370965'), Decimal('-15.427896'))
        fake.local_latlng(country_code="US", coords_only=False)    # 返回某个国家某地的经纬度
        # ('25.67927', '-80.31727', 'Kendall', 'US', 'America/New_York')
        fake.location_on_land(coords_only=False)                   # 返回地球上某个位置的经纬度
        # ('42.50729', '1.53414', 'les Escaldes', 'AD', 'Europe/Andorra')
        fake.longitude()                                   # 经度
        # Decimal('70.815233')
网络相关
            fake.ascii_company_email(*args, **kwargs)        # 企业邮箱(ascii编码)
            # 'qiuyan@xiulan.cn'
            fake.ascii_email(*args, **kwargs)                # 企业邮箱+免费邮箱(ascii编码)
            # 'lei59@78.net'
            fake.ascii_free_email(*args, **kwargs)           # 免费邮箱(ascii编码)
            # 'pcheng@gmail.com'
            fake.ascii_safe_email(*args, **kwargs)           # 安全邮箱(ascii编码)
            # 'fangyan@example.org'
            fake.company_email(*args, **kwargs)              # 企业邮箱
            # 'scao@pingjing.net'
            fake.domain_name(levels=1)                       # 域名
            # 'dy.cn'
            fake.domain_word(*args, **kwargs)                # 二级域名
            # 'gangxiuying'
            fake.email(*args, **kwargs)                      # 企业邮箱+免费邮箱
            # 'na13@ding.cn'
            fake.free_email(*args, **kwargs)                 # 免费邮箱
            # 'fang48@hotmail.com'
            fake.free_email_domain(*args, **kwargs)          # 免费邮箱域名
            # 'yahoo.com'
            fake.hostname(*args, **kwargs)                   # 主机名
            # 'lt-70.53.cn'
            fake.image_url(width=None, height=None)          # 图片URL
            # 'https://placekitten.com/752/243'
            fake.ipv4(network=False, address_class=None, private=None)    # ipv4
            # '160.152.149.78'
            fake.ipv4_network_class()                                     # ipv4网络等级
            # 'b'
            fake.ipv4_private(network=False, address_class=None)          # 私有ipv4
            # '10.99.124.57'
            fake.ipv4_public(network=False, address_class=None)           # 公共ipv4
            # '169.120.29.235'
            fake.ipv6(network=False)                                      # ipv6
            # 'f392:573f:d60f:9aed:2a4c:36d7:fe5b:7034'
            fake.mac_address()                            # MAC地址
            # '62:67:79:8c:c2:40'
            fake.safe_email(*args, **kwargs)              # 安全邮箱
            # 'jing58@example.org'
            fake.slug(*args, **kwargs)                    # URL中的slug
            # ''
            fake.tld()                                    # 顶级域名
            # 'cn'
            fake.uri()                                    # URI
            # 'http://yi.com/list/main/explore/register.php'
            fake.uri_extension()                          # URI扩展
            # '.php'
            fake.uri_page()                               # URI页
            # 'terms'
            fake.uri_path(deep=None)                      # URI路径
            # 'blog/tags/blog'
            fake.url(schemes=None)                        # URL
            # 'http://liutao.cn/'
            fake.user_name(*args, **kwargs)               # 用户名
            # 'xiulan80'
图书相关
        fake.isbn10(separator="-")        # ISBN-10图书编号
        # '0-588-73943-X'
        fake.isbn13(separator="-")        # ISBN-13图书编号
        # '978-1-116-51399-8'
职位相关
        fake.job()        # 职位
        # '法务助理'
文本相关
            fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)    # 单个段落
            # '最新事情生产.方面解决名称责任而且.类型其实内容发生电脑.音乐具有今年是一.'
            fake.paragraphs(nb=3, ext_word_list=None)                                         # 多个段落
            # ['使用评论管理.没有广告工作评论是否.', '帖子而且专业.这些比较完全发现准备设计工具.', '完成详细发生空间汽车.新闻电影您的游戏这种操作网站知道.']
            fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)    # 单个句子
            # '直接这样点击单位对于时候.'
            fake.sentences(nb=3, ext_word_list=None)                                 # 多个句子
            # ['电话国际项目管理.', '软件之后提高一样次数电影规定.', '东西会员发展什么不断经济.']
            fake.text(max_nb_chars=200, ext_word_list=None)                          # 单个文本
            # ('资源信息得到因此开发资源资料.\n'
            #  '国家这样等级需要用户如此.电话非常一切游戏所以学校类型.不要正在如果来源认为投资在线.\n'
            #  '这些更新密码其中起来实现有些.以上事情重要通过.\n'
            #  '但是就是介绍最大深圳简介设计.历史这种可以出现中心社区.\n'
            #  '政府当然包括简介全国内容生活.有些地址以上.回复这些来自搜索现在不断经营不断.\n'
            #  '操作为什孩子报告东西拥有如此.相关特别业务日本这种.合作问题准备比较谢谢.')
            fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)             # 多个文本
            # [   '地址控制无法正在必须中心积分一些.支持制作安全.\n'
            #     '比较最新最大她的功能能够是一.主题选择当前显示.\n'
            #     '的话社会现在地区阅读继续所有.美国数据正在深圳不能.\n'
            #     '能够查看其中生活商品.谢谢认为之后以及以下之后这里.\n'
            #     '活动支持人民这么今年.要求包括生活运行技术社会.\n'
            #     '当前更多游戏.下载一点开发论坛法律为了美国.\n'
            #     '如何更新个人谢谢作为还有论坛.销售销售法律学生这么责任一些.',
            #     '日本最大方法活动主题到了结果.教育还有孩子觉得简介出现国际.东西国家图片威望品牌.\n'
            #     '那些会员现在准备可能.威望部分文件主题东西业务一切之间.所以必须当前方法.\n'
            #     '等级大小重要可能下载孩子.来源感觉业务文件以后深圳学校.网络什么新闻都是安全.\n'
            #     '资料重要成功谢谢时候音乐安全相关.电脑系列日期.工具使用搜索来源首页.\n'
            #     '直接企业影响大小什么.相关品牌选择她的规定来源推荐.',
            #     '中文文化数据内容系统.他们这些之间深圳.\n'
            #     '联系城市出现部分都是政府生活.社会同时人民市场现在决定需要.其他政府简介深圳教育加入对于.\n'
            #     '运行是一语言安全通过大小学生.商品然后信息由于虽然.\n'
            #     '因为关于选择希望行业具有深圳.出现价格那么下载提高知道人员.设备直接显示事情帖子正在两个关于.\n'
            #     '系列公司大家.论坛所以完全文章标准.活动中国工具电脑.\n'
            #     '主题作者不能.进行国家系统地区增加.经验质量价格我的.']
            fake.word(ext_word_list=None)                                            # 单个词语
            # '新闻'
            fake.words(nb=3, ext_word_list=None, unique=False)                       # 多个词语
            # ['选择', '历史', '规定']
编码相关
        fake.binary(length=1048576)                # 二进制
        # (b'\xbf\xce\x01Y:\xf7\xf4\xe0G]\x94*Rb\x9f\x85\xb6\xcd\x83\x15\t\xbc\x16\x8d'
        #  b'\xcb\n\x90\x10S\x1e85\x91\xae\x06\xbdq.\xf6c\x1f\xfd\x94=\\\xf9_\xc2'
        #  b't\xe0{\x15\xd9\x8fW7\xe5[\x0b\x84\xd2\x94\xf4\xd91\xd2\x91\x01\xb5\xeej\x84'
        #  b'*\x81\x96\xa7\xa9\xda\x1f\xee\x9a\xb0\x1d\xef\xad\x92\x1c\x0f\xa0U6\xaf'
        #  b'x5\x9f\x93\\b \xf7kq\xfe\x97(\xe0Q\x89*\xbb\x8b\x9a\x14\xd2\xfe\x07'
        #  b'\xfe\xcfYy\x16\x12\xef\xe3\xd9%\x95\\\x80O\xec\x9f\xf7\x88\xfal'
        #  b'\x11\x93\x94\xb1\xd9\xf6b\xf0\x7f\xa2\x95\x93[\x98\xf3\xe0$\xdd\xe0D'
        #  b'\xde\x8c\xe3\xe0\xc0f\xab\x1c\xf6\xdf]\xbe8U\x11\xc7\xce\xf6f\xc9'
        #  b'1\xa6\xda\x85\xe6.\xda\xd1_\x8a\xbe\x05\xbf\xf4*x [\xb9\xc3\xbb\x99\xa1\xbe'
        #  b'GT\xb75\x96\x8a\x9a:`o\x1bm\xe9KzT\x0c\xdc\xb1\xe7ssiN\xcb2\x8eY'
        #  b'\xd1\xb4\x8c+\xe9\xc1Ph\x0fD\x0f\xd5}\n/K$\x85J\xaf\x1d\xb2\xd0R\xa7n0l'
        #  b'\xafQ\x91\x95\xac]a\xe1\x8f\x1f\x9e`e\xd2\x1f\xaa\xeb\xf3[}(\xd60\x01'
        #  b'Y\r\xe2XCW\xba\xa3\xad\xe4OP\x891=\xff\xae\xb9\x9d\xa2!\xfa2\r\x81\xfat\xfb'
        #  b'3t%\xd5\x11B\x94Os\x8d\xc5\xae%\xa6\x93}[p\x02\xd7\xba\xa4\xf0?R\xbb\xf6\xb1'
        #  b'h\x12J\x05\xce\xf9\xcd\xc6\xa7\xed\x80\x9e\x9e\xf8q]\xab\x9a\xd7\xd6'
        #  b'\xad\xecK\x1d=\xb0?\xb2\x83\t<\xb2ZGl\x9f\x8dmI\x1d\xf1jh\xd3s\x9d\xd6\xf9'
        #  b'\x8e\xbfs\xa9_\xe0\xaf\x86O\xde|\x17\xb5\x8b\xe4:Z\xa1\x01f\xc9l[Z'
        #  b'\xb4\x7fS\x0f7\x9c\x9d\xdd\xd3PY\x86\xf4\xec\xcb\x87\x05\xafU-\xaebY~'
        #  b"\x9f\xec\xf6\x9c\x84\x99'S\xd4\t.\xd0x\xbb\x01<&\xdd\xfc6M\xa9|R"
        #  b'\xec\xf9b\xcdz\x9a\x97p\xb5\xb6\x13\xd9\xab\x91C\xe4\x95\xc9\x18\xaeAi\\N'
        #  b"#\x99\t+Z\xd2\xf1\x89\xa0L\x04\xef\xaf<\xc4\xfbO\xcd\x83\xd4\x17'C\x10"
        #  b'\x0b\xd6\xb5Cv\x98}E\xc9;\xbf\x05\xab\xc7 W\xa8\xbcmX\x06\x865\xbe\\f\xedc'
        #  b'\xacb\xc8\x84\xc0KI\xd5\xea\x888\x93^\xfcE\xee,^(\x97g\xd17\xcd8\xabU\x95'
        #  b'\x17~]\x08\x11\xa4\xbf\xed\xf3\xabm\x15l\xde\xf5\x06c\xe1\xad+'
        #  b'\xed\xd1\xa5\xda\x15\xbax\xac}\x8e\xd7\x8831\x04\xb3\xae\xc7\xb4\x04'
        #  b'y\xda!\xeb\x1e\xcd\n+\x94#4\xe51\xc8\xe9t\n.:\xfd\xcfc\x1a\xcf\x99VY\x11'
        #  b'Y\x1bF\xe9\x9e\xebK\x86WD\x80\x12\xf1\x11z\xf6\xe3vV4\xbcB\n^k(\x1aw'
        #  b'<\xfd\x95z\t\xf7\xaa_F%n\xc4\xeb\x94\xcd\x80\xffh\xbe{^\x04\xe3\xe7'
        #  b'\xab\xa3\xd9\x037\x86\xde~J\x15th\x98_\xda\xe25\xeaO\xc8\x15\xae\xd7\xa9'
        #  b'\x80\x9as\xef<FU\xb2\x10\x7fN\x05\x8dd_\xef\x0bQO-\x9diW\xdc\xcdV\xbe*'
        #  b'\x13\xa7$\x08\xe4\xb8\x96bd\xcf\xe7\xd6h\xe9.{Z:S\xef\xc4\x14R\x91'
        #  b"\xce\xd3\xcd\xe3\xbc\x9f!Y\x05A\xa00\x11\xca\xaa\xeb\xc4')\xb3\xdcF\x8e\xfa"
        #  b'\xbd\x9b:\xae\x1f\xbe<7]\x93E\xc2\x1b\x17\xc95x\x8f\x88|\xb8^\xea\x06'
        #  b'(\x9d\xc5\xeb\x8a|\x9f\x05\x83\xfe\xf5KsUy\xdc\xd1S\x96\xda\xc5q\xc4\xfd'
        #  b'\xeb\xc4"\x14Y\x1cU\x99\xe8\x11r\x04\x941\xa1\xac^c\xbbG\xc4\xd8\xb70'
        #  b'\xadX\x98\xad\xf8\xc1\x11\x10\xbc\x00\x80\x84\x05\x07b\x8c0\x93\xe6\xd8'
        #  b'\xe2I\xea\xecm+-\x8aY\xb8F\x0e\x19#zH{/\xcb\x88\xac\xa9\xfe\x84cH[_'
        #  b'0d\xc6\xc4\x0b\r\x9ef\n\xb3\x97d\xb4;\xf1\x014kv\xd9h\xad\x18/\xe6\xf1r\xa1'
        #  b'3\x9cz\xf7\x90\r\xaf\xed\x85\x07\x80\xbb\xc2\x82\xe4\xcc\x91\xc8\xdf\x9a'
        #  b'`St\xd8\x98\xbb\xac\xe9\x93\xe0*\xd7\x9b/)\x93\x08\xc1\x0cxhD\xd2\xf1'
        #  b'\xbe5\xe1\x1f:\x04\x07\xf1\xb4\xaeJ\xe2\xe0[\x9e\xa4\x9b\xed)\xbf\xc2}+\x88'
        #  b'\x08I^f\x82-\xa2o\xb2\xc3\x85\xc5;Z\x13B\xf76~\x9af\xf7\xa9\x1a\xa4\xd4\xb8b')
        fake.boolean(chance_of_getting_true=50)    # 布尔值
        # True
        fake.md5(raw_output=False)                 # Md5
        # '0712ca7a3be00aa01c823de37dc61230'
        fake.null_boolean()                        # NULL+布尔值
        # True
        fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)                           # 密码
        # '^7cSoHR1^r'
        fake.sha1(raw_output=False)                # SHA1
        # 'f89f039d9fc00860651d9a567ac27990ae609445'
        fake.sha256(raw_output=False)              # SHA256
        # '675a85aa0d29583200f75351e35b4af0335af835fc617382cbd9fece258b6520'
        fake.uuid4(cast_to=<class 'str'>)          # UUID4
        # '0d7be36a-febd-4f9f-bf1e-791c0ee1227b'
人物相关
            fake.first_name()            # 名字
            # '强'
            fake.first_name_female()     # 名字(女)
            # '桂荣'
            fake.first_name_male()       # 名字(男)
            # '志强'
            fake.first_romanized_name()  # 名字(罗马文)
            # 'Chao'
            fake.last_name()             # 姓
            # '宋'
            fake.last_name_female()      # 姓(女)
            # '陆'
            fake.last_name_male()        # 姓(男)
            # '曾'
            fake.last_romanized_name()   # 姓(罗马文)
            # 'Xie'
            fake.name()                  # 姓名
            # '王凯'
            fake.name_female()           # 姓名(女)
            # '戴丽丽'
            fake.name_male()             # 姓名(男)
            # '刘荣'
            fake.prefix()                # 称谓
            # ''
            fake.prefix_female()         # 称谓(女)
            # ''
            fake.prefix_male()           # 称谓(男)
            # ''
            fake.romanized_name()        # 称谓(罗马文)
            # 'Guiying Chang'
            fake.suffix()                # 姓名后缀(中文不适用)
            # ''
            fake.suffix_female()
            # ''
            fake.suffix_male()
            # ''
电话相关
        fake.msisdn()                # 完整手机号码(加了国家和国内区号)
        # '9067936325890'
        fake.phone_number()          # 手机号
        # '18520149907'
        fake.phonenumber_prefix()    # 区号
        # 145
档案相关
            fake.profile(fields=None, sex=None)        # 档案(完整)
            # {   'address': '河南省昆明市清河哈尔滨路H座 496152',
            #     'birthdate': datetime.date(2014, 11, 20),
            #     'blood_group': 'AB+',
            #     'company': '易动力信息有限公司',
            #     'current_location': (Decimal('77.504143'), Decimal('-167.365806')),
            #     'job': '培训策划',
            #     'mail': 'liangyang@yahoo.com',
            #     'name': '杨磊',
            #     'residence': '澳门特别行政区台北县西夏兴城街L座 803680',
            #     'sex': 'F',
            #     'ssn': '140722200004166520',
            #     'username': 'lei65',
            #     'website': [   'http://www.29.cn/',
            #                    'http://www.lei.cn/',
            #                    'http://lishao.net/',
            #                    'https://www.feng.net/']}
            fake.simple_profile(sex=None)               # 档案(简单)
            # {   'address': '广西壮族自治区南宁市花溪孙街c座 653694',
            #     'birthdate': datetime.date(1993, 12, 16),
            #     'mail': 'haomin@yahoo.com',
            #     'name': '任秀英',
            #     'sex': 'F',
            #     'username': 'iding'}
Python相关
            fake.pybool()    # Python布尔值
            # False
            fake.pydecimal(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)  # Python十进制数
            # Decimal('-837022273798.0')
            fake.pydict(nb_elements=10, variable_nb_elements=True, *value_types)    # Python字典
            # {   '一种': 6381,
            #     '可以': -9242847.69292,
            #     '地址': 9668,
            #     '拥有': 'jVBverSGAJvHsrcZPFDg',
            #     '控制': Decimal('-98521.0'),
            #     '本站': datetime.datetime(1983, 5, 30, 22, 51, 22),
            #     '来源': 'MRTmgbdlwNlqHiIDUVTN',
            #     '标题': 929,
            #     '注册': 'QvYtlygVIopYPasYHCQr',
            #     '解决': -7138575.3,
            #     '问题': 1115.0}
            fake.pyfloat(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)        # Python浮点数
            # 6.7442382094132
            fake.pyint(min_value=0, max_value=9999, step=1)    # Python整型值
            # 8326
            fake.pyiterable(nb_elements=10, variable_nb_elements=True, *value_types)    # Python可迭代对象
            # {'gang42@gmail.com', Decimal('-638462592926556.0'), 5383, 1608, 185608.962728, datetime.datetime(2013, 8, 7, 10, 44, 51), 'xvqHfWdLyTkaFoguvnqd', datetime.datetime(1999, 9, 10, 4, 41, 29), Decimal('4627589014.65023'), 'http://57.cn/category/', 'UZJwIrsLowvwVGAChwzB', Decimal('68.623476938'), 'mtUbDpTHnQAPVjXzknIM'}
            fake.pylist(nb_elements=10, variable_nb_elements=True, *value_types)    # Python列表
            # [   589,
            #     'https://www.yangbai.cn/main/',
            #     'http://fang.cn/faq/',
            #     'HvtSTwWqDtughQLYibOd',
            #     Decimal('-3541501.934427'),
            #     2758,
            #     datetime.datetime(2018, 2, 22, 9, 51, 8),
            #     5375,
            #     'UVXMfCqJyZwBkfgGhQiH',
            #     'HfxybvRTPwaFmuhwvKLT',
            #     Decimal('-21565647052012.8'),
            #     'wEqWsXKTputijSMWhCIb']
            fake.pyset(nb_elements=10, variable_nb_elements=True, *value_types)    # Python集合
            # {7105, 'sidMFYVhXjkNZnHHimJJ', 'yexiuying@kw.cn', 'GPxoyEYixUGAoRCiEmDe', datetime.datetime(2001, 6, 17, 12, 49, 57), 'vOsPAdmmCmkJxeBUpBJP', -75011.0}
            fake.pystr(min_chars=None, max_chars=20)    # Python字符串
            # 'NOlWELuogcxSfRjYauSV'
            fake.pystruct(count=10, *value_types)       # Python结构
            # (   [   'SQeHWPNdooccsfbZslee',
            #         'nDXibfaPXSpmIpxtDUWP',
            #         'DrZHepzMfNPRrxgcXwvR',
            #         988.956374402,
            #         7239,
            #         4885,
            #         datetime.datetime(1972, 6, 13, 14, 18, 11),
            #         -582284.9732,
            #         datetime.datetime(1997, 8, 23, 9, 19, 6),
            #         'http://www.hu.cn/homepage.php'],
            #     {   '一般': 'oqUQKBhqNylyofEditXs',
            #         '不要': 'qTlztJembuRZHFEzZnGO',
            #         '价格': -2100690667.387,
            #         '国内': datetime.datetime(1989, 9, 3, 11, 27, 11),
            #         '密码': 'aWaufuJAzfgeuhyXAwDL',
            #         '开发': 'aJvNisEMynJcAPhbNAHa',
            #         '方法': 'WVEqHUnnkpUbAnllUqKL',
            #         '汽车': 'bfQlaULiNfjgkrqQUCnL',
            #         '用户': 'WDYNlInLyCcIXMFgyLDS',
            #         '那个': 'qWivpUnOcTwGDhOXihOb'},
            #     {   '个人': {   1: 'http://www.ik.cn/categories/tags/search/homepage/',
            #                   2: [   'gBSKOBAYYlPwILaWgory',
            #                          'xoeueUWWgbvNHDxKYASD',
            #                          'nkcelmDSpqiQasuKvNZg'],
            #                   3: {   1: 2000,
            #                          2: 'SeDZKUpCxrCLlrDIlPxV',
            #                          3: [Decimal('7833105.737'), Decimal('-7.994')]}},
            #         '帖子': {   0: 'HXTKojcilYqgYmFUMjuk',
            #                   1: [6887, 3635, 'http://hezhu.com/list/main/terms.html'],
            #                   2: {   0: 'hkong@fujiang.cn',
            #                          1: 4676,
            #                          2: ['JYEFavcRqcsdpnSMwENU', 'vxu@gmail.com']}},
            #         '应该': {   7: 'EmzzdZrmUpIetxPktXAU',
            #                   8: [   Decimal('4786692875733.0'),
            #                          datetime.datetime(2016, 10, 11, 10, 38, 20),
            #                          'ghtelDQAsBeYDaokgbYg'],
            #                   9: {   7: 'yanding@yahoo.com',
            #                          8: 'dtjdazSyZCStWkVYwIvK',
            #                          9: ['TPTzKNGReDCJmrfTkKmd', 'TKQmVfrNRioICuqCrrDQ']}},
            #         '我的': {   3: 'http://17.cn/home/',
            #                   4: [   'https://www.guiyingsu.cn/category/',
            #                          'gweRIERFoojbKxRiiliG',
            #                          'dMjUNjDRCSpdrNAlHXRp'],
            #                   5: {   3: 'YeIsIoVHcIgAQWYZkQiR',
            #                          4: 'hGDzyNMVafuDMXSbbhzY',
            #                          5: [977, 'xCFBFdaPHNyFscSCqEWd']}},
            #         '或者': {   9: 'owgjdYQvTWZIZRewhkev',
            #                   10: ['nHusiXLRunAMvynwjJgu', 6500, 'cQRHfcdFJGUyPDlIocqG'],
            #                   11: {   9: 'sETogfbiwRIqFlrGXeiT',
            #                           10: 'tliang@kong.cn',
            #                           11: [   'https://chaohao.cn/register.html',
            #                                   'fang21@yahoo.com']}},
            #         '技术': {   4: 8843,
            #                   5: [-5660697068472.0, 7952, -52210308185.53],
            #                   6: {   4: 6477,
            #                          5: 8669,
            #                          6: ['sGueDRKWFAtTExnruySP', 'YZcIHHkbDRLUgeHhblCu']}},
            #         '深圳': {   5: 2532,
            #                   6: [   Decimal('66661967013036.0'),
            #                          'lei14@yahoo.com',
            #                          'https://www.fangyao.cn/categories/search.html'],
            #                   7: {   5: datetime.datetime(1988, 9, 11, 2, 30, 1),
            #                          6: 50.1,
            #                          7: [   'https://www.gang.cn/',
            #                                 'http://www.liao.cn/posts/app/main.html']}},
            #         '生产': {   2: 2187,
            #                   3: [   8629589.339,
            #                          'QvftOABFsahZurjYIPTr',
            #                          'GumqSZMuOSIfrUzjTzKO'],
            #                   4: {   2: 1982,
            #                          3: 'WatxfisQAelRTuwopoOA',
            #                          4: ['xiacheng@00.cn', 'flrVEiuWlEnJjbxCazQG']}},
            #         '起来': {   6: 'luming@yahoo.com',
            #                   7: [   'http://www.yu.cn/home.php',
            #                          'vvmhckwxQGnMCafhjXIA',
            #                          Decimal('-511928454.48')],
            #                   8: {   6: 'https://www.naguiying.cn/',
            #                          7: 279.928,
            #                          8: [5034, 'shaochao@17.cn']}},
            #         '那么': {   8: 'PNrBODNdjLnhalWpVMXk',
            #                   9: [   datetime.datetime(1973, 7, 4, 11, 42, 8),
            #                          'iye@gmail.com',
            #                          'iEPyTnfNhNhWWXbkStQC'],
            #                   10: {   8: Decimal('-227034846260.0'),
            #                           9: Decimal('616424892362.0'),
            #                           10: [   'AjpDMNozhUbedUuOZWdL',
            #                                   datetime.datetime(1972, 10, 27, 8, 36, 39)]}}})
            fake.pytuple(nb_elements=10, variable_nb_elements=True, *value_types)    # Python元组
            # (   Decimal('989085669.60574'),
            #     'yang44@hotmail.com',
            #     794,
            #     datetime.datetime(1989, 12, 11, 4, 10, 40),
            #     234,
            #     'TyEwXywfUShjlUVwtMAk',
            #     'NLUdMSRYoBHmGGPhbwor',
            #     -69.356824324)
身份证相关
        fake.ssn(min_age=18, max_age=90)    # 身份证
        # '410622198603154708'
用户代理相关
        fake.android_platform_token()        # 安卓
        # 'Android 5.0.1'
        fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899)    # Chrome
        # ('Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_9) AppleWebKit/534.0 (KHTML, '
        #  'like Gecko) Chrome/62.0.826.0 Safari/534.0')
        fake.firefox()                       # FireFox
        # ('Mozilla/5.0 (Windows NT 5.1; cs-CZ; rv:1.9.0.20) Gecko/2010-12-02 06:14:30 '
        #  'Firefox/3.6.5')
        faker.internet_explorer()             # Ie
        # 'Mozilla/5.0 (compatible; MSIE 7.0; Windows 95; Trident/3.0)'
        fake.ios_platform_token()            # ios
        # 'iPhone; CPU iPhone OS 5_1_1 like Mac OS X'
        fake.linux_platform_token()          # Linux
        # 'X11; Linux i686'
        fake.linux_processor()               # Linux处理器
        # 'x86_64'
        fake.mac_platform_token()            # Mac
        # 'Macintosh; U; PPC Mac OS X 10_11_2'
        fake.mac_processor()                 # Mac处理器
        # 'Intel'
        fake.opera()                         # Opera
        # 'Opera/8.32.(Windows 98; Win 9x 4.90; mr-IN) Presto/2.9.188 Version/10.00'
        fake.safari()                        # Safari
        # ('Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.43.6 (KHTML, like '
        #  'Gecko) Version/4.0.5 Safari/533.43.6')
        fake.user_agent()                    # 随机用户代理
        # 'Mozilla/5.0 (compatible; MSIE 9.0; Windows 95; Trident/3.0)'
        fake.windows_platform_token()        # Windows
        # 'Windows NT 6.2'
'''


# 也可以使用这方式来定义语系
# DEFAULT_LOCALE='en_US'

from faker import Faker
faker = Faker(locale='zh_CN')  # 语系
print(faker.name())
print(faker.address())
