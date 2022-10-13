# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


class class_example(object):
    pass


obj=class_example()
print(obj)
print(type(obj))
print(type(class_example())) #  这个等价于obj
print(type(class_example)) # type  类的类型就是 type，
print(type(int))  # 也是type  原因同上


'''这个class_example是一个类，但同时也是一个 object，同时也是一个可以创建其他object 的 object，所以这个 object 同时也是一个 class的原因
如果这是个对象，那么就具备对象具有的属性，赋值，设置属性等，
'''

动态创建 class， 1.是在方法中创建 class，
def dynamic_class_class(name):
    class  classtest(object):
        pass

    return classtest

但是这种方法依然没有特别动态，因为需要自己定义类中内容，下面要像产生 instance 那样产生 class，  type可以动态创建 class，type()函数可以接收class的描述来作为参数并返回所生成的class object
type(class_name, tuple_of_parent_class, dict_of_attribute_names_and_values)
其中第二个参数tuple_of_parent_class用来表示继承关系，可以为空。第三个参数用来描述我们所要创建的类所应该具有的attribute。如下面的例子所示：


mateclass 就是用来创建 class object 的 class:
如：
    class=metaclass()
    object=class()

type就是一个 metaclass，是在幕后创建所有 class 的 meteclass： 既obj.__class__.__class__=type



自定义 metaclass ：metaclass 的主要目的就是在 class 被创建的时候对生成的 class 进行自动的动态修改。

下面这个例子就是通过修改 metaclass来修改修改默认 class 属性或者类行为的方法。
def upper_attr(class_name, class_parents, class_attr):
    '''Return a class object, with the list of its attribute turned into
    uppercase.
    '''
    # pick up any attribute that doesn't start with '__' and turn it into uppercase.
    uppercase_attr = {}
    for name, val in class_attr.items():
        if name.startswith('__'):
            uppercase_attr[name] = val
        else:
            uppercase_attr[name.upper()] = val

    # let `type` do the class creation
    return type(class_name, class_parents, uppercase_attr)


class Foo(object):
    # this __metaclass__ will affect the creation of this new style class
    __metaclass__ = upper_attr
    bar = 'bar'


