# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

1.动态语言和静态语言的区别
动态语言只有在执行时候才创建资源的

2.新式类和旧式类的区别

然后是
type(类名)  这个结果是 type  实际就是类的类型是什么就是 type
和 type(实例名)这个结果是类名   实例的类型是类


class 类名 这个是用来定于类的方式的
如果是创建类就要用到 metaclass，先用 metaclass(元类) --类--实例 这个顺序

定义元类：一般是以 metaclass 来结尾



引用场景： ORM  用类来代表表的操作。


创建元类：
class Meta(type):
    pass

class listmetaclass(metaclass=Meta):
    pass

理论上上元类要实现 init 和 new 方法