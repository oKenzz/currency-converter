from flask import jsonify, Blueprint, redirect, render_template, request
import requests
import backend
routes = Blueprint(__name__, "server")

#openexchange api url
# url="https://openexchangerates.org/api/latest.json?app_id=appID"

baseValue = 0
rate = 0

@routes.route('/',methods=["POST", "GET"])
def home():
    global baseValue
    global rate
    newValue = 0
    print(request.form)
    if request.method=="POST":
        if 'baseValue' in request.form:
            baseValue = request.form['baseValue']
            newValue = backend.convertCurrency(baseValue, rate)
        elif 'rate' in request.form:
            rate = request.form['rate']
    return render_template("index.html", newValue=newValue)