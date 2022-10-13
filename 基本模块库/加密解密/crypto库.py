# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



'''
Crypto 算法库在 python 中最初叫 pycrypto，这个作者有点懒，好几年没有更新，后来就有大佬写了个替代库 pycryptodome。这个库目前只支持 python3，安装也很简单pip install pycryptodome就行了！详细的用法可以看看 官方文档

常见对称密码在 Crypto.Cipher 库下，主要有： DES 3DES AES RC4 Salsa20
非对称密码在 Crypto.PublicKey 库下，主要有： RSA ECC DSA
哈希密码在 Crypto.Hash 库下，常用的有： MD5 SHA-1 SHA-128 SHA-256
随机数在 Crypto.Random 库下
实用小工具在 Crypto.Util 库下
数字签名在 Crypto.Signature 库下
'''




'''
AES算法详解：高级加密标准,它是一种对称加密算法，AES只有一个密钥，这个密钥既用来加密，也用于解密。

AES加密方式有五种：ECB, CBC, CTR, CFB, OFB。
从安全性角度推荐CBC加密方法，本文介绍了CBC,ECB两种加密方法的python实现。

CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
ECB加密不需要iv

接收到的数据中只有密钥而没有偏移量。故使用ECB处理密文。

1、密钥处理
直接处理密钥会报错：‘AES key must be either 16, 24, or 32 bytes long’
因为AES接收的key&vi都必须是有固定长度。
对Key 进行填充至符合规格。

2、密文处理
有可能处理密文时候会报错：'Error: Incorrect padding'
这是因为密文长度不符合规格，对base64解码的string补齐等号就可以了
'''



# AEC加密
from crypto.Cipher  import AES
import  base64

# 第一种方式 补0


# 对 key 的 处理，必须是16 24 32位,对应 AES-128,AES-192,AES-256
key=bytes('123456789'.ljust(16,'0'),encodeing='utf-8')



# 对文本的处理， 补足为 16 的倍数
def  key_to_16(key):
    while len(key) %16 !=0:
        key+='\0'
    return  str.encode(key,encoding='utf-8',errors='strict')



text='nihao'

aes=AES.new(key,AES.MODE_ECB)

text_enc=aes.encrpty(b'helloworld')











