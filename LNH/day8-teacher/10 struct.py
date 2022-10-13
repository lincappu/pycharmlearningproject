import struct

# res1=struct.pack('i',23322) # i代表打包后的结果是4个Bytes，打包的目标整型数字
# print(res1)
# print(len(res1))
#
# res2=struct.unpack('i',res1)
# print(res2)
# print(res2[0])

# res3=struct.pack('q',23222222232222222222222222222222222222222)

#
# #制作报头
# import json
# header_dic={
#     'filename':'a.txt',
#     'total_size':123111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112312111111111,
#     'md5':'xxxxxxxxx'
# }
# head_json=json.dumps(header_dic)
# head_bytes=head_json.encode('utf-8')
#
# print(head_bytes)
# print(len(head_bytes))


import struct

# res=struct.pack('hhh',1,2,3)  # 打包成字节流
# print(res)
#
# print(struct.calcsize('ii'))
# res2=struct.unpack('hhh',res)      # 解包的结果是元组。
# print(res2)
# print(type(res2))

# buf3 = 'hello  world'
#
# bin_buf3 = struct.pack('12s',bytes(buf3,encoding='utf-8') )  #字符串要先转为 bytes 类型
#
# print(bin_buf3)





# struct header {
#   int buf1;
#   double buf2;
#   char buf3[11];
# }
bin_buf_all = struct.pack('id11s', buf1, buf2, bytes(buf3,encoding='ascii'))
ret_all = struct.unpack('id11s', bin_buf_all)
print(bin_buf_all, '  <====>  ', ret_all)



# record = b'raymond   \x32\x12\x08\x01\x08'
#
# a1,a2,a3,a4=struct.unpack('<10sHHb',record)
#
# print(a1,a2,a3,a4)
