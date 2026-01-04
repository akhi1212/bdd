# BDD API Tests with Python Behave

This repository contains a simple **BDD framework** using **Python + Behave** to test REST APIs.  
Scenarios are written in **Gherkin** under `Features/` and implemented as step definitions under `Features/Steps/`.


Getting Started

# bdd
prerequisite
pip install requests
pip install behave
pip install allure-behave

commands to run this framewrok 
 go to Feature folder in your cmd
 type  behave --tags=sampleAPIhit if you want to run single file
 if you want to run all feature file type behave



---

## Project Structure

```text
bdd/
├── Features/
│   ├── Steps/
│   │   ├── HealthCheckupbdd.py          # Basic Behave demo steps
│   │   ├── HealthCheckupbddSelenium.py  # API health‑check using requests
│   │   └── HealthcheckupAPI.py          # Additional API‑related steps
│   ├── helper/
│   │   └── CRUD.py                      # Helper methods for GET/POST using requests
│   ├── APISSetup.feature                # (Example) API setup scenarios
│   ├── BehaveFunctionalityCheck.feature # Feature to validate Behave setup
│   ├── HealthCheckup.feature            # Simple health‑check feature
│   └── HealthCheckupSecond.feature      # Second feature using same steps
├── behave.ini                           # Behave configuration (stdout/stderr capture)
├── README.md                            # Project documentation
└── .idea / __pycache__                  # IDE and cache files (can be ignored)

Example Feature and Steps
1. Sample Feature (Features/HealthCheckupSecond.feature)
text
Feature: This is second feature file to check setup of bdd framework

  Scenario: This is for second feature file to test bdd framework setup correctly
    Given This is to create url and hit it on the server
    When URL created and hitted in the server
    Then It should be created and hit it on the server.
2. Matching Steps (Features/Steps/HealthCheckupbddSelenium.py)
python
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
    context.actualcode = context.r.status_code
    expected = 200
    assert context.actualcode == expected
Given step: calls the API and stores response object in context.r.

When step: parses JSON and saves in context.json_response.

Then step: asserts the HTTP status code is 200.

3. Helper CRUD Module (Features/helper/CRUD.py)
python
import requests
import json

def hitgetApi(r, url):
    print("--- API Get method call ---")
    if r == "get":
        r1 = requests.get(url)
        r1_get = r1.text
        json_fresponse = json.loads(r1_get)
    else:
        print("Please correct your details")
        json_fresponse = None
    return json_fresponse

def hitpostApi(e, url2, data):
    print("--- API Post method call ---")
    if e == "post":
        e1 = requests.post(url2, data=data)
        print(e1.status_code)
        post_res = e1.text
        print(post_res)
    else:
        print("Your method call is incorrect.")
        post_res = None
    return post_res
This can be imported inside step files to avoid duplicating request logic.

behave.ini
behave.ini configures Behave’s output:

text
[behave]
stderr_capture=False
stdout_capture=False
Setting both to False makes Behave show print() output directly in the console (useful for learning).

Core Components
1. CRUD Helper (helpers/crudAPI.py)
Your crudAPI.py looks like:

python
import requests
import sys
sys.path.append("/api-automation/helpers")

def hitgetApi(r, url):
    print("--- API Get method call ---")
    if r == "get":
        r1 = requests.get(url)
        print(r1.status_code)
        r1_get = r1.text
        print(r1.text)
    else:
        print("Please correct your details")
        r1_get = None
    return r1_get

def hitpostApi(e, url2, data):
    print("--- API Post method call ---")
    if e == "post":
        e1 = requests.post(url2, data=data)
        print(e1.status_code)
        post_res = e1.text
        print(post_res)
    else:
        print("Your method call is incorrect.")
        post_res = None
    return post_res
hitgetApi("get", url) → performs a GET call and returns the raw response text.

hitpostApi("post", url, data) → performs a POST call with data payload and returns response text.

2. Configuration Helper (utility/Config.py)
You use it as:

python
from utility import Config
gurl = Config.readConfigData("APIDetails", "get_url")
Typical config.ini under configurations/ (example):

text
[APIDetails]
base_url = https://reqres.in
get_url = https://reqres.in/api/users?page=2
post_url = https://reqres.in/api/users
Adjust keys to match your actual implementation.

3. Example Scripts
scripts/getAPIHIT.py
python
import sys
from helpers import crudAPI
from utility import Config
import json
import jsonpath

gurl = Config.readConfigData("APIDetails", "get_url")

a = crudAPI.hitgetApi("get", gurl)

json_response = json.loads(a)
print(json_response)

x = jsonpath.jsonpath(json_response, 'total')
print(x)
assert x == 12
Reads GET URL from config.

Calls hitgetApi.

Parses JSON, extracts total using jsonpath, and asserts expected value.

scripts/postAPI1.py

Run 
python scripts/postAPI1.py
python scripts/test_001.py


Author
Akhilesh Gairola
QA Engineer – API & UI Automation (Python / Requests / Selenium)
This repository demonstrates a lightweight API automation setup without a test framework, suitable for learning and for explaining framework design in interviews.

