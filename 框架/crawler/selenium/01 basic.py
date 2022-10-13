# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



import time

from selenium库 import webdriver
from  selenium库.webdriver import Chrome
from  selenium库.webdriver.common.alert import Alert



# 1,查找页面元素：  元素选择器.
返回的是一个webelement对象，list类型，并且只会返回找到的第一个，没找到则返回NoSuchElementException异常

find_element_by_id
find_element_by_name
find_element_by_xpath


# 超文本连接匹配： 匹配的是text字段，下面这个是子串匹配。
find_element_by_link_text
find_element_by_partial_link_text


find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector


一次查找多个元素：  只有id是唯一的，其他都可以不唯一，所以这个最准确
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

私有方法： find_element 和 find_elements开头的，这个返回的是列表
使用BY方法：
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

关联定位：
above()
below()
toLeftOf()
toRightOf()
near()  50px以内的元素



passwordField = driver.find_element(By.ID, "password")
emailAddressField = driver.find_element(with_tag_name("input").above(passwordField))





页面元素：
class selenium.webdriver.remote.webelement.WebElement(parent, id_, w3c=False)
代表一个DOM
refresh_check的机制。

元素属性：
get_attribute(name)
is_displayed() - 元素对用户是否可见
is_enabled() - 元素是否可用
is_selected() - 元素是否被选中, 可用来检测单选或者复选按钮是否被选中
screenshot(filename) - 获取当前元素的截图，有IOError会返回False, 文件名要包含完整路径
send_keys(*value) - 模拟向元素输入
submit() - 提交表单
location - 元素在可渲染的画布上的位置
parent - WebDriver实例的内部引用，元素是从哪里发现的
rect - 元素尺寸和位置的dict
screenshot_as_base64 - 当前元素截图的base64编码字符串
screenshot_as_png - 当前元素截图的二进制数据
size - 元素的尺寸
tag_name - 元素的标签名
text - 元素的文本



2. 等待事件：
driver.set_page_load_timeout()  # 设置页面加载超时
driver.set_script_timeout()  # 设置页面异步js执行超时
window.stop() 停止 js 执行


本质原因：
web平台就是异步的，webdriver不跟踪DOM的实时活动状态，

显式等待：  默认是每隔500ms查询一次。
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()


常用的判断条件：
title_is 标题是某内容
title_contains 标题包含某内容
presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')
visibility_of_element_located 元素可见，传入定位元组
visibility_of 可见，传入元素对象
presence_of_all_elements_located 所有元素加载出
text_to_be_present_in_element 某个元素文本包含某文字
text_to_be_present_in_element_value 某个元素值包含某文字
frame_to_be_available_and_switch_to_it frame加载并切换
invisibility_of_element_located 元素不可见
element_to_be_clickable 元素可点击
staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
element_to_be_selected 元素可选择，传元素对象
element_located_to_be_selected 元素可选择，传入定位元组
element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False
alert_is_present 是否出现Alert

多个WebDriverWait条件等待写法：
使用CSS_SELECTOR
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".element_A_class, .element_B_class"))
XPATH通过lambda使用：
element = WebDriverWait(driver,20).until(lambda driver: driver.find_element(By.NAME,"element_A_name") or driver.find_element(By.ID,"element_B_id"))
还可以通通过多个 try/except{} 来完成。



隐式等待：
隐式等待是全局等待，指定的webdriver轮询DOM的次数，默认是0次， 并且这个是不确定的，在不同系统上默认值是不一样的
所以不建议使用




!!!!! 动作链：针对于全局交互动作，比如说鼠标拖拽、键盘按键，
ActionChains对象，是一个队列，调用perform()方法时，队列里面的动作会按照队列的顺序进行触发


链式写法：
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()


队列写法：
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
action.perform()


具体的行为：
click(on_element=None)点击一个元素
参数： * on_element:要点击的元素，如果是None，点击鼠标当前的位置

click_and_hold(on_element=None) 鼠标左键点击一个元素并且保持
参数： * on_element:同click()类似

double_click(on_element=None) 双击一个元素
参数： * on_element:同click()类似

drag_and_drop(source, target) 鼠标左键点击source元素，然后移动到target元素释放鼠标按键
参数： source:鼠标点击的元素 target:鼠标松开的元素

drag_and_drop_by_offset(source, xoffset,yoffset) 拖拽目标元素到指定的偏移点释放
参数: source:点击的参数 xoffset:X偏移量 * yoffset:Y偏移量

key_down(value,element=None) 只按下键盘，不释放。我们应该只对那些功能键使用(Contril,Alt,Shift)
参数： value：要发送的键，值在Keys类里有定义 element:发送的目标元素，如果是None，value会发到当前聚焦的元素上
例如，我们要按下 ctrl+c:
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

key_up(value,element=None) 释放键。参考key_down的解释
move_by_offset(xoffset,yoffset)将当前鼠标的位置进行移动
参数： xoffset:要移动的X偏移量，可以是正也可以是负 yoffset:要移动的Y偏移量，可以是正也可以是负

