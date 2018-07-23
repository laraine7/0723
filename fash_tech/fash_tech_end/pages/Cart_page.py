# encoding: utf-8

import random,time,os
from fash_tech_end.lee_selenium import Lee

class CartPage(Lee):
    '''定位器'''

    all_select_loc=("id","allChecked")

    single_election_loc=("css selector",".cart_column>div>input:nth-child(1)")

    all_delete_loc=("link text","删除全部")

    delete_loc=("link text","删除")

    submit_loc=("xpath","//*[@class='container check-shippingbag']/dd/input")

    def all_select(self):
        self.click(self.all_select_loc)

    def single_election(self):
        self.clicks(self.single_election_loc,-1)

    def submit(self):
        self.click(self.submit_loc)

    #操作方法
    def submit_goods(self):

        #滚动到底部
        # self.js_scoll_end()

        self.all_select()

        self.single_election()

        self.submit()




