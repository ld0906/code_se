from behave import given,when,then

@given('string details as below')
def str_test(context):
    context.str1 = context.text


@when('string text length is calculated')
def str_test(context):
    context.len1 = len(context.str1)

@then('length should be "{len2}"')
def str_test(context,len2):
    assert int(len2) == context.len1