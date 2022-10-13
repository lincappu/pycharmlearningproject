import configparser




'''
configparser过程：
1、生成实例configparser.ConfigParser()，然后读配置文件，
'''





obj=configparser.ConfigParser()
obj.read('my.cnf')


# print(obj.sections())
# print(obj.options('mysql'))
# print(obj.items('mysql'))



# print(obj.get('mysql','user')) #拿到的结果是字符串类型

# x=obj.get('mysqld','port')
# print(x,type(x))

#  获取特定类型的字段值，如果类型不符合会报错，
print(type(obj.getint('mysql','port')))
print(type(obj.getboolean('mysql','x')))
print(type(obj.getfloat('mysql','y')))


#判断是否存在
# import configparser
# obj=configparser.ConfigParser()
# obj.read('my.cnf')
#
# print(obj.has_section('mysql'))
# print(obj.has_option('alex','is_sbxxxxxxxxxxx'))





#了解：修改操作
# import configparser

# obj=configparser.ConfigParser()
# obj.read('my.cnf')

# obj.add_section('alex')
# obj.set('alex','password','123')
# obj.set('alex','is_sb','True')

# obj.remove_section('mysqld')
# obj.remove_option('mysql','user')
# obj.write(open('my.cnf','w'))






# import  configparser

# config=configparser.ConfigParser()
# config.read('my.cnf',encoding='utf-8')
#
# res=config.sections()
# print(res)

# option=config.options('mysql')
# print(option)
#
# item_list=config.items('mysql')
# print(item_list)
#
# config.remove_section('mysql')
#
# config.remove_option('alex','password')
#
# print(config.has_section('alex'))
# print(config.has_option('alex','password'))
#
# config.add_section('egon')
#
# config.set('egon','name','egon')
#
# config.write(open('a.ini','w'))


