# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


'''
secrets 模块用于生成高度加密的随机数，适于管理密码、账户验证、安全凭据及机密数据。
最好用 secrets 替代 random 模块的默认伪随机数生成器，该生成器适用于建模和模拟，不宜用于安全与加密。

随机数
secrets 模块是操作系统提供的最安全地随机性来源。

class secrets.SystemRandom
用操作系统提供的最高质量源生成随机数的类。详见 random.SystemRandom。

secrets.choice(sequence)
返回从非空序列中随机选取的元素。

secrets.randbelow(n)
返回 [0, n) 范围内的随机整数。

secrets.randbits(k)
返回 k 个随机比特位的整数。

生成 Token
secrets 模块提供了生成安全 Token 的函数，适用于密码重置、密保 URL 等应用场景。

secrets.token_bytes([nbytes=None])
返回含 nbytes 个字节的随机字节字符串。如果未提供 nbytes，或*nbytes* 为 None，则使用合理的默认值。

>>> token_bytes(16)
b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'
secrets.token_hex([nbytes=None])
返回十六进制随机文本字符串。字符串有 nbytes 个随机字节，每个字节转换为两个十六进制数码。未提供 nbytes 或为 None 时，则使用合理的默认值。

>>> token_hex(16)
'f9bf78b9a18ce6d46a0cd2b0b86df9da'
secrets.token_urlsafe([nbytes=None])
返回安全的 URL 随机文本字符串，包含 nbytes 个随机字节。文本用 Base64 编码，平均来说，每个字节对应 1.3 个结果字符。未提供 nbytes 或为 None 时，则使用合理的默认值。

>>> token_urlsafe(16)
'Drmhze6EPcv0fN_81Bj-nA'
'''

import secrets

print(secrets.choice([1, 2, 3, 4, 5]))
print(secrets.randbelow(10))
print(secrets.randbits(8))

print(secrets.token_bytes(16))
print(secrets.token_hex(16))
print(secrets.token_urlsafe())

#  例子： 生成长度为 8 为的字符和数字的密码
import string

alphabet = string.ascii_letters + string.digits

password =''.join(secrets.choice(alphabet) for i in range(8))