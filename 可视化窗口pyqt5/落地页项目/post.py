# flask
import os
from flask import Flask, request,jsonify
from flask_cors import *
app_ = Flask(__name__)
import json
CORS(app_, supports_credentials=True)
@app_.route('/test', methods=["POST"])
class get_post(object):
    def calculate():
        params = request.form if request.form else request.json
        newData = [];
        for data in params:
            a = json.loads(params[data])
            newData.append(a)
        b = json.dumps(newData)
        f = open('../indor.txt', "w")
        f.write(b)
        f.close
        return jsonify(content_type='app_lication/json;charset=utf-8',
                       reason='success',
                       charset='utf-8',
                       status='200')
    def get_post_run(self):
        app_.run(host='0.0.0.0',
                 threaded=True,
                 debug=True,
                 port=8080)



