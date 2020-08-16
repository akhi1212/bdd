from behave import *


@given(u'Precondition behave installed and perform its operation')
def step_impl(context):
   print("I am runned from given")


@when(u'Run feature file with  the behave')
def step_impl(context):
    print("I am runned from given")

@then(u'it should run successfully')
def step_impl(context):
    print("I am runned from given")


## from command line, you can use the following:
## --no-capture for any stdout output to be printed immediately.
## --no-capture-stderr for any stderr output to be printed immediately.