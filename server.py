from flask import Flask, jsonify, abort
from flask.ext.cors import cross_origin
from flask.ext.cache import Cache
from parse_ical import IcsParser
from parse_html import HtmlParser

icsParser = IcsParser()
htmlParser = HtmlParser()

baseUrl = '/api'
app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

oneMonth = 60*60*24*30

@app.route('/')
def hello():
	return 'Hello World!'

@app.route(baseUrl + '/holidays/<language>/<fromYear>/<toYear>')
@cross_origin()
def holidays(language, fromYear, toYear):
	try:
		return jsonify(result=getHolidays(language, fromYear, toYear))
	except:
		abort(400)

@app.route(baseUrl + '/countries')
@cross_origin()
def countries():
	try:
		return jsonify(result=getCountries())
	except:
		abort(400)

@cache.memoize(oneMonth)
def getHolidays(language, fromYear, toYear):
	return icsParser.getIcs(language, fromYear, toYear)

@cache.memoize(oneMonth)
def getCountries():
	return htmlParser.getCountries()

if __name__ == '__main__':
    app.run(debug=True)