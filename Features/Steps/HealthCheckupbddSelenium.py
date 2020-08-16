from behave import *
import requests
import json



@given(u'This is to create url and hit it on the server')
def step_impl(context):
    context.r = requests.get("https://reqres.in/api/users")


@when(u'URL created and hitted in the server')
def step_impl(context):
    context.json_response = json.loads(context.r.text)
    print(context.json_response)



@then(u'It should be created and hit it on the server.')
def step_impl(context):
   context.actualccode = context.r.status_code
   expected = 200
   assert context.actualccode == expected

