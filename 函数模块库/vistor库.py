#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/13 16:15
# @Project  : pycharmlearningproject
# @File     : vistor库.py

'''
vistor访问者模式：
你要处理由大量不同类型的对象组成的复杂数据结构，每一个对象都需要进行不同的处理。 比如，遍历一个树形结构，然后根据每个节点的相应状态执行不同的操作。

这里遇到的问题在编程领域中是很普遍的，有时候会构建一个由大量不同对象组成的数据结构。 假设你要写一个表示数学表达式的程序，那么你可能需要定义如下的类：

这样做的问题是对于每个表达式，每次都要重新定义一遍，有没有一种更通用的方式让它支持所有的数字和操作符呢。 这里我们使用访问者模式可以达到这样的目的：
'''

class Node:
    pass
class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand
class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass

class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass

class Div(BinaryOperator):
    pass

class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

# Representation of 1 + 2 * (3 - 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)

class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


# 编写一个类来继承visit的方法
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -node.operand

# 调用
e = Evaluator()
# print(e.visit(t4))


# 下面一个例子：就是有很多种数据结构类型的数据，组成json
# Visitor  __init__.py代码 每个数据进来就会
class Visitor():
    """Base class for visitors."""
    def visit(self, node):
        """Visit a node.
        Calls ``visit_CLASSNAME`` on itself passing ``node``, where
        ``CLASSNAME`` is the node's class. If the visitor does not implement an
        appropriate visitation method, will go up the
        `MRO <https://www.python.org/download/releases/2.3/mro/>`_ until a
        match is found.
        If the search exhausts all classes of node, raises a
        :class:`~exceptions.NotImplementedError`.
        :param node: The node to visit.
        :return: The return value of the called visitation function.
        """
        if isinstance(node, type):  # 这个mro简易的判断数据类型的，没看出来这个的用处，直接用type直接就可以
            mro = node.mro()
        else:
            mro = type(node).mro()  # 如果没有判断出来就直接type(node) 来获取类型
        print('mro： ',mro)
        for cls in mro:
            meth = getattr(self, 'visit_' + cls.__name__, None) # 这个就是类的反射，反射对应的方法，并执行。这个cls 其实就是当前类的。
            if meth is not None:
                print('meth: ',meth)  # 这个返回的方法的地址
                print('meth name: ',meth.__name__)  # 这个就是返回的方法的名字
                return meth(node)
        raise NotImplementedError('No visitation method visit_{}'.format(node.__class__.__name__))

class JSONEncoder(Visitor):
    def __init__(self):
        self.indent = 0

    def escape_str(self, s):
        # note: this is not a good escape function, do not use this in
        # production!
        s = s.replace('\\', '\\\\')
        s = s.replace('"', '\\"')
        return '"' + s + '"'

    def visit_list(self, node):
        self.indent += 1
        s = '[\n' + '  ' * self.indent
        s += (',\n' + '  ' * self.indent).join(self.visit(item)
                                               for item in node)
        self.indent -= 1
        s += '\n' + '  ' * self.indent + ']'
        return s

    def visit_str(self, node):
        return self.escape_str(node)

    def visit_int(self, node):
        return str(node)

    def visit_bool(self, node):
        return 'true' if node else 'false'

    def visit_dict(self, node):
        self.indent += 1
        s = '{\n' + '  ' * self.indent
        s += (',\n' + '  ' * self.indent).join(
            '{}: {}'.format(self.escape_str(key), self.visit(value))
            for key, value in sorted(node.items())
        )
        self.indent -= 1
        s += '\n' + '  ' * self.indent + '}'
        return s


data = [
    'List', 'of', 42, 'items', True, {
        'sub1': 'some string',
        'sub2': {
            'sub2sub1': False,
            'sub2sub2': 123,
        }
    }
]


# Visitor 其实就是判断出入数据类型，加上visit_NAME 组成完成的方法名，返回给这个方法
v=Visitor()
# print(v.visit('a'))



print(JSONEncoder().visit(1))











