# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from passlib.hash import pbkdf2_sha256,oracle10,md5_crypt
from passlib.context import CryptContext
from passlib.totp import TOTP
from passlib.totp import generate_secret


# 通用加密抽象类：PasswordHash

# h=pbkdf2_sha256.hash('nihao')
# print(h)
# print(pbkdf2_sha256.verify('nihao',h))

pwd_context=CryptContext(
    schemes=["pbkdf2_sha256", "des_crypt"],
    deprecated="auto",
)

h2=pwd_context.hash('nihao')
h3=pwd_context.hash('nihao')
print(h2)
print(h3)
print(pwd_context.verify('nihao',h2))
print(pwd_context.verify('nihao',h3))

# 带校验用户名的 hash
h4=oracle10.hash('nihao',user='admin')
print(h4)
print(oracle10.verify('nihao',h4,user='admin'))
print(oracle10.context_kwds)
print(pbkdf2_sha256.context_kwds)

# identify 验证密文是哪种加密方法加密的
h5=pbkdf2_sha256.hash('nihao')
print(pbkdf2_sha256.identify(h5))


# CryptContext 功能：
# 1.就是和上述 3 个方法是一样的 hash  verify  identify
# 2.为不同的加密算法提供不同的默认设置，而不是将其硬编码到每个 hash()调用，
# 3.指定某些弃用算法，

myctx = CryptContext(["sha256_crypt", "ldap_salted_md5"]) # 按位置排序
myctx.hash("password", scheme="sha256_crypt")
myctx.update(sha256_crypt__default_rounds=91234,ldap_salted_md5__salt_size=16)

# 序列化到文件中
cfg=myctx.to_dict()
cfg=myctx.to_string()

# 然后在需要的位置进行加载
myctx2=CryptContext.from_string(cfg)
myctx2=CryptContext.from_path('/some/path/on/local/system')


# 动态令牌：totp 支持双因素验证到应用程序,
延伸：动态令牌的种类：
OTP：一次性密码
HOTP：HMAC-based One-Time Password 简写，表示基于 HMAC 算法加密的一次性密码。是事件同步，通过某一特定的事件次序及相同的种子值作为输入，通过 HASH 算法运算出一致的密码。
TOTP：Time-based One-Time Password 简写，表示基于时间戳算法的一次性密码。 时间同步，基于客户端的动态口令和动态口令验证服务器的时间比对，一般每 60 秒产生一个新口令，要求客户端和服务器能够十分精确的保持正确的时钟，客户端和服务端基于时间计算的动态口令才能一致。　　

OTP 原理：
OTP(K,C) = Truncate(HMAC-SHA-1(K,C))
其中，
K 表示秘钥串；
C 是一个数字，表示随机数；
HMAC-SHA-1 表示使用 SHA-1 做 HMAC；
Truncate 是一个函数，就是怎么截取加密后的串，并取加密后串的哪些字段组成一个数字。
对 HMAC-SHA-1 方式加密来说，Truncate 实现如下：
HMAC-SHA-1 加密后的长度得到一个 20 字节的密串；
取这个 20 字节的密串的最后一个字节，取这字节的低 4 位，作为截取加密串的下标偏移量；
按照下标偏移量开始，获取4个字节，按照大端方式组成一个整数；
截取这个整数的后 6 位或者 8 位转成字符串返回。


HOTP:c是随机数
TOTP：c是时间戳

TOTP原理：
TOTP(K,C) = HOTP(K,C) = Truncate(HMAC-SHA-1(K,C))
C = (T - T0) / X   # x 是时间步数，也就是多长时间产生一个动态密码，



