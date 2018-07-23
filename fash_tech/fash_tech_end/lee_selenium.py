# encoding: utf-8

from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *#导入所有异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from selenium import webdriver
import random
'''
基于原生的selenium框架做了二次封装

'''


def browser():
    driver = webdriver.Firefox()
    return driver

class Lee(object):



    def __init__(self,driver):
        """启动浏览器参数化，默认启动火狐"""
        self.driver=driver

    def open(self,url,t='',timeout=10):
        '''
        使用get打开url后，最大化窗口，判断title符合预期

        '''
        self.browser.get(url)
        # self.driver.maximize_window()
        try:
            WebDriverWait(self.driver,timeout,1).until(EC.title_contains(t))
        except TimeoutError:
            print("open%s title error"%url)
        except Exception as msg:
            print("Error:%s"%msg)
    def find_element(self,locator,timeout=10):
        '''定位元素，参数locator是元祖类型'''
        element=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        return element



    # def find_elements(self,locator,timeout=10):
    #     '''定位一组元素'''
    #     elements=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
    #     return elements

    def find_elements(self, loc, timrout=10, ):
        elements = WebDriverWait(self.driver, timrout, 1).until(lambda x: x.find_elements(*loc))
        return elements

    def find(self, loc, timrout=10, ):
        element = WebDriverWait(self.driver, timrout, 1).until(lambda x: x.find_element(*loc))
        return element


    def random_randint(self,loc):
        elements = self.find_elements(loc)
        sj = random.randint(0, len(elements) - 1)
        return sj

    def random_randint_juti(self,loc):
        elements = self.find_elements(loc)

        elements[self.random_randint(loc)].click()


    def click(self,locator):
        '''点击操作'''

        element=self.find_element(locator)
        element.click()

    def clicks(self,locator,n):
        elements=self.find_elements(locator)
        elements[n].click()

    def send_keys(self,locator,text):
        '''发送文本,清空后输入'''
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)

        # 判断元素是否存在
    def is_element_exist(self, css):
        s = self.driver.find_elements_by_css_selector(css)
        if len(s) == 0:
            # print("元素未找到:%s" % css)
            return False
        # elif len(s) == 1:
        #     return True
        else:
            # print("找到%s个元素:%s" % (len(s),css))
            return True




    def is_text_in_element(self,locator,text,timeout=10):
        '''判断文本在元素里，没定位到元素返回False,定位到返回判断结果布尔值'''
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
        except TimeoutException:
            # print("元素没定位到："+str(locator))
            return False
        else:
            return result
    def is_text_in_element01(self,locator,value,timeout=10):
        '''判断元素的value值，没定位到元素就返回Flase,定位到返回判断结果布尔值'''
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,value))

        except TimeoutException:
            # print("元素没定位到:"+str(locator))
            return False
        else:
            return result
    def is_title(self,title,timeout=10):
        '''判断title完全等于'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))
        return result

    def is_contains(self,title,timeout=10):
        '''判断title包含'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.title_contains(title))
        return result

    def is_selected(self,locator,timout=10):
        '''判断元素被选中，返回布尔值'''
        result=WebDriverWait(self.driver,timout,1).until(EC.element_located_to_be_selected(locator))
        return result
    def is_selected_be(self,locator,selected=True,timeout=10):
        '''判断元素的状态，selected是期望的参数True/False,返回布尔值'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))
        return result
    def is_alert_present(self,timeout=10):
        '''判断页面是否有alert
        有返回alert（注意这里是返回alert,不是True
        没有返回Flase'''

        result=WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())
        return result

    def is_visibility(self,locator,timeout=10):
        '''元素可见返回本身，不可见返回Fasle'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self,locaotr,timeout=10):
        '''元素可见返回本身，不可见返回True,没找到元素也返回True'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.invisibility_of_element_located(locaotr))
        return result

    def is_clickable(self,locator,timeout=10):
        '''元素可以点击is_enabled返回本身，不可点击返回FALSE'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self,locator,timeout=10):
        '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        element=self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        '''back to old window'''
        self.driver.back()

    def forward(self):
        '''forward to old window'''
        self.driver.forward()

    def close(self):
        '''close the window'''
        self.driver.close()

    def quit(self):
        '''quit the driver and close all the windows'''

        self.driver.quit()
    def get_title(self):
        '''获取title'''
        return self.driver.title


    def get_text(self,locator):
        '''获取文本'''
        element=self.find_element(locator)
        return element.text

    def get_attribute(self,locator,name):
        '''获取属性'''

        element=self.find_element(locator)
        return element.get_attribule(name)
    def js_execute(self,js):
        '''执行js'''
        return self.driver.execute_script(js)

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target=self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)
    def js_scoll_end(self):
        '''滚动到底部'''
        js = "var q=document.documentElement.scrollTop=10000"
        # self.driver.execute_script(js)
        # js="window.scollTop(0,document.boby.scollHeight)"
        self.driver.execute_script(js)
    def select_by_index(self,locator,index):
        '''通过索引，index是索引第几个，从0开始'''
        element=self.find_element(locator)
        Select(element).select_by_index(index)
    def select_by_value(self,locator,value):
        '''通过value属性'''
        element=self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
       ''' 通过文本值定位'''
       element=self.find_element(locator)
       Select(element).deselect_by_visible_text(text)

    def get_window_handle(self,locator):
        h=self.driver.current_wondow_handle
        print(h)
        self.click(locator)
        all_h=driver.window_handles
        print(all_h)



    #appium模拟手指滑动
    #上滑
    # 通过get_window_size函数获取尺寸
    def get_size(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return (x,y)
    def swipe_up(self,t=500,n=1):
        screen=self.get_size()
        for i in range(n):
            self.driver.swipe(screen[0]*0.5,screen[1]*0.75,screen[0]*0.5,screen[1]*0.25,t)

    # 下滑
    def swipe_down(self,t,n=1 ):
        screen=self.get_size()
        for i in range(n):
            self.driver.swipe(screen[0]*0.5,screen[1]*0.25,screen[0]*0.5,screen[1]*0.75,t)

    # 左滑
    def swipe_left(self,t,n=1):
        screen=self.get_size()
        for i in range(n):
            self.driver.swipe(screen[0]*0.75,screen[1]*0.5,screen[0]*0.25,screen[1]*0.5,t)

    # 右滑
    def swipe_right(self,t,n=1):
        screen=self.get_size()
        for i in range(n):
            self.driver.swipe(screen[0]*0.25,screen[1]*0.5,screen[0]*0.75,screen[1]*0.5,t)

    def is_toast_exist(driver, text, timeout=30, poll_frequency=0.5):
        '''is toast exist, return True or False
        :Agrs:
         - driver - 传driver
         - text   - 页面上看到的文本内容
         - timeout - 最大超时时间，默认30s
         - poll_frequency  - 间隔查询时间，默认0.5s查询一次
        :Usage:
         is_toast_exist(driver, "看到的内容")
        '''
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False


if __name__=="__main__":
    driver=browser()
    driver_n=Lee(driver)#返回类的实例：打开浏览器
    driver_n.open("https://www.baidu.com/")
    input_loc=("id","kw")
    print(driver_n.get_title())
    el=driver_n.find_element(input_loc)
    driver_n.send_keys(input_loc,"yoyo")































