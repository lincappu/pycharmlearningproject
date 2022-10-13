## unittest 和 pytest 的区别
<br/>
Unittest

unittest是python标准库，自带的单元测试框架，有时候也被称为PyUnit。类似于java的JUnit。

Pytest  
pytest是python第三方单元测试库，功能非常的丰富，也比较成熟，比unittest更简洁方便。

下面会从是否需要安装，用例编写规则，用例分类执行，前置和后置，参数化，断言，报告，是否有失败重跑机制等多维度来分析unittest与pytest测试框架的区别；

一、是否需要安装  
Unittest是标准库，所以是不需要安装的。

pytest是第三方库，所以使用前需要安装：
pip install pytest

二、用例编写规则  
1、Unittest

首先需要导入unittest（import unittest)
测试类必须继承unittest.TestCase
测试方法必须以”test_”开头
测试类必须要有unittest.main()方法

2、Pytest

测试文件必须以”test_”开头或”_test”结尾
测试方法必须要”test_”开头
测试类的命名要以”Test”开头
运行不需要main方法

三、用例分类执行  
1、unittest  
默认执行的是全部的测试用例，但也可以通过加载testsuit执行部分测试用例   
2、pytest
通过@pytest.mark来标记类和方法，pytest.main加入参数（“-m”)只运行标记的类和方法

四、用例的前置和后置  
1、Unittest
unittest提供了setUp/tearDown,在每个用例运行前执行一次，运行结束后执行一次。
SetUpClass和tearDownClass，用例执行前，用例执行结束后，只运行一次。  
2、Pytest  
pytest提供了模块级，类级，方法级等setup/teardown,比unittest的setUp/tearDown要更丰富灵活。 <br />  
模块级（setup_module/teardown_module）开始于模块始末，全局的，整个模块开只运行一次，优先于测试用例。 <br />      
函数级（setup_function/teardown_function）只对函数用例生效（不在类中） <br />  
类级（setup_class/teardown_class）只在类中前后运行一次(在类中)，只针对此类生效  
方法级（setup_method/teardown_method）开始于方法始末（在类中），定义在类里面，每个用例都执行一次

五、参数化  
1、Unittest  
需要依赖DDT库  
2、Pytest  
使用@pytest.mark.parametrize装饰器

六、断言  
1、Unittest    
unittest提供了很多断言方式  
如：assertEqual、assertIn、assertTrue、assertFalse  
2、Pytest  
pytest提供assert表达式，简单，方便

七、报告  
1、Unittest
unittest使用HTMLTestRunnerNew库  
2、Pytest  
pytest有pytest-HTML、allure插件

八、失败是否重跑  
1、Unittest  
unittest没有提供这个功能  
2、Pytest
Pytest通过pytest-rerunfailures插件是支持用例执行失败重跑的，

<br /> 
好了，分析完unittest和pytest它们的区别以后，咱们再来做一个简单的总结:  
unittest和pytest这两个都属于python的单元测试框架，也是目前用的比较多的自动化测试框架。

unittest呢是python自带的，比较传统的测试框架，提供的插件少，用例格式比较复杂。pytest相对来说，更加简单方便 ，兼容性比较强，插件也很丰富。用例出错了还可以重跑，非常的灵活，效率要比unittest更高。