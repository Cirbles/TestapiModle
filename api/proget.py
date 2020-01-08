# -#- coding:utf-8 -*-
# @Time:2019/11/30上午11:24
# @Author:liguangchun
# @File:proget.py
from flask import Flask
import json

app = Flask(__name__)

@app.route('/test')
def helloWorld():
    return "Hello world!!!"


if __name__ == '__main__':
    app.run(debug=True)