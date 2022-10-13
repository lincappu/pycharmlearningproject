# !/user/bin/env python3
# -*-   coding:utf-8 -*_
# second job：
# 1.三级菜单
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

exit_tag = True
while exit_tag:
    for key in menu:
        print(key)
    choice = input('>: ').strip()
    if choice == 'quit':
        exit_tag = False
        continue
    if len(choice) == 0:
        continue

    if choice in menu:
        while exit_tag:
            first = menu[choice]
            for key2 in first:  # 第二层循环
                print(key2)
            choice2 = input('>>：').strip()
            if choice2 == 'bye':
                break
            if choice2 == 'quit':
                exit_tag = False
                continue
            if len(choice2) == 0:
                continue
            if choice2 in first:
                while exit_tag:
                    second = first[choice2]
                    for key3 in second:  # 第三层
                        print(key3)
                    choice3 = input('>>>: ').strip()
                    if choice3 == 'bye':
                        break
                    if choice3 == 'quit':
                        exit_tag = False
                        continue
                    if choice3 in second:
                        third = second[choice3]
                        for key4 in third:
                            print(key4)
                        choice4 = input('>>>>: ').strip()
                        if choice4 == 'bye':
                            break
                        if choice4 == 'quit':
                            exit_tag = False
                            continue
#
# 2.购物车程序：
# good = {
#     '1':{'apple': 100},
#     '2':{'tesla': 100},
#     '3':{'mac': 100},
#     '4':{'lenovo': 100},
#     '5':{'chicken': 100},
# }
# shoping_list = []
# exit_tag = True
# count = 0
# while exit_tag:
#     account = input('your acconut: ').strip('|')
#     password = input('your password: ').strip()
#     with open('login.txt', 'r') as file:
#         pair = file.read().split('|')
#         name, secert = pair
#         # print(name,secert)
#     if account not in pair:
#         print('用户名不存在')
#     if account == name and password == secert:
#         print('登陆成功')
#         salary = input('请输入你的工资： ').strip()
#         if salary == 'quit':
#             exit_tag = False
#             continue
#         if not salary.isdigit():
#             print('请重新输入（工资必须为数字)：')
#         else:
#             salary_balance = int(salary)
#             while exit_tag:
#                 for key in good:
#                     print(key,good[key])
#                 serial = input('请输入商品编号： ').strip()
#                 if serial == 'quit':
#                     exit_tag = False
#                     continue
#                 if serial in good:
#                     number = input('请输入购买的商品个数：').strip()
#                     if  number.isdigit():
#                         goods_name = list(good[serial])[0]
#                         goods_price = good[serial][goods_name]
#                         print('你选择购买的商品为：%s  单价为：%s  购买个数为： %s' %(goods_name,goods_price,number))
#                         shoping_list.append((goods_name,goods_price,number))
#                         goods_sum = int(goods_price)*int(number)
#                         salary_balance -= goods_sum
#                         if salary_balance < 0:
#                             print('你的账户余额不足，退出!')
#                             exit_tag = False
#                             continue
#                         else:
#                             continue
#                     else:
#                         print('商品个数必须为数字：')
#                 else:
#                     print('请输入正确的商品编号： ')
#             print('你的购物清单为%s \n' %(shoping_list))
#     else:
#         print('你输入的密码不对，请重新输入！')
#         count += 1
#     if count > 2:
#         print('你尝试的次数过多，请稍后再试！')
#         exit_tag =False
#         continue
