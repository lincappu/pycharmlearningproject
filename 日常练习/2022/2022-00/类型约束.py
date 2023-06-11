# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# typing   强类型支持
# 两种用法：
# 1.在声明变量时，变量的后面可以加一个冒号，后面再写上变量的类型
# 2.在声明方法返回值的时候，可以在方法的后面加一个箭头，后面加上返回值的类型

# from typing import List,Tuple,Dict,Sequence,Set,AbstractSet,Any,

# names: List[str]=['Germey', 'Guido']
# version: Tuple[int, int, int] = (3, 7, 4)
# operations: Dict[str, bool] = {'show': False, 'sort': True}

# 函数的形式
# def func(a:int, string:str) -> List[int or str]:
#     list1 = []
#     list1.append(a)
#     list1.append(string)
#     return list1




# Pydantic：使用 python 类型提示来进行数据验证和设置管理的库

from pydantic import BaseModel

BaseModel定义的基础数据类型：
class Demo(BaseModel):
    a: int # 整型
    b: float # 浮点型
    c: str # 字符串
    d: bool # 布尔型
    e: List[int] # 整型列表
    f: Dict[str, int] # 字典型，key为str，value为int
    g: Set[int] # 集合
    h: Tuple[str, int] #


可选数据类型：
from typing import Optional
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: Optional[int]



validator 进行数据校验：

import re
from pydantic import BaseModel, validator

class Password(BaseModel):
    password: str

    @validator("password")
    def password_rule(cls, password):
        def is_valid(password):
            if len(password) < 6 or len(password) > 20:
                return False
            if not re.search("[a-z]", password):
                return False
            if not re.search("[A-Z]", password):
                return False
            if not re.search("\d", password):
                return False
            return True

        if not is_valid(password):
            raise ValueError("password is invalid")


config 的形式进行校验：
from pydantic import BaseModel

class Password(BaseModel):
    password: str

    class Config:
        min_anystr_length = 6  # 令Password类中所有的字符串长度均要不少于6
        max_anystr_length = 20






























