# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import time

from selenium库 import webdriver
from selenium库.webdriver.common.by import By
from selenium库.webdriver.support import expected_conditions as EC
from selenium库.webdriver.support.ui import WebDriverWait


class Pengpaihao():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'https://www.thepaper.cn/pph_follow_search.jsp?pageType=1'

    def pengpai(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(url=self.base_url)

        name_list = []

        time.sleep(2)

        try:
            name = WebDriverWait(driver, 10, 0.5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "more_pph_pitem"))
            )
        finally:
            driver.quit()

        name = driver.find_elements_by_xpath('//a[starts-with(@href, "gov_")]/div[2]')
        for n in name:
            print(n.text)
            name_list.append(n)

        i = 1
        while (i < 28):
            next_button = driver.find_element_by_class_name('next_page')
            next_button.click()
            time.sleep(2)
            name = driver.find_elements_by_xpath('//a[starts-with(@href, "gov_")]/div[2]')
            for n in name:
                print(n.text)
                name_list.append(n)
            i += 1




        print(len(name_list))
        print(name_list)

        driver.quit()


# if __name__ == '__main__':
#     p = Pengpaihao()
#     p.setUp()
#     p.pengpai()


dic={
    '1':'2',
    '3':'4',
}
for k,v in enumerate(dic):
     print(k,v,dic[v])