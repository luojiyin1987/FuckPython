#!/bin/env python
# -*- encoding: utf-8 -*-
from  __future__ import unicode_literals
import requests
import json
url = "http://127.0.0.1:3000/api"
#登陆并获取token
def login(username, password):
    req_url = "%slogin?username=%s&passwd=%s" %(url, username, password)
    r = requests.get(rep_url)
    result = json.loads(r.content)
    if result['code'] == 0:
        token = result["authorization"]
        return json.dumps({'code':0, 'token':token})
    else:
        return json.dumps({'code':1, 'errmsg':result['errmsg']})

def rpc():
    res = login('admin', '123456')
    result = json.loads(res)
    if int(result['code']) == 0:
        token = result['token']
        headers = {'content-type':'application/json','authorization':token}
        print token
    else:
        print  result
        return result
    

    
