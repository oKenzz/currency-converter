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
newValue = 0

@routes.route('/')
def home():
    # if (baseValue == 0 and rate == 0 and currency == "" and newValue == 0):
        return render_template("index.html")
    # return render_template("index.html", newValue=newValue, currency=currency)

@routes.route('/newValue', methods=['POST'])
def getNewValue():
    global baseValue
    baseValue = request.form['baseValue']
    return redirect('/updateData')

@routes.route('/rate', methods=['POST'])
def updateRate():
    global rate       
    global currency
    data = json.loads(request.form['rate'])
    rate = data['rate']
    currency = data['currency']
    return redirect('/updateData')

@routes.route('/updateData')
def updateData():
    global newValue
    newValue = backend.convertCurrency(baseValue,rate)
    return redirect('/')

@routes.route('/data')
def data():
    data = {"newValue": newValue, "currency": currency}
    return data