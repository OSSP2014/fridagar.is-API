from flask import Flask, jsonify, abort
from flask.ext.cors import cross_origin
from flask.ext.cache import Cache
from flask.ext.autodoc import Autodoc
from parse_ical import IcsParser
from parse_html import HtmlParser

icsParser = IcsParser()
htmlParser = HtmlParser()

baseUrl = '/api'
app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
auto = Autodoc(app)

oneMonth = 60*60*24*30

@app.route('/')
def hello():
	return auto.html()

@app.route(baseUrl + '/holidays/<country>/<fromYear>/<toYear>')
@auto.doc()
@cross_origin()
def holidays(country, fromYear, toYear):
	'''
		Get holidays for specified country and period
	'''
	try:
		return jsonify(result=getHolidays(country, fromYear, toYear))
	except:
		abort(400)

@app.route(baseUrl + '/countries')
@auto.doc()
@cross_origin()
def countries():
	'''
		Get all supported countries
	'''
	try:
		return jsonify(result=getCountries())
	except:
		abort(400)

@cache.memoize(oneMonth)
def getHolidays(country, fromYear, toYear):
	return icsParser.getIcs(country, fromYear, toYear)

@cache.memoize(oneMonth)
def getCountries():
	return htmlParser.getCountries()

if __name__ == '__main__':
    app.run(debug=True)