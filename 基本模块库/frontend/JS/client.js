十三章、web浏览器中的js
Window对象：是所有client js特性和API的主要接入点，
    全局属性：不用加.调用，处于作用链顶部，window：是Window引用自身的属性，使用其他属性不需要加window来引用，直接写属性或者方法就行。

js的两类最常用的对象：
    文档对象：Documents和它的Element对象
    应用对象：底层网络API、保存数据、绘制图像。

在HTML里面嵌套JS的四种方法：
    1.内联: <script></script
    2.外置，script src 来引用        最常用
    3.放置在HTML事件处理器中，由onclick或者onmouseover等值指定
    4.放在一个url里，使用"javascript:" 协议。



同源策略：
    js能操作哪些web内容一条完整的安全限制。负责是不同窗口和窗体之间的js代码的交互。
    协议、主机、端口
    限制的不是脚本本身的来源，既不是限制src的位置，而是限制和脚本嵌入的文档的来源有关，即便代码和文档来自不同的来源，js也可以和它嵌入的文档进行交互。当在页面中src包含一个脚本时，就给了脚本作者完全的web权限。
        就是src的位置和加载的内容要一致。
    不严格的同源策略：
    1.document.domain 同时设置为一级域名。
    2.跨域资源共享CORS：使用新的"Orign"请求头和Access-Control-Allow-Origin响应头来扩展HTTP，
    3.跨文档消息，

html和js脚本的执行：
    同步、阻塞模式。
    内联js必须先执行js完后才能在继续渲染
    src的js文件默认是也是如此
    defer、async  延迟，异步的模式，不常用，


js不能做什么：
    1.不删除、写入计算机上的任何文件
    2.没有通用的网络能力，只能进行websocket的通信能力，既客户端和服务器端不能同时用js来写，
    3.自身功能的限制。




十四章、Window对象

1.计时器：
    setTimeout()  setInterval() clearInterval()

    function invoke(f,start,interval,end) {
        if(!start) start=0;
        if(arguments.length<=2){
            setTimeout(f,start);
        }
        else{
            setTimeout(repeat,start);
        }
        function repeat() {
            var h=setInterval(f,interval);
            if (end) setTimeout(function () {clearInterval(h);},end);

        }
    }

    setTimeout()  setInterval() 的第一个参数可以作为字符串传入，这时候它会自动求值。
    如果以0毫秒来设置settimeout那么这个函数不会立即执行，相反会放到队列中，等前面处于等待状态的事件处理程序全部执行完毕，再立即调用它。

2.浏览器定位和导航
    Location本身也是个对象。 window.location === document.location，表示该窗口中当前显示的文档的URL
    分解URL：protocol、host、hostname、port、pathname、search

    function urlArgs() {
        var args={};
        var query=location.search.substring(1);
        var pairs=query.split(&);
        for(var i=0;i<pairs.length;i++){
            var pos=pairs[i].indexOf('=');
            if(!pos){continue;}
            var name=pairs[i].substring(0,pos);
            var value=pairs[i].substring(pos+1);
            value=decodeURIComponent(value);
            args[name]=value;
        }
        return args;
    }

    载入新的文档：
    assgin()  reload()  replace()

3.浏览历史：history属性引用的是History对象
    history.length


4.浏览器和屏幕信息：
    浏览器信息：
    navigator属性引用是navigator对象，包含浏览器厂商和版本信息。
    navigator.appName,navigator.appCodeName,navigator.appVersion
    屏幕信息：screen对象。窗口显示的大小和可用的颜色数量信息。
    availHeight显示的是出去任务栏之类的大小，是整个屏幕的全部大小，类似。
``


5.对话框：
    alert() 显示一条消息然后等待用户关闭，
    confirm() 显示一条消息，要求用户点击 确定或者取消
    prompt() 显示一条消息，等待用户输入字符串，并返回那个字符串。

    function do(){
        var name=prompt('you name:');
        var correct=confirm('you need' +name+'confirm or cancel');
        while (!correct) alert('hello:'+name);
    }

    showModalDialog()方法：包含一个模拟态的对话框，    基本已经废弃

6.错误处理：
    onerror对象：时间处理程序。现在已经被try/catch取代。现在很少使用。


