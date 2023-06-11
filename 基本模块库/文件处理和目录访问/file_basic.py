# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 1.xml 格式
# xml 转为字典或者字典转为xml
#
# import  dicttoxml
# from  xml.dom.minidom import parseString
# import os
#
# d=[20,'name',
#    {'name':'bill','age':20,'salary':2000},
#    {'name':'fls','age':30,'salary':3000},
#    {'name':'john','age':40,'salary':4000},
# ]
#
# bxml=dicttoxml.dicttoxml(d,custom_root='person')
# xml=bxml.decode('utf-8')
# print(xml)
#
#
# dom=parseString(xml)
#
# prettyxml=dom.toprettyxml(indent=' ')
# print(prettyxml)
#



# 2.csv 格式文件
# import csv
#
# # with open('a.csv','w') as f:
# #    writer=csv.writer(f,delimter=',')
# #    writer.writerow(['field1','field2','field3'])
# #    writer.writerow(['data1','data2','data3'])
#
#
# with open('a.csv','r',encoding='utf-8') as f:
#    reader=csv.reader(f)
#    for r in reader:
#       print(r)



import pathlib
'''
pathlib 提供纯计算操作而没有I/O操作的纯路径，可以跨平台处理，
比如在unix操作window路径， C:\\test\a\b.log这是一个纯路径的文件，在unix上肯定是不能操作的， 但是如果只是计算这个路径操作是
可以的，但是如果是os.path就不能，因为他会校验这个路径。


pathlib库与os库的对比:
os库                    	                        pathlib库	            描述	英文说明
os.path.abspath(("文件路径"))	             Path("文件路径").resolve()         	将路径转换为绝对路径	-
os.chmod()	                               Path("文件路径").chmod(xxx)         	更改文件权限	change mode
os.mkdir(("文件路径"))              	       Path("文件路径").mkdir()	            新建文件夹	make directory
os.rename("文件路径", "xxx")	               Path("文件路径").rename("xxx")   	重命名文件/文件夹名称	-
os.replace(a, b)	                       Path("文件路径").replace(a, b)    	替换字符串	-
os.rmdir()	                               Path("文件路径").rmdir()          	删除文件夹（里面必须是空的）	remove directory
os.remove("文件路径")/os.unlink("文件路径")   Path("文件路径").unlink()	            删除文件（非目录）	-
os.getcwd()	                               Path("文件路径").cwd()            	获取当前文件工作目录	current work directory
os.path.isdir()	                           Path("文件路径").is_dir()         	判断当前路径是否为目录	-
os.path.isfile()	                       Path("文件路径").is_file()          	判断当前路径是否为文件	-
os.stat()	                               Path("文件路径").stat()	            返回当前路径的信息	status
os.path.isabs()	                           Path("文件路径").is_absolute()   	判断当前路径是否为绝对路径	-
os.path.basename()                      	Path("文件路径").name             	返回文件/目录的基础名称（不带路径）	-
os.path.dirname()                       	Path("文件路径").parent           	返回路径所属文件夹名称	-
os.path.samefile()                      	Path("文件路径").samefile(xxx)   	判断两个文件是否相同	-
os.path.splitext("文件路径")                	(Path("文件路径").stem, Path("文件路径").suffix)	将文件名分离，分成前缀和后缀	stem + suffix
'''

# 1、纯路径类， PurePath     子类: PurePosixPath PureWindowsPath
# 纯路径类提供了不实际访问文件系统路径的操作。
p1 = pathlib.PurePath('c:/Windows', 'd:bar')
# print(p1)

p2 = pathlib.PurePosixPath('/etc/', 'a/', 'a.log')
# 是以/开头，只能有一个在开头，其他可以没有，也可以在末尾，如果有多个/在开头，取最后一个，和join还不一样。
p2 = pathlib.PurePosixPath('/etc/', '/a', '/a.log')  # a.log
# print(p2)

p3 = pathlib.PureWindowsPath('c:/Program Files/PSF')  # 盘符的问题，会自己变化
# print(p3)
# print(p3.parts)


