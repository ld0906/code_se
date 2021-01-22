"""
Created by 2020/12/01
QQ: 2574674466
微信公众号：TimTest
"""

from behave import given,when,then
from selenium import webdriver

@given('在浏览器地址栏里输入网址 "{url}" 并点击回车键')
def step_given_get_blog_url(context,url):
    context.driver = webdriver.Firefox()
    context.driver.get(url)


@when('页面加载完毕')
def step_impl_1(context):
    pass


@then('页面会出现 "{keywords}" 字样')
def step_impl_assert(context,keywords):
    assert keywords in context.driver.page_source