move_to_element(to_element)把鼠标移到一个元素的中间
参数： * to_element:目标元素

move_to_element_with_offset(to_element,xoffset,yoffset)
鼠标移动到元素的指定位置，偏移量以元素的左上角为基准
参数： to_element:目标元素 xoffset:要移动的X偏移量 * yoffset:要移动的Y偏移量

perform()
执行所有存储的动作

release(on_element=None)释放一个元素上的鼠标按键，
参数： * on_element:如果为None,在当前鼠标位置上释放

send_keys(*keys_to_send) 向当前的焦点元素发送键
参数: * keys_to_send:要发送的键，修饰键可以到Keys类里找到

send_keys_to_element(element,*keys_to_send)向指定的元素发送键





# !!!!  警告框
警告框, 提示框和确认框

dr = webdriver.Chrome()

dr.get('https://www.baidu.com/')

inp = dr.find_element_by_id('kw')
searcH_button = dr.find_element_by_id('su')
inp.send_keys('python')
searcH_button.click()

name_prompt = Alert(dr)
name_prompt.send_keys('nihao')
name_prompt.accept()

time.sleep(10)
dr.quit()




# 浏览器驱动：
chrome
为主：

create_options()
launch_app(id)以特定的id启动Chrome
quit()  退出

# 在单个窗口上进行的操作，控制浏览器页面的跳转。
# 在单个窗口上进行的操作，控制浏览器页面的跳转。
back() 回退
forward() 前进


属性：
session_id
session_id - WebDriver控制，浏览器会话产生的一个String
ID
capabilities - 返回浏览器会话的可用功能dict，




# UI支持：

class selenium.webdriver.support.select.Select(webelement)


deselect_all() - 清除所有的选中输入。仅当选择项支持多选的时候可用，如果不支持多选会抛出NotImplementedError。
deselect_by_index(index) - 取消指定索引的选项的选中。这个方法会检查index属性，而不仅仅是计数
deselect_by_value(value) - 取消所有选项的值匹配的选中状态。



all_selected_options - 返回这个选择标签的所有选中选项list
first_selected_option - 选择标签的的第一个选中项(或者一个正常选择框的当前选中项)
options - 选择标签的所有选项list


class selenium.webdriver.support.wait.WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)


until(method, message='')
调用驱动提供的方法名当参数，直到方法返回值
不是
False
until_not(method, message='')
调用驱动提供的方法名当参数，直到方法返回值
是
False

#  颜色支持。


# 预期条件支持。



键盘支持：
Keys 支持发送特殊字符， Keys.ENTER

sendKeys
keyDown
keyUp
clear



上下文管理：
# 或者使用上下文管理器
from selenium库.webdriver import Chrome

with Chrome() as driver:
# 你自己的代码放在这个缩进中




http代理功能：
例子：
from selenium库 import webdriver

PROXY = "<HOST:PORT>"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}
with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://selenium.dev")




页面加载策略：
这个只是针对于动态内容来说的， 静态内容是不会变化的。document.readstate 的状态变成了complete
单页应用程序中 (例如Angular, react, Ember) , 一旦动态内容加载完毕 (即pageLoadStrategy状态为COMPLETE) , 则点击链接或在页面内执行某些操作的行为将不会向服务器发出新请求, 因为内容在客户端动态加载, 无需刷新页面.
单页应用程序可以动态加载许多视图, 而无需任何服务器请求, 因此页面加载策略将始终显示为 COMPLETE 的状态, 直到我们执行新的 driver.get() 或 driver.navigate().to() 为止.
具体策略如下：
normal
此配置使Selenium WebDriver等待整个页面的加载. 设置为 normal 时, Selenium WebDriver将保持等待, 直到 返回 load 事件
默认情况下, 如果未设置页面加载策略, 则设置 normal 为初始策略.
eager
这将使Selenium WebDriver保持等待, 直到完全加载并解析了HTML文档, 该策略无关样式表, 图片和subframes的加载.
设置为 eager 时, Selenium WebDriver保持等待, 直至返回 DOMContentLoaded 事件.
none
设置为 none 时, Selenium WebDriver仅等待至初始页面下载完成.



cookies设置：
get_cookies()
delete_all_cookes()
add_cookie()



选项卡操作：
通过执行js命令实现新开选项卡window.open()
不同的选项卡是存在列表里browser.window_handles
通过browser.window_handles[0]就可以操作第一个选项卡




# from selenium库 import webdriver


# from selenium库.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("http://")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()





#
# dr = webdriver.Chrome()
#
# dr.get('https://www.baidu.com/')
# print(dr.session_id)
# print(dr.command_executor)
# print(dr.current_url)
#
# inp = dr.find_element_by_id('kw')
# searcH_button = dr.find_element_by_id('su')
# inp.send_keys('python')
# searcH_button.click()
#
# time.sleep(10)
# dr.quit()
