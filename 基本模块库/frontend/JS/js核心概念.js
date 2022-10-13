3.8  类型转换
隐式：
    NaN，非空非数字也是 NaN， undefied，对象都是 true，tostring()   number()  Boolean() 做转换的方法。== 和===的两个转换特殊点
显式：
    boolean() number()  string() object() 方法，NaN， undefied  这两个特殊
对象转变为原始值：
对象到布尔值：所有对象都是 true
到字符串：tostring()， valyeOf() ：弱，简单返回本身。日期类特殊：70 年的毫秒数。
到数值：初日期外，按操作符及隐式转换为数字。



变量：

定义：var   undefied    未声明也不一定会报错，全局可以不写，局部必须写var
作用域：全局，局部，局部可以覆盖全局。函数嵌套引起变量作用域的嵌套，
函数作用域：就是块作用域，函数内所有变量全部整体可见。
声明提前：函数内的变量声明在函数体的顶部。在函数内会重新声明覆盖全局的那个变量。变量定义原则：靠近作用域而不是使用的地方。
var 创建的变量是不可以delete 手动删除，未用 var 定义的变量是可以的。
全局变量允许使用 this 来引用。
作用链。



四、表达式和运算符：
表达式：
    原始表达式：最小单位就是赋值。
    对象和数组表达式：数组在内部进行计算。对象用{}标示，内部值计算一次。
    函数表达式：其实就是函数的返回值。
    属性访问表达式： express . identifier  或者是 expression [expression]   .和[之前都会被先计算。
    调用表达式：其实就是函数调用的形式。
    对象创建表达式：new 加函数名（）
运算符：
    typeof 检测操作数类型。 instanceof测试对象类。
    操作数个数：唯一一个三元运算符：条件判断运算符  ?:       x>0 ? x: -x
    左值：在赋值表达式左边的值，变量、对象属性、和元组元素。自定义函数不能返回左值。
    优先级。
    结合性
    在 js 中所有的数都是 fload 型的。
    + 号的特殊转换。
关系表达式：
    表达式总是返回一个 boolean 值。
    == 相对相等，允许进行转换。  === 严格相等，不能进行转换。
逻辑表达式：
表达式计算：
    eval() 必须是字符串，不能被赋予别名。
其他运算符：
    ?:
    typeof  返回的是传入参数的类型。
    delete 删除属性或者元素。
    void

五、语句
条件：if switch
循环: for  while
跳转: continue break  throw

复合语句和空语句：  ;就是空语句，
声明语句：var  function  函数声明要加{},函数声明可以嵌套，但是只能出现在所嵌套的函数的顶部，不能是 if  while 循环之内。函数声明语句创建的变量是
        无法被删除的，可以覆盖。
switch  可以用return 或者是 break 结束循环。
throw:  try catch finally 结构
with  临时扩展作用域链，js 中避免使用 with 语句。
    with(document.forms[0]){
        name.value='';
        address.value='';
        email.value='';
    }
    减少了大量的输入。
    只有在查找标识符的时候才会用到作用域链。
debugger：




六、对象
除了字符串、数字、boolean、NaN、undefied以外都是对象。
内置对象、宿主对象、自定义对象、   自有属性、继承属性

创建对象：
    对象直接量： 数组、列表、字典
    new 函数名()
    原型：每一个对象(除 null) 都有另一个对象相关联。对象都是对原型的继承。object.create(原型,描述)

属性值：. []  两种取值方式。
属性的继承关系：向原型查找-->向原型的原型查找直至找到一个 NULL 的对象。
属性不存在是undefined

delete 只能删除自用属性不能删除继承属性。不能删除全局属性、全局函数、delete this.x

枚举属性：对象继承的内置方法是不可枚举、给对象添加的属性是可枚举的。

存取器属性：getter  setter
    结构：get  set  函数名() {},

属性特性：value writeable  enumerable configurable  属性特性可以被修改： object.defineProperty（）

对象属性：
    原型：用来继承
    类属性：是一个字符串、用来表示对象类型信息。
    可扩展性：是否可以给对象添加新属性。

序列化对象：
    json.stringify()  json.parse()   序列化和反序列化。

对象方法：
    所有对象都是从 object.prototype继承属性。




七、数组
定义：直接量， 为定义的值都是undefied
数组是对象：所以不会出现越界的错误，没有就是显示undefined，省略的元素在数组中是存在的，值就是undefined。
    既 a1=[,,,] 表示有3个元素为undefined，undefined，undefined，
    而： a2=array[3]  这表示这个数组是空。没有一个元素。
稀疏数组：就是undefined。

操作： push  delete
遍历： if (!a[i]) continue或者a[i]===undefied      foreach()函数。

数组的数组： 二维数组,
        for table=new array(19)
        for (var i=0;var< table.length;i++)
            table[i]=new array(10)
        for(var row=0;row<table.length;row++){
            for(col=0,col<table.length;col++){
                table[row][col]=row*col
            }
        }

方法：
    join() 转换为字符串，
    concat() 按原样拼接所有的元素，

EMAC5的方法：
        forEach()
        map() 返回的是返回值的数组。





八、函数
函数既对象。
函数调用：
        作为函数
        作为方法
        作为构造函数
        通过call()和apply()方法间接调用。

this没有作用域的限制，不会继承，指向调用它的对象，如果想要访问外部函数的this值，需要将这个this值保存在同一个作用域的变量里。通常用self来保存this。
实参对象：
    arguments来存储所传入的参数，并不是真正的数组，而是一个实参对象，实参对象的数组元素是函数形参所对应实参的别名，两者指向同一个值，通过实参名字修改实参值了，通过arguments也可以获得更改后的值。

函数的作用域：
        体内都可见，体外不可见。


高阶函数：
    函数的函数
    记忆能力的函数，递归函数时使用到




九、类和模块
原型对象：就是类 inherit表示继承于原型对象。任何类的方法和属性都是通过this这个关键字来访问
     // 定义工厂函数。
    function range(from,to) {
        var r=inherit(range.methods);
        r.from=from;
        r.to=to;

        return r;
    }
    // 定义原型对象的方法
    range.methods={
        includes: function (x) {
            return this.from <=x && x >=this.to;
            }
        foreach: function (f) {
            for (var x=Math.ceil(this.from);x<=this.to;x++){
                f(x);
            }
        toString: function () {
            return "("+this.from+"..."+this.to+")";
             }

        }
    }



构建函数：  属性的名字必须是prototype
        Range.prototype={ 定义的属性和方法}
        构建函数和类的标识符：r instanceof range， 检测的不是r是不是由range()构造函数而来，而是会检查r是否继承于range.prototype。
        对于任意的函数 F=F.prototype.constructor    constructor实际就是指向的是一个函数对象。


类和类型：
    构造函数时公共标识，原型是唯一标识
    instanceof 递归继承
    isPrototypeOf(属性或者方法)  检测原型是否有这个属性或方法。


鸭子类型：强调功能而不强调定义。



十、正则表达式的模式匹配。
正则用RegExp对象来表示。

RegExp对象： 注意是两个\\  第二个参数是全局修饰符。
        reg= new RegExp('\\d{5}','g')
    属性：
        source  返回正则本身
        global 是否带修饰符g
        ignoreCase 是否带有i
        multiline  是否带有m
        lastIndes  如果有g 返回下一次开始检测的位置。
    方法：
        exec()  null 或者 是匹配到的结果
        test() 测试是否有不为空。



十一、js的子集和扩展
子集：
常量和局部变量：
        常量：const来定义，不可重复赋值，定义在函数定义的顶部
        let：和var一致，定义的变量只在最近的函数体内内可以使用
        let表达式：做计算用的，let (x=x+1)
结构赋值：
        将右侧的数组或者对象元素一一取出来然后赋值给左侧的数组或者对象的元素，两边的个数不要求一致
        右侧是对象的情况：let {r:red,g:green,b:blue} 名值对， 属性:变量，用{}括号扩起来

迭代：
        for/each 遍历的是属性的值，for/in遍历的是属性
        o={1:one,2:two,3:three}]
        for each (let v in o) { console.log(v); }
        迭代器：






十二、服务器端js
    Rhino
    Node





