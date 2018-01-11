# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import shutil


# shutil.copyfileobj(open('t1.log','r'),open('t2.log','w'),length=1)

# shutil.copyfile('t1.log','t2.log')

# shutil.copymode('t1.log','t2.log')

# shutil.copystat('t1.log','t2.log')

# shutil.copy('t1.log','t2.log')

# shutil.copy2('t1.log','t2.log')

# shutil.copytree('a','aa',ignore=shutil.ignore_patterns('tmp*'))
# shutil.copytree('a','aaa',ignore=shutil.ignore_patterns('tmp*'))
# shutil.copytree('a','aaaa',ignore=shutil.ignore_patterns('tmp*'))


# shutil.rmtree('aa')

# shutil.move('a','b')

# shutil.make_archive('b_bak','zip','b')




import  zipfile,tarfile

# z=zipfile.ZipFile('t.bak','w')
# z.write('t1.log')
# z.write('t2.log')
# z.close()

z=zipfile.ZipFile('t.bak','r')
z.extractall('.')
z.close()




# t=tarfile.open('t.tar','w')
# t.add('t1.log',arcname='t1.bak')
# t.add('t2.log',arcname='t2.bak')
# t.close()


# t=tarfile.open('t.tar','r')
# t.extractall('.')
# t.close()


# total,used,free=shutil.disk_usage('b')
# print(total/1073741824, used / 1073741824, free / 1073741824)


# shutil.unpack_archive()