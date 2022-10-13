# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Eemail_163():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'https://www.baidu.com'

    def test_163(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.baidu.com')
        source=driver.page_source   # 网站源码
        print("source %s" %source )
        driver.find_element_by_id('kw').clear()
        time.sleep(0.5)  #  等待一下，否则输入框中的文本可能不会被清楚
        driver.find_element_by_id('kw').send_keys(u'163邮箱登录')

        # 点击搜索的方式：可以直接回车，也可以点击搜索按钮
        # driver.find_element_by_id('su').click()   # send_keys(Keys.RETURN)
        # driver.find_element_by_id('su').send_keys(Keys.RETURN)   # send_keys(Keys.RETURN)
        driver.find_element_by_id('su').send_keys(Keys.ENTER)  # send_keys(Keys.RETURN)

        # 这个一定要注意延迟。
        time.sleep(1)

        # driver.find_element_by_link_text(u"163网易免费邮").click()
        # driver.find_element_by_xpath('//*[@id="1"]/h3/a')
        driver.find_element_by_link_text(u"163网易免费邮--中文邮箱第一品牌_163邮箱").click()
        # driver.find_element_by_css_selector('div>h3>a').click()

        #页面等待的实现方式。
        wait=WebDriverWait(driver,5)
        wait.until()

        time.sleep(3)

        # 切换窗口
        window = driver.window_handles
        driver.switch_to_window(window[-1])

        # 切换iframe
        frame = driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
        driver.switch_to.frame(frame)

        # 发送账户密码
        driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input[1]").send_keys('lincappu')
        driver.find_element_by_name('password').send_keys('lin111www555')

        # driver.find_element_by_id('un-login').click()
        # driver.find_element_by_id('un-login').send_keys(Keys.SPACE)

        # 点击登录
        driver.find_element_by_id('dologin').click()

        # driver.refresh()
        time.sleep(3)
        driver.quit()


        # 关闭窗口，然后跳转到上一个窗口， 比如说当详情页处理完成时要关闭这个页面，然后调回列表页
        self.driver.execute_script("window.close()")
        self.driver.switch_to.window(self.driver.window_handles[0])


        # selenium库 + lxml 配合
        source = driver.page_source  # 网站源码
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)


# https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=%2F%2Fmimg.127.net%2Fp%2Ffreemail%2Findex%2Funified%2Fstatic%2F2020%2F%2Fcss%2F&cf=urs.163.4944934a.css&MGID=1592478725535.6064&wdaId=&pkid=CvViHzl&product=mail163




# if __name__ == '__main__':
#     email_163 = Eemail_163()
#     email_163.setUp()
#     email_163.test_163()

# 无头浏览器
driver=webdriver.PhantomJS()
driver.get('http://www.baidu.com')
print(driver.page_source)


