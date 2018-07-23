# encoding: utf-8

from fash_tech_end.lee_selenium import Lee
from selenium import webdriver
import unittest

class LoginPage(Lee):
    '''登录页面元素--定位器'''
    email_loc = ("link text", "邮箱登录")  # 邮箱登录

    input_un = ("name", "username")  # 输入账号

    input_psw = ("name", "password")

    login_but = ("css selector", "#login-btn")

    forget_psw = ("css selector", ".one>h5>a")  # 忘记密码

    my_account = ("link text", "我的账户")


    def click_email_sub(self):
        '''点击邮箱登录'''
        self.click(self.email_loc)

    def input_username(self,un):
        '''输入账号框'''

        self.send_keys(self.input_un,un)

    def input_passward(self,psw):
        '''输入密码框'''

        self.send_keys(self.input_psw,psw)

    def click_sub(self):
        '''登录按钮'''
        self.clicks(self.login_but,1)

    def click_forget_pw(self):
        '''忘记密码'''
        self.click(self.forget_psw)

    #登录方法
    def login_case(self,un,psw):
        '''login case method'''

        self.click_email_sub()

        #第一步：输入账号
        self.input_username(un)

        #第二步：输入密码
        self.input_passward(psw)

        #第三步：点登录按钮
        self.click_sub()

    # 登录方法
    def login_case_f(self,un,psw):
        # 第一步：输入账号
        self.input_username(un)

        # 第二步：输入密码
        self.input_passward(psw)

        # 第三步：点登录按钮
        self.click_sub()


























