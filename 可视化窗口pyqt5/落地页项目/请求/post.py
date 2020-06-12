# flask
import os
from flask import Flask, request,jsonify
from flask_cors import *
app_ = Flask(__name__)
import json
CORS(app_, supports_credentials=True)
@app_.route('/test', methods=["POST"])
def calculate():
    params = request.form if request.form else request.json
    # a = params.get(0)
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


if __name__ == '__main__':
    app_.run(host='0.0.0.0',
            threaded=True,
            debug=True,
            port=8080)
