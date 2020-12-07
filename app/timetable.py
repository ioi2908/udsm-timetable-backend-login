from bs4 import BeautifulSoup 
from urllib.request import urlopen
#from selenium import webdriver
#from selenium.webdriver import FirefoxOptions
import app.organizer as organizer
from app import basedir
import json
import os

url = 'https://timetable.udsm.ac.tz/'
#frame = 'resource'
#opts = FirefoxOptions()
#opts.add_argument("--headless")

#codes = ['DS112', 'ES101', 'ES115', 'ES102', 'MT100', 'MT127']

data = {}

'''

def hrefs():

	try:
		driver = webdriver.Firefox(firefox_options=opts)
		print('no browser will show')
	except:
		driver = webdriver.Firefox()
		print('browser openning')

	driver.get(url)

	driver.switch_to.frame(frame)

	html = driver.page_source

	soup = BeautifulSoup(html, 'lxml')

	links = soup.find_all('a')

	print('Got '+ str(len(links)) + ' links')

	data = {}
	req_href = ''
	for link in links:
		data[link.text] = link.get('href')
	print('data is ready for storage')
	return data

def store_hrefs():

	data = hrefs()

	with open('hrefs.txt', 'w') as hr:
		print('storing data ...')
		json.dump(data, hr)

	return 'stored in hrefs.json'

'''

def get_hrefs():
	'''
	try:
		with open('hrefs.txt', 'r') as hr:
			print('opennig file')
			data = json.load(hr)
			print('loaded data ...')
			return data
	except IOError:
		store_hrefs()
		get_hrefs()
		resource(code)
	'''

	with open(os.path.join(basedir, 'hrefs.txt'), 'r') as hr:
		print('opennig file')
		data = json.load(hr)
		print('loaded data ...')
		return data

def check_code(code):

	data = get_hrefs()
	score = 0
	for i in data.keys():
		if code == i:
			score = score + 1

	if score == 0:
		return False
	else:
		return True


def resource(code):

	code  = str(code)

	if check_code(code) == False:
		return str(code) + " doesn't exist"

	try:
		data = get_hrefs()
	except:
		return 'no data'

	if data:

		for i in data.keys():

			if i == code:
				req_href = data[i]

			else:
				pass

		page = urlopen(url+req_href)

		s_ = BeautifulSoup(page, 'lxml')

		trs = s_.find_all('tr')

		print(len(trs[2:]))

		table = {}

		for i in trs[2:]:
			try:
				tds = i.find_all('td')
				length = len(tds)
				day_table = []
				t =[]
				for td in tds:
					t.append(td.text.replace('\n','').replace('\r','').replace('\xa0',''))

				try:
					if i.th.text.replace('\n','') != '':
						table[i.th.text.replace('\n','')] = [t]
				except:	
					target = table.keys()
					tar_ = []
					for v in target:
						tar_.append(v)
					table[tar_[-1:][0]].append(t) 
			except:
				continue

		return table
				

def create_timetable(codes):

	promise = {
		'MONDAY':[],
		'TUESDAY':[],
		'WEDNESDAY':[],
		'THURSDAY':[],
		'FRIDAY':[]
	} 

	for code in codes:
		t = resource(code)
		if type(t) == str:
			return t 
		t_keys = [i for i in t.keys()]

		mon = t[t_keys[0]]
		tue = t[t_keys[1]]
		wed = t[t_keys[2]]
		thu = t[t_keys[3]]
		fri = t[t_keys[4]]

		promise['MONDAY'].append(mon)
		promise['TUESDAY'].append(tue)
		promise['WEDNESDAY'].append(wed)
		promise['THURSDAY'].append(thu)
		promise['FRIDAY'].append(fri)

	timetable = {}

	for key in promise.keys():
		timetable[key] = organizer.analyzer(promise[key], codes)

		'''
	with open('timetable.txt', 'w') as tt:
		json.dump(timetable, tt)
		'''

	return timetable


def my_timetable(codes):

	'''
	try:
		filename = 'timetable.txt'
		with open(filename, 'r') as file:
			time_table = json.load(file)
	except:
		try:
			filename = create_timetable(codes)
			with open(filename, 'r') as file:
				time_table = json.load(file)
		except:
			return filename
	'''

	time_table = create_timetable(codes)

	return time_table

#print(json.dumps(my_timetable(), indent = 4))

