from icalendar import Calendar, Event
import urllib2

'''
	Parses .ics files retrived from www.kayaposoft.com
'''
class IcsParser:

	'''Constructor for IcsParser'''
	def __init__(self):
		self.icsFile = None
		self.url = 'http://www.kayaposoft.com/enrico/ics/v1.0?country=%s&fromDate=01-01-%s&toDate=31-12-%s'

	'''
		Method getIcs
		Parameters:
			country: string, e.g. 'isl', 'eng', 'usa'
			fromYear: string from 01-01, e.g. '2014', '2015'
			toYear: string to 31-12, e.g. '2015', '2016'
		Returns: dictionary {'holidayName': vText('example'), 'holidayDate': datetime.date(2014, 12, 25)}
	'''
	def getIcs(self, country, fromYear, toYear):
		self.__downloadFile__(country, fromYear, toYear)
		return self.__parseToDictionary__()

	'''
		Private method __downloadFile__
		self.icsFile is the downloaded file
	'''
	def __downloadFile__(self, country, fromYear, toYear):
		response = urllib2.urlopen(self.url % (country, fromYear, toYear))
		self.icsFile = response.read()
		response.close()

	'''
		Private method __parseToDictionary__
		parses .ics file to list of holidays
		Returns: list of dictionary {'holidayName': vText('example'), 'holidayDate': datetime.date(2014, 12, 25)}
	'''
	def __parseToDictionary__(self):
		if self.icsFile is not None:
			result = []
			gcal = Calendar.from_ical(self.icsFile)
			for component in gcal.walk():
				if component.name == "VEVENT":
					result.append({'holidayName': component.get('summary'), 'holidayDate': component.get('dtstart').dt.strftime("%Y-%m-%d %H:%M:%S")})
		
		return result

if __name__ == '__main__':
	parser = IcsParser()
	print parser.getIcs('isl', '2014', '2014')
	print parser.getIcs('isl', '2014', '2014')