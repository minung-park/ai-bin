# -*- coding: UTF-8 -*-
# Copyright (c) 2020-present, Law & Company, Inc. All rights reserved.
# @author: Minyoung P
# @created: 2022-01-27
# @last_updated: 2022-01-27
# 아무런 역할을 하지않는 깡통 api 입니다. 중간 브릿지 역할만을 담당합니다.


from flask import Flask, request
import requests
from urllib.parse import urlencode
app = Flask(__name__)


@app.route("/api/call", methods=["POST"])
def api_post():
    data = eval(request.data)
    url = data.get('url', None)
    param = data.get('param', '')
    method = data.get('method', 'POST')
    if not url:
        return None, 400

    if method == 'POST':
        resp = requests.post(url, data=param)
    elif method == 'GET':
        query_string = urlencode(param)
        resp = requests.get(f'{url}?{query_string}')

    return resp.text, resp.status_code
