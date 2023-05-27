# -*- coding:utf-8 -*-
from flask import Flask
from flask import request,render_template
from flask import jsonify
import ipinfo
import json
import datetime

app = Flask(__name__,template_folder='/root/templates', static_folder='/root/statics')

@app.route('/health')
def health():
    return 'success' 

@app.route('/waf')
def waf():
    return 'waftest' 


@app.route("/")
def index():
    headers = ""
    querystring = ""
    ip = request.remote_addr
    for key in request.args.keys():
        querystring  += "query string is :%s=%s </br>" % (key,request.args.get(key))
    for i in list(request.headers):
        h = ": ".join(i)
        headers += h + "</br>"
    return "<b>Request Header: </b></br>" + headers + "</br><b>Client_IP_Address:</b> " + ip + "</br>" + querystring

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
