# encoding: utf-8

import random,time,os
from fash_tech_end.lee_selenium import Lee
from fash_tech_end.my_log import Log

logger=Log()

class ComfirmOrder(Lee):
    '''定位器'''

    Change_address_loc=("link text","更改")

    Add_new_address_loc=("link text","使用新地址")

    Add_gift_code_loc=("css selector",".left>input")

    Add_gift_button_loc=("css selector",".right>button")

    Payment_method_loc=("css selector",".label-list>label>input")

    Pay_now_loc=("css selector","#sub")

    Payment_succes_loc=("link text","已完成付款")

    Payment_fail_loc=("link text","付款遇到问题")

    Order_no_loc_1=("css selector",".commodity-message-row>span:nth-child(1)")
    Order_no_loc_2=("css selector",".pay-style>p>span")
    Order_no_loc_3=("css selector",".order_main>p:nth-child(2)")

    #操作方法

    def Payment_method(self):

        self.js_scoll_end()

        number=self.random_randint(self.Payment_method_loc)
        print(number)
        self.clicks(self.Payment_method_loc,number)



        #获得支付的订单号
        if number==0:
            self.click(self.Pay_now_loc)
            all_h = self.driver.window_handles
            self.driver.switch_to.window(all_h[1])
            order_no=self.find(self.Order_no_loc_1).text
            jubin = self.driver.title
            logger.info("--------支付页面的句柄：%s-----------" % jubin)
            logger.info("------打印支付订单号:%s--------" % order_no)
            self.driver.switch_to.window(all_h[0])
            
        elif number==1:
            self.click(self.Pay_now_loc)
            all_h = self.driver.window_handles
            self.driver.switch_to.window(all_h[1])
            order_no = self.find(self.Order_no_loc_2).text
            jubin = self.driver.title
            logger.info("--------支付页面的句柄：%s-----------" % jubin)
            logger.info("------打印支付订单号:%s--------" % order_no)
            self.driver.switch_to.window(all_h[0])

        elif number==2:
            self.click(self.Pay_now_loc)
            all_h = self.driver.window_handles
            self.driver.switch_to.window(all_h[1])
            order_no = self.find(self.Order_no_loc_3).text
            jubin = self.driver.title
            logger.info("--------支付页面的句柄：%s-----------" % jubin)
            logger.info("------打印支付订单号:%s--------" % order_no)
            self.driver.switch_to.window(all_h[0])

    def Pay_now(self):

        self.click(self.Pay_now_loc)

    def Payment_succes(self):
        self.click(self.Payment_succes_loc)
