from behave import *
from helper import CRUD
import jsonpath

@given(u'user find the get api url')
def step_impl(context):
    context.a = CRUD.hitgetApi("get", "https://reqres.in/api/users?page=2")

@when(u'user hit get api url')
def step_impl(context):
    #context.json_response = json.load(context.a)
    print(context.a)

@then(u'user should  see the response json format')
def step_impl(context):
    #print("This is passed")
    fsntname = jsonpath.jsonpath(context.a, 'total')
    print(fsntname[0])



