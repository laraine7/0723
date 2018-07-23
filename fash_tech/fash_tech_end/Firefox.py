# encoding: utf-8

from selenium import webdriver

class browser(object):
    def firefox(self):
        driver=webdriver.Firefox()
        driver.get("https://www.fash-tech.cn/member/login/")
        return driver