# encoding: utf-8

from fash_tech_end.lee_selenium import Lee
from fash_tech_end.my_log import Log

logger=Log()
class Orderlist(Lee):

    '''定位器'''
    Pay_data_loc=("xpath","//*[@class='list-detail']/li[2]/a/span[1]")
    Pay_order_loc=("xpath","//*[@class='list-detail']/li/a/span[2]")
    Pay_order_state_loc = ("xpath", "//*[@class='list-detail']/li/a/span[3]")

    # 操作方法

    def get_order_no(self):
        Pay_data=self.find(self.Pay_data_loc).text

        logger.info("----------------支付日期:%s-------------"%Pay_data)
        Pay_order=self.find_element(self.Pay_order_loc).text
        logger.info("----------------支付单号:%s-------------" % Pay_order)
        Pay_order_state=self.find_element(self.Pay_order_state_loc).text
        logger.info("----------------支付状态:%s-------------" % Pay_order_state)