7.作为window对象属性的文档元素。
    元素id会自动成为隐式的全局变量：隐式声明。
    如果html文档有用id属性来为换一个元素命名，但是window对象中没有这个名字的属性，那么windwo对象会自动创建一个属性，它的名字是id属性的值，并且他们指向文档元素的中htmlelement对象，这样它就自动成为了全局对象。
    但是如果window已经有此名字的属性会不会发生这一步。显示声明的会覆盖隐式声明的。

8.多窗口和窗体：独立窗体和嵌套窗体
    每一个标签页都是独立的上下文，独立的window对象。受同源策略限制。一般不会交互。但h5提供一个基于事件的消息api可以用于ifram间通信。

    open 四个参数
    close 默认只能关闭js自己创建的iframe，在表示窗体而不是顶级窗体或者标签页上的Winod对象执行close方法不会有任何效果，它不能关闭一个窗体。

    opener 返回父窗体parent。 只有顶级窗体parent==self
    top 直接表示顶级窗口。




十五章、脚本化文档 DOM，
1.文档的层次化结构
    window对象来表示一个窗体，而document对象来表示一个窗体内的内容
    树状结构：
    Documents:根部，代表整个文档
    Element：代表html元素，
    Text：代表文本节点。
    common 代表注释。
    三者都是Node的子类。

    区别：
        Document  代表一个文档，  Element 对象代表文档中的一个元素
        HTMLDocument  HTMLElement  针对的是HTML文档和元素，是上一个的子集。


2.如何选取文档中的元素
    id： 唯一 document.getElementById();
    name  不必唯一 document.getElementsByName()
    标签     document.getElementsByTagName()
    css类    document.getElementsByClassName()
    css选择器  document.querySelectorAll()

    document.all  返回除文本对象之外的所有元素


3.文档的遍历

    parentNode  childNode  firstChild lastChild
    nodeType  1 element 3 text 8 conment  9 document     11 documentFrament
    nodeValue  text或者是comment节点的内容
    nodeName 元素标签名 大写

    <html> 一般是作为/节点。


4.属性
    获取HTMLDocument元素的属性，先获取相对应的元素，然后直接用.引用他的属性

    getAttribute   setAttribute 设置非标准HTML属性。
    getAttributeNS() 来自其他空间  依次类推

    使用Element元素的属性的方法： document.body.attributes[0] 只针对element节点。

5.元素的内容
    HTML的字符串    解析 innerHTML

    纯文本字符串    paraContent  和innertext方法的区别

    text节点    textContent


6.节点的操作

    创建：
        document.createTextNode()类似的方法
        复制方法  cloneNode()
    插入：
        document.insertBefore()   document.appendChild()
    删除/替换：
        document.removeChild()  document.replaceChild()


    临时节点： DocumentFragment 其他节点的临时容器。
        document.createDocumentFragment()
        它总是独立，不属于任何文档的一部分，也即是parentNode总是Null，可以有子节点。如果要插入一个fragment则是将整个fragment都插入进去


7.生成目录表



8.文档和元素的几何形状滚动



9.html表单
    <form>  最早的交互式脚本实现方式
    服务器端程序是基于表单提交动作的，按表单块处理数据
    客户端是基于事件的-可以对单独的表单块进行处理。


    获取表单和表单元素  返回时的是一个collections对象。

    表单和元素的属性： html元素

    表单和元素的事件处理程序：
        submit   onsubmit() reset onreset()   这个只能通过按钮来触发，而不能通过函数来触发。

        click onClick()  change onchange()    表单激活、表单改变、

        focus  blur 事件，获取或者失去鼠标焦点。


    按钮： 是动作就是按钮，是链接就是链接。
        开发按钮：单选和多选的按钮，checked 或者defaultcheckted
        触发onclick()事件处理程序

    文本域：
        value 就是输入的值，


document.write() 方法。
    只有在解析文档的时候才会这个方法输出HTML到当前文档中，









十六章、脚本化CSS
    <script>  <style>标签不会当成html来解析，由另外的处理程序来解析。

脚本化样式表：
    使用js查询和设置单个元素
    两种场景：
        1.直接使用标签里查找
        2.stylesheet 属性，是☁️一个只读的类数组对象，包含了一个CSSStyeSheet对象，表示与文件档关联在一起的样式表，

开关样式表： 从stylesheet查找这个属性，然后设置为属性为.disabled=true
    插入、删除、修改 都是一样的，修改这个数组的属性值。





