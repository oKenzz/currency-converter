import json
from flask import jsonify, Blueprint, redirect, render_template, request
import requests
import backend
routes = Blueprint(__name__, "server")

#openexchange api url
# url="https://openexchangerates.org/api/latest.json?app_id=appID"

baseValue = 0
rate = 0
currency=""

@routes.route('/',methods=["POST", "GET"])
def home():
    global baseValue
    global rate
    global currency
    newValue = 0
    print(request.form)
    if request.method=="POST":
        if 'baseValue' in request.form:
            baseValue = request.form['baseValue']
            newValue = backend.convertCurrency(baseValue, rate)
        elif 'rate' in request.form:
            data = json.loads(request.form['rate'])
            rate = data['rate']
            currency = data['currency']
    return render_template("index.html", newValue=newValue, currency=currency)