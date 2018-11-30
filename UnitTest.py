# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
# Created on 2016-7-27
# @author: Jennifer
# Project:使用unittest框架编写测试用例思路

# 3.导入unittest模块
import unittest
from unittest import TestCase,mock
import client
import requests
# import django
# from django.test import TestCase
# from forms import ProductForm
import os,re

# 测试函数
def function_divide(x, y):
    if function_isnum(x) and function_isnum(y):
        if function_iszero(x) and function_iszero(y):
            z = x / y
            return z
        else:
            return "one is zero, cant divide"
    else:
        return "one is not number, cant divide"

testvar = 3.14
teststr = "XiaoLee小李"
testbool = False

def function_iszero(x):
    if x == 0:
        return True
    else:
        return False

def function_isnum(x):

    if isinstance(x, int) or isinstance(x, float):
        return True
    else:
        return False


# 4.定义测试类，父类为unittest.TestCase。
# 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
# 可继承unittest.TestCase的各种断言方法。
class TestDoDivide(unittest.TestCase):
    # 5.定义setUp()方法用于测试用例执行前的初始化工作。
    # 注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
    # 注意，输入的值为字符型的需要转为int型
    def setUp(self):
        self.num1 = input('Enter a number:')
        self.num2 = input('Enter another number:')
        # self.number = int(self.number)

    # 6.定义测试用例，以“test_”开头命名的方法,最重要部分
    # 注意：方法的入参为self，可用unittest.TestCase类的各种断言方法判断测试结果，可定义多个测试用例
    @unittest.skip("must skipping")  # 必须跳过下面用例，相当少用
    def test_int(self):
        self.assertEqual(function_divide(self.num1, self.num2), False, msg="%s is not a num" % self.num1)

    @unittest.skip("must skipping")  # 必须跳过下面用例，相当少用
    def test_int2(self):
        self.assertEqual(function_divide(self.num1, self.num2), False, msg="%s is not a num" % self.num2)

    @unittest.skip("must skipping")  # 必须跳过下面用例，相当少用
    def test_float(self):
        self.assertEqual(function_divide(self.num1, self.num2), False, msg="3.14 is not a num")

    def test_success(self):
        success_send = mock.Mock(return_value=True)
        client.
        self.assertEqual(function_divide(self.num1, self.num2), False, msg="%s is not a num" % self.num1)

    def test_failure(self):
        self.assertEqual(function_divide(self.num1, self.num2), False, msg="%s is not a num" % self.num1)

    def tearDown(self):
        print ('Test over')


# from app.models import classname

# # 页面传入服务器连接信息（信息接受正确/错误，存入数据库成功/失败）
# class GetServerInfoTestCase(TestCase):
#     def setUp(self):
#
# # 连接服务器（连接成功/失败）
# # 从服务器取参数（找文件成功/失败，从文件取参数成功/失败）
# # 对比标准文件（对比目标参数成功/失败，反馈结果成功/失败）
# # 修改服务器不符合的配置（修改成功/失败）
#
#
# # 例子：测试myapp.models 中的 Animal 类相关的方法功能
# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")
#
#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')
#
# # 用 django.test.Client 的实例来实现 get 或 post 内容，检查一个网址返回的网页源代码
# from django.test import Client
# c = Client()
# response = c.post('/login/', {'username': 'john', 'password': 'smith'})
# print(response.status_code)     # 200
# response = c.get('/customer/details/')
# print(response.content)     # '<!DOCTYPE html...'
#
# # 如果测试需要检查CSRF（默认禁用）
# csrf_client = Client(enforce_csrf_checks=True)
#
# # 指定浏览USER - AGENT:
# c = Client(HTTP_USER_AGENT='Mozilla/5.0')
#
# # 模拟post上传附件：
# from django.test import Client
# c = Client()
#
# with open('wishlist.doc') as fp:
#     c.post('/customers/wishes/', {'name': 'fred', 'attachment': fp})
#
# # 测试网页返回状态：
#
# class SimpleTest(TestCase):
#     def test_details(self):
#         response = self.client.get('/customer/details/')
#         # 用self.client即可，不用client = Client()这样实例化，更方便
#         self.assertEqual(response.status_code, 200)
#
#     def test_index(self):
#         response = self.client.get('/customer/index/')
#         self.assertEqual(response.status_code, 200)
#
#
# # 还可以继承Client，添加一些其它方法
#
# class MyTestClient(Client):
#     # Specialized methods for your environment
#     ...
#
# class MyTest(TestCase):
#     client_class = MyTestClient
#
#     def test_my_stuff(self):
#         # Here self.client is an instance of MyTestClient...
#         call_some_test_code()
#
#
# # 定制self.client的方法：
# from django.test import Client, TestCase
#
# class MyAppTests(TestCase):
#     def setUp(self):
#         super(MyAppTests, self).setUp()
#         self.client = Client(enforce_csrf_checks=True)
#
#     def test_home(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#

# ###################--unitest_exp--###########################

# python -m unittest UnitTest
if __name__ == '__main__':
    unittest.main()