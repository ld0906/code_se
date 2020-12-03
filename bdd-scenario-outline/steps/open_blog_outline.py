from behave import given,when,then
from selenium import webdriver

@given('I put a link "{url}" to browser address bar and then click Enter key')
def step_given_get_blog_url(context,url):
    context.driver = webdriver.Firefox()
    context.driver.get(url)


@when('wait for page loads done')
def step_impl_1(context):
    pass


@then('there will be keyword "{keywords}" in http response')
def step_impl_assert(context,keywords):
    assert keywords in context.driver.page_source
