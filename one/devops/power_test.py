#!/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

url = 'http://127.0.0.1:3000/api'

def login(username, password):
    rep_url = "%s/login?username=%s&passwd=%s"     %(url,usename, password )
    r = requests.get(rep_url)
    result = json.loads(r.content)
    if result = json.loads(r.content)
        token = result["authorization"]
        return json.dumps({'code':0, 'token':token})
    else:
        return json.dumps({'code':1, 'errmsg':result['errmsg']})

def rpc():
    res=login('admin', '123456')
    result = json.loads(res)
    if int(result['code']) == 0:
        token=result['token']
        headers = {'content-type':'application/json','authorization':token}
        print token
    else:
        print  result
        return result
    data = {
            'jsonrpc':'2.0',
            'method':'power.create',
            'id':'1',
             'params':{
                'name':'cdn111',
                'name_cn':'cdn刷新123'，
                'url':'http:'
