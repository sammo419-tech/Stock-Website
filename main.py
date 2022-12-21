from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import json

ticker = "SPY"
api_key = "43620a19078c459ea22098c6bddae06d"
key = "BB7126AAA54D46E596083321E7C43BF7"

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='home')

@app.route("/markets", methods=['GET'])
def markets():
    url = f"https://api.twelvedata.com/quote?symbol={ticker}&apikey={api_key}"
    response = requests.get(url).json()
    return render_template('markets.html', response=response)

@app.route("/government")
def government():
    url = f"https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json"
    response = requests.get(url).json()
    # test = sorted(response, key=lambda response: response['disclosure_year'], reverse=True)
    return render_template('government.html', response=response)

@app.route("/wallstreetbets")
def wallstreetbets():
    url = f"https://tradestie.com/api/v1/apps/reddit"
    response = requests.get(url).json()
    # test = sorted(response, key=lambda response: response['disclosure_year'], reverse=True)
    return render_template('wallstreetbets.html', response=response)