十七章、事件处理
    浏览器采用的异步事件驱动模型，所以只能用event。时间是浏览器来定义的，而不是js来定义的。

1.事件类型：
    表单事件
    Window事件   表示窗口本身而不是窗口内的文档的变化。 load 窗口内的所有资源全部加载完毕会触发。 unload 离开当前文档转向其他文档，
    鼠标事件：
    键盘事件：
    DOM事件：3级DOM事件，
    HTML5事件
    触摸屏和移动设备事件：

2.注册事件处理程序：
    早期：将事件传给目标对象作为属性
    现在：将事件处理程序传给对象的一个方法。

    设置属性：
    window.onload=function(){
        var elt=document.getElementById('address');
        elt.onsubmit=function(){return validate(this);}
    }

    设置标签：
    <button onclick='alert(thank you);'>



    addEventListener()  所有的Window  document 和文档元素都定义了这个方法，这个方法可以为目标注册事件处理程序

    attachEvent()方法： 老的方法


3.事件处理的调用：
    当事件发生时自动就调用了处理程序。
    把事件处理程序作为第一个参数
    返回值： true 或者false。
    调用顺序：对象属性》addEventListener》attachEvent
    事件传播：冒泡：向上传播执行。
    事件取消：上面三种方式分别的取消方式： return false ; preventDfault方法；returnValue属性
        DOM模型：defaultPrevented()方法


 各种事件用到的时候再详细研究




十八章、脚本化HTTP
    使用js操作http，本章主要是说在没有发生窗口重载或窗体内容的情况下，js如何实现浏览器如何与服务器之间进行通信。

    ajax 异步js和XML。主要功能就是使用js操做HTTP和web服务器进行数据交换，不是导致页面重载。
    comet与ajax相反，ajax是浏览器从服务器拉数据，而comet是服务器向浏览器推数据

    xmlhttprequest对象首先要实例化一个对象：
    var request=new XMLHttpRequest();

    第二步:
    open(http方法，URL，false) 最后一个参数表示是同步请求还是异步请求。




十九章、JQuery
js的库，简化通用操作，能隐藏浏览器之间的差异，聚焦于查询，如使用css选择器来识别一组文档元素

1.jquery（）全局函数调用
$ 快捷别名，如果是要自己定义变量 首先要用jQuery.noConflict() 来释放$变量，让其指向子定义的变量。


jQuery()==$() 返回对象是一个类数组，toArray()可以转换为真是的数组，
调用方式：
    1.css选择器(字符串)给它，  返回当前文档中匹配选中的元素集合
    2.传递一个Element、Document、Window对象，这时$() 只是将该对象封装成jquery的对象返回，这样能用jquery的方法而不是原生的DOM方法来操作
    3.传递HTML文本字符串，这时jquyey会创建好html元素，并封装为jquery对象返回，必须包含一个<>js的两类最常用的对象
    4.传入一个函数给$(), 当文档加载完毕切DOM可以操作时，传入的函数将被调用。
    最常见的匿名函数：jQuery(function(){});
    此时 this代表的是文档对象，


查询结果返回的是一个类数组，toArray()可以转换为真是的数组，可以通过[]调用，
    属性：length   selector(要查询的字符串)   context(第二个参数)
    方法：  each() map() index() toArray() get()

2.查询和设置属性： getter  setter

html属性：
$('form').attr('action')  获取属性
$('#form').attr(src,'a.jif')  设置属性
$('#form').removeAttr(src,'a.jif')


css属性：
$('h1').css('{ backgroudColor:red , textColor:white,}')

css类操作：
addClass()
remoteClass()
toggleClass()
hasClass()
removeClass()


获取表单值：
val() 获取html表单元素的value属性，


text() html() 用来获取和设置元素的纯文本或者html内容，


获取元素的位置：宽高、偏移等

获取和设置元素数据： data()





3.修改文档结构
复制元素clone()

包装元素 wrap()  wrapInner()   wrapAll()

删除元素：  empty()级联删除    remove()只移除元素



4.jquery时间处理程序：







二十、cookie的作用

可以存储少量的数据，同时和页面和站点相关，

是否启动：navigator.cookieEnabled  这个参数来显示

属性：
    有效期：可以设置， max-age的属性，过期后会自动删除，
    作用域：path+domain

限制：
    20个字段
    4KB
































