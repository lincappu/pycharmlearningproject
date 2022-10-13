import os
#
# res=os.system('tasklist')
# print('==========================?>',res)

# print(os.path.split(r'a\b\c\d.txt') )
# print(os.path.dirname(r'a\b\c\d.txt') )
# print(os.path.basename(r'a\b\c\d.txt') )


# print(os.stat(r'C:\Users\Administrator\PycharmProjects\19期\day6\soft\conf\settings.py.py').st_size)
# print(os.path.getsize(r'C:\Users\Administrator\PycharmProjects\19期\day6\soft\conf\settings.py.py'))


# print(os.path.normcase('c:/Windows\\system32\\'))


# print(os.path.normpath('c://windows\\System32\\../Temp/') )
#
#
#
#
#
#
# x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(x)
#
#
# print(os.path.normpath(os.path.join(
#     os.path.abspath(__file__),
#     '..',
#     '..'
# )
# ))



import  os

print(os.getcwd())
print(os.chdir(r'/Users/FLS/OneDrive - 北京新橙科技有限公司/pycharmlearningproject/day6-teacher'))
print(os.getcwd())
print(os.curdir)
print(os.pardir)
# print(os.makedirs('1/2/3'))
# print(os.removedirs('1/2/3'))
# print(os.mkdir('1'))
# print(os.rmdir('1'))
print(os.listdir(''))
# print(os.remove('t1'))
# print(os.rename('t2','t222'))
print(os.stat('t222'))
print(os.sep)
print(os.name)
print(os.system('uname -a'))

print(os.environ)
print(os.path.abspath(''))
print(os.path.dirname(''))
print(os.path.getsize('t222'))

print(os.path.join('/','a/b'))
print(os.ctermid())
print(os.fspath('.    '))




print()















