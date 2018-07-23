# encoding: utf-8

from selenium import webdriver
import random,time,os
from fash_tech_end.lee_selenium import Lee

class GoodsDetails(Lee):

    '''标准码定位器'''
    goods_name_loc=("css selector",".product-details>dl>dt:nth-child(2)")

    goods_price_loc=("css selector","#pro_price")

    goods_size_loc=("css selector",".standard-size>dt")

    add_cart_button=("css selector",".product-details>dl>dt:nth-child(12)>button")

    '''量身尺码定位器'''

    #量身尺码
    click_liangshen_size=("css selector","#sizedata")

    chooes_liangshen_size=("class name","ckSize")

    chooes_liangshen_button=("css selector",".submit>button")

    '''购物车的商品价格于名称'''

    cart_goods_name = ("css selector", ".goods-info>h4>a")

    cart_goods_price = ("css selector", ".cart-ckbox>input:nth-child(1)")

    #商品名称

    # def get_goods_name_(self,n=0):
    #     result=self.find_elements(self.cart_goods_name)
    #     result[n].get_attribute("price")
    #
    # def get_goods_name(self):
    #     self.get_goods_name_(n=-1)
    #
    # def get_goods_price_(self,n=0):
    #     result=self.find_elements(self.cart_goods_price)
    #     result[n].text()
    #
    # def get_goods_price(self):
    #     self.get_goods_price_(n=-1)


    #点击量身尺码

    def click_liangshen(self):
        self.click(self.click_liangshen_size)
    #选择尺码
    def chooes_liangshen(self):
        number = random.randint(0, 10)
        # number=self.random_randint(self.chooes_liangshen_size)
        print(number)

        self.clicks(self.chooes_liangshen_size,number)

        self.clicks(self.chooes_liangshen_button,number)

    def goods_biaozhui_size(self):
        elements = self.find_elements(self.goods_size_loc)

        number = random.randint(0, (len(elements) - 1) // 2)

        self.clicks(self.goods_size_loc,number)

    def click_addcar_button(self):
        self.click(self.add_cart_button)

    def goods_name(self):
        self.find_element(self.goods_name_loc).text()

    def goods_price(self):
        self.find_element(self.goods_price_loc).text()


    #操作方法
    def chooes_goods(self):

        #量身尺码
        result_01 = self.is_element_exist("#sizedata")
        #标准尺码
        result_02 = self.is_element_exist(".standard-size>dt")

        if result_01:
            self.click_liangshen()

            self.chooes_liangshen()

            self.click_addcar_button()


        elif result_02:
            self.goods_biaozhui_size()

        self.click_addcar_button()












