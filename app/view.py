
from flask import request
from app import app
from app.timetable import my_timetable
from flask import Flask

@app.route('/udsm-timetable', methods = ['POST'])
def getTimetable():

	raw = request.json['data']
	cd  = raw['formrows']
	codes = []
	for i in cd:
		codes.append(i.upper().replace(' ', ''))

	#codes = ['CL111', 'CS174', 'DS112', 'ES173', 'ME101', 'MT161']
	
	data = my_timetable(codes)
	print(data)
	
	return {'data':data, 'codes':codes}

@app.route('/', methods = ['GET'])
def testTimetable():

	codes = ['CL111', 'CS174', 'DS112', 'ES173', 'ME101', 'MT161']
	
	data = my_timetable(codes)
	print(data)
	
	return {'data': data, 'codes': codes}
	



app = Flask(__name__)
