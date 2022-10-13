import shutil
#
#
#打包压缩:day5_bak.tar.gz
# shutil.make_archive('day5_bak','gztar',root_dir=r'C:\Users\Administrator\PycharmProjects\19期\day5')



# import tarfile
# obj=tarfile.open('day5_bak.tar.gz')
# obj.extractall('aaa')
# obj.close()




# shutil.copytree('aaa','bbb',symlinks=False,ignore=None)
# shutil.copytree('aaa','ccc',symlinks=True,ignore=None)

# shutil.rmtree('ccc')


# shutil.make_archive('aaa','gztar',root_dir='aaa')


import zipfile


# #
#
# z=zipfile.ZipFile('111.zip','r')
# z.extractall(path='.')
# z.close()




import  tarfile

# t=tarfile.open('222.tar','w')
# t.add('t3')
# t.close()





t=tarfile.open('222.tar', 'r')
t.extractall('./222')
t.close()













