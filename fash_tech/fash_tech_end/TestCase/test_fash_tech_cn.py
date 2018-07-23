# encoding: utf-8

import unittest
from object.page.Login_page_two import Login_lee,login_url
from fash_tech_end.my_log import Log
from selenium import webdriver
from fash_tech_end.pages.Login_Page import LoginPage
from fash_tech_end.pages.Shop_classifiy_Page import ShopClassifiy
from fash_tech_end.pages.Goods_details_Page import GoodsDetails
from fash_tech_end.pages.Cart_page import CartPage
from fash_tech_end.pages.Comfirm_order_page import ComfirmOrder
from fash_tech_end.pages.Order_list import Orderlist
import time

logger=Log()

class Login_test(unittest.TestCase):
    '''登录页面的case'''

    @classmethod
    def setUpClass(cls):

        logger.info("------start driver-------")

        # self.driver = webdriver.Firefox()
        cls.driver = webdriver.Firefox()
        cls.login = LoginPage(cls.driver)
        cls.chooes_goods=ShopClassifiy(cls.driver)
        cls.add_cart=GoodsDetails(cls.driver)
        cls.submit=CartPage(cls.driver)
        cls.comfirm_order=ComfirmOrder(cls.driver)
        cls.get_order=Orderlist(cls.driver)

        cls.driver.get(login_url)


    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

        logger.info("------close driver------")

    @unittest.skip('暂时跳过用例的测试')
    def test_login01(self):
        '''输入错误的账号密码'''
        logger.info("----------输入错误的账号密码---------")

        try:
            self.login.login_case("1037791044@qq.com","asdasd43434")
            # 测试结果，判断是否登录成功
            my_account = ("link text", "我的账户")
            result = self.login.is_text_in_element(my_account, "我的账户")

            # 第五步：期望结果
            self.assertEqual(result, False)

        except Exception as e:
            logger.critical("----------执行异常--------%s"%e)

    # @unittest.skip('暂时跳过用例的测试')
    def test_02(self):
        '''输入正常的账号密码'''
        logger.info("----------输入正常的账号密码---------")
        try:
            self.login.login_case("1037791044@qq.com","asd123")
            # 测试结果，判断是否登录成功
            my_account = ("link text", "我的账户")
            result = self.login.is_text_in_element(my_account, "我的账户")

            # 第五步：期望结果
            self.assertEqual(result,True)

        except Exception as e:
            logger.critical("----------执行异常--------%s"%e)

    # @unittest.skip('暂时跳过用例的测试')
    def test_03(self):
        '''1，选择分类，2，随机选择商品'''
        logger.info("----------选择商品---------")
        try:
            self.chooes_goods.choose_shop_method()

        except Exception as e:
            logger.critical("----------执行异常--------%s"%e)

    # @unittest.skip('暂时跳过用例的测试')
    def test_04(self):
        '''判断商品类型（量身尺码or标准码）加入购物车'''
        logger.info("----------加入购物车---------")
        try:
            self.add_cart.chooes_goods()


        except Exception as e:
            logger.critical("----------执行异常--------%s"%e)

    @unittest.skip('暂时跳过用例的测试')
    def test_05(self):
        '''断言加入到购物车的商品名称价格是否正确'''
        try:
            goods_name_=self.add_cart.goods_name()
            goods_price_=self.add_cart.goods_price()
            cart_goods_name = ("css selector", ".goods-info>h4>a")
            cart_goods_price = ("css selector", ".cart-ckbox>input:nth-child(1)")

            result_01 = self.login.is_text_in_element(cart_goods_name[0], goods_name_)
            # result_02 = self.login.is_text_in_element(cart_goods_price[0], goods_price_)

            # 期望结果
            self.assertEqual(result_01, True)
            # self.assertIn(result_02,True)
        except Exception as e:
            logger.critical("----------执行异常--------%s"%e)
    def test_06(self):
        '''将添加到购物车的商品点击结算'''
        logger.info("----------点击结算---------")
        try:
            self.submit.submit_goods()

        except Exception as e:
            logger.critical("----------执行异常--------%s"%e)


    def test_07(self):
        '''确认订单页面，选择支付方式，点击支付'''
        logger.info("----------点击支付---------")
        try:
            self.comfirm_order.Payment_method()
            self.comfirm_order.Payment_succes()

            time.sleep(2)

        except Exception as e:
            logger.critical("----------执行异常--------%s"%e)


    def test_08(self):

        '''获得最新订单号'''

        self.get_order.get_order_no()


if __name__=="__main__":
    unittest.main()