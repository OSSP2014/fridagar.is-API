from bs4 import BeautifulSoup as bs
import urllib2

class HtmlParser:
	def __init__(self, url='http://holidays.kayaposoft.com/'):
		self.url = url

	def getCountries(self):
		htmlFile = self.__downloadFile__()
		return self.__parseToDictionary__(htmlFile)

	def __downloadFile__(self):
		response = urllib2.urlopen(self.url)
		html = response.read()
		response.close()
		return html

	def __parseToDictionary__(self, htmlFile):
		if htmlFile is not None:
			result = []
			soup = bs(htmlFile, from_encoding='utf8')
			tableRows = soup.select('table table tr')[1:]		# such style, many table
			for row in tableRows:
				tds = row.find_all('td')
				try:
					key = tds[2].text
					value = tds[1].text
					result.append({'countryKey' : key, 'countryName' : value})
				except IndexError:
					continue
		return result


if __name__ == '__main__':
	htmlParser = HtmlParser()
	print htmlParser.getCountries()