import requests
import json
#import sys

#sys.path.append("/api-automation/helpers")


def hitgetApi(r, url):
    print("---API Get method call---")
    if r == "get":
        r1 = requests.get(url)
        #print(r1.status_code)
        r1_get = r1.text
        json_fresponse = json.loads(r1_get)
        #print(r1.text)
    else:
        print("Please correct your details")
    return json_fresponse


def hitpostApi(e, ulr2, data):
    print("---API Post method call---")
    if e == "post":
        e1 = requests.post(ulr2, data=data)
        print(e1.status_code)
        post_res = e1.text
        print(post_res)
    else:
        print("Your method call is incorrect.")
    return post_res
