from behave import *


# use_step_matcher("re")


@given("the system is running")
def step_impl(context):
    pass

@when("a User visits the Landing Page")
def step_impl(context):
    context.browser.get(context.address)
    context.response = context.browser.page_source

@then('"{text}" is returned to the User')
def step_impl(context, text):
    if text not in context.response:
        fail('%r not in %r' % (text, context.response))