# 2、具体路径类：Path，在PurePath的基础上提供了对路径对象进行系统调用的方法。 Path，PosixPath  WindowsPath
# 涉及到的方法和属性在上面。

path = r'C:\Users\lisonfan\Desktop\jianguoyun\pypeoject\pycharmlearningproject\基本模块库\文件处理'
p = pathlib.Path(path)
# print(p.name)
# print(p.suffix)
# print(p.parent)
# print(p.parent.parent)


# 逐级获取上层文件夹
# for inx,folder_path in enumerate(p.parent):
#    print(folder_path)


'''
os.path 提供了不pathlib更为高级的功能，
'''
# os.path.abspath(path)  返回path规范化的绝对路径
# os.path.split(path)  将path分割成目录和文件名二元组返回
# os.path.splitest(file)  按后缀分成两部分
# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  如果path是绝对路径，返回True
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(path) 返回path的大小
# os.path.getsize(file) 返回文件的大小，如果是文件夹则返回0


'''
fileinput:实现了一次读入多个文件的，
典型用法是在命令行执行python脚本的时候传入文件列表，默认会读取sys.argv[1:]中的所有文件按行读入，默认是文本方式，列表是空则会使用sys.stdin
,如果有一个参数为‘-’，则也会替换为sys.stdin并且可选参数mode和openhook会被忽略，


两个类：下面一个是实现。
fileinput.input()
FileInput()
'''
# import fileinput
# for line in fileinput.input():
#     print(line)


'''
stat()类：通常，你应当使用 os.path.is*() 函数来检测文件的类型；这里提供的函数则适用于当你要对同一文件执行多项检测并且希望避免每项检测的stat() 
系统调用开销的情况。 这些函数也适用于检测有关未被 os.path 处理的信息，例如检测块和字符设备等。

不包含具体的方法，其实只是多个状态标志，这些标志可以用在os.path中进行判断。
'''

'''
filecmp类： 实现对文件和目录的比较，并且可以选取多种关于时间和准确性折衷方案。

cmp类比较文件，以及多个目录下的相同文件。
dircmp类比较目录中的文件。以及递归比对
'''
import filecmp

# print(filecmp.cmp('1.log','2.log'))


'''
glob: 路径名模式扩展，局势
glob(pathname,*,recursive=False)
'''
import glob

# print(glob.glob('./[0-9].*'))


'''
fnmatch  unix文件名的模式匹配判断，返回的是True和False
'''
import fnmatch

# print(fnmatch.fnmatch('./', '*.log'))


'''
linecache  随机读取w文本行：
允许从python源文件中随机读取任意的行，并且尝试用缓存进行内部优化，
'''
import linecache
# print(linecache.getline(__file__,1))


'''
tempfile 创建临时文件和目录：可以跨平台。
'''
# import  tempfile
# with tempfile.TemporaryFile() as fp:
#     fp.write(b'helloworld')
#     fp.seek(0)
#     print(fp.read())


'''
shutil: 提供对一系列文件和目录的高阶操作，提别是文件的拷贝和删除的函数，对于单个文件还是还是用os模块。
核心的点比如说是：
1、拷贝文件：可以是对象、文件、copy  copy2 ，模式、copytree   
2、归档操作。make_archive 
'''



'''
codecs:  自动做编码转换，open函数会默认以bytes类型打开文件，然后转换为Unicode，encoding是指定编码格式，
如果是读：其实是以bytes的方式去读，转换成默认的编码
如果是写：如果参数是unicode，则使用open（）时指定的编码进行编码后写入，如果是str，则先根据源代码文件申明的字符编码，解码成Unicode后再进行上述操作。
它主要的解决场景在于如果出现了不统一或者未知的编码，那这个时候就会出现问题，用这个来统一转码写入。
'''
# import codecs
# f = codecs.open('testfile', mode='rb',encoding='utf-8')
# data = f.read()
# print(type(data))
