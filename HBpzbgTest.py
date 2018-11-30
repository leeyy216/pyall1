import unittest
import django
from django.test import TestCase
from forms import ProductForm
import os,re

# from app.models import classname

# 页面传入服务器连接信息（信息接受正确/错误，存入数据库成功/失败）
class GetServerInfoTestCase(TestCase):
    def setUp(self):

# 连接服务器（连接成功/失败）
# 从服务器取参数（找文件成功/失败，从文件取参数成功/失败）
# 对比标准文件（对比目标参数成功/失败，反馈结果成功/失败）
# 修改服务器不符合的配置（修改成功/失败）


# 例子：测试myapp.models 中的 Animal 类相关的方法功能
class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

# 用 django.test.Client 的实例来实现 get 或 post 内容，检查一个网址返回的网页源代码
from django.test import Client
c = Client()
response = c.post('/login/', {'username': 'john', 'password': 'smith'})
print(response.status_code)     # 200
response = c.get('/customer/details/')
print(response.content)     # '<!DOCTYPE html...'

# 如果测试需要检查CSRF（默认禁用）
csrf_client = Client(enforce_csrf_checks=True)

# 指定浏览USER - AGENT:
c = Client(HTTP_USER_AGENT='Mozilla/5.0')

# 模拟post上传附件：
from django.test import Client
c = Client()

with open('wishlist.doc') as fp:
    c.post('/customers/wishes/', {'name': 'fred', 'attachment': fp})

# 测试网页返回状态：
from django.test import TestCase

class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/customer/details/')
        # 用self.client即可，不用client = Client()这样实例化，更方便
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)


# 还可以继承Client，添加一些其它方法
from django.test import TestCase, Client

class MyTestClient(Client):
    # Specialized methods for your environment
    ...

class MyTest(TestCase):
    client_class = MyTestClient

    def test_my_stuff(self):
        # Here self.client is an instance of MyTestClient...
        call_some_test_code()


# 定制self.client的方法：
from django.test import Client, TestCase

class MyAppTests(TestCase):
    def setUp(self):
        super(MyAppTests, self).setUp()
        self.client = Client(enforce_csrf_checks=True)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


# ###################--unitest_exp--###########################
def division_funtion(x, y):
    return x / y


class TestDivision(unittest.TestCase):
    def test_int(self):
        self.assertEqual(division_funtion(9, 3), 3)

    def test_int2(self):
        self.assertEqual(division_funtion(9, 4), 2.25)

    def test_float(self):
        self.assertEqual(division_funtion(4.2, 3), 1.4)


if __name__ == '__main__':
    unittest.main()