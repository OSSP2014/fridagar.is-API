from flask import Flask, jsonify
from parse_ical import IcsParser
from cache_function import memorize
import time

parser = IcsParser()

baseUrl = "/api"
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route(baseUrl + "/holidays/<language>/<fromYear>/<toYear>")
def getHolidays(language, fromYear, toYear):
	return jsonify(result=callParser(language, fromYear, toYear))

@memorize
def callParser(language, fromYear, toYear):
	return parser.getIcs(language, fromYear, toYear)

if __name__ == "__main__":
    app.run()