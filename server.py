from flask import Flask, jsonify
from parse_ical import IcsParser
from parse_html import HtmlParser
from cache_function import memorize
import time

icsParser = IcsParser()
htmlParser = HtmlParser()

baseUrl = "/api"
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route(baseUrl + "/holidays/<language>/<fromYear>/<toYear>")
def holidays(language, fromYear, toYear):
	return jsonify(result=getHolidays(language, fromYear, toYear))

@app.route(baseUrl + "/countries")
def countries():
	return jsonify(result=getCountries())

@memorize
def getHolidays(language, fromYear, toYear):
	return icsParser.getIcs(language, fromYear, toYear)

@memorize
def getCountries():
	return htmlParser.getCountries()

if __name__ == "__main__":
    app.run()