from behave import *


@given(u'Precondition behave installed and perform its operation')
def step_impl(context):
   print("I am run from given")


@when(u'Run feature file with  the behave')
def step_impl(context):
    print("I am run from WHEN STATEMENT")

@then(u'it should run successfully')
def step_impl(context):
    print("I am run from THEN STATEMENT")

@then(u'it should run successfully from different file setup')
def step_impl(context):
  print("This is testing THEN statement in two different feature file but step class is same. Thanks for executing me")


## from command line, you can use the following:
## --no-capture for any stdout output to be printed immediately.
## --no-capture-stderr for any stderr output to be printed immediately.