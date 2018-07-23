# encoding: utf-8

from selenium import webdriver
from fash_tech_end.lee_selenium import Lee
import random,time,os

class ShopClassifiy(Lee):
    move_stop=("link text","商城")

    zhaoshang=("link text","招商合作")

    my_account=("link text","我的账户")

    my_favourite=("xpath","//*[@class='top-menu']/ul/li[3]/a")

    my_cart=("xpath","//*[@id='sizeTotal']")

    my_home_page=("class name","web-font ft-logo")

    shop_name = ("css selector", ".product-title>h5>a")

    shop_price=("css selector",".product-title>h5>em")

    goods = ["女装", "新款上市"]




    def click_classifiy(self):
        self.move_to_element(self.move_stop)

    def choose_classifiy(self):
        t = random.choice(self.goods)

        goods_type = ("link text", t)
        self.click(goods_type)

    def choose_shop(self):
        suijishu = self.random_randint(self.shop_name)

        self.clicks(self.shop_name, suijishu)


    def choose_shop_text(self):
        pass

    def choose_shop_price(self):
        pass

    # 操作方法
    def choose_shop_method(self):
        self.click_classifiy()
        self.choose_classifiy()
        self.choose_shop()







