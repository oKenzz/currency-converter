from flask import jsonify, Blueprint, render_template, request
import requests
import backend
routes = Blueprint(__name__, "server")

#openexchange api url
# url="https://openexchangerates.org/api/latest.json?app_id=appID"

@routes.route('/',methods=["POST", "GET"])
def home():
    newValue = 0
    if request.method=="POST":
        baseValue = request.form['baseValue']
        newValue = backend.convertCurrency(baseValue)
    return render_template("index.html", newValue=newValue)