
import json

#cominer function creates a 13 column long list from any entered list
def combiner(n):
	#create a 13 elements list
	cm = ["-" for i in range(13)]

	#inspect all elements of the entered list to see if they have a value
	for i in n:
		
		if i != '':
			got = i.split(' ')[1]
			ind = int(got[:11][:2]) - 7
			ind2 = int(got[:11].split('-')[1][:2]) - 7

			if int(got[:11].split('-')[1][3:]) == 55:
				ind2 = ind2 + 1

			typ = i.split(' ')[0].replace(',','').replace(' ','')
			time = i.split(' ')[1][:11]
			groups = i.replace(' ','').replace('Rooms',' ').replace('Groups',' ').split(' ')[2].replace(':','')
			room = i.split('Rooms')[1].split('Groups')[0][2:]

			cm[ind] = str(typ)+'<br>'+str(time)+'<br>'+'Room(s): '+str(room)+'<br>'+'Groups: '+str(groups)

			span = ind2-ind

			if span >1:
				print(span)
				for i in range(span):
					nd = 0
					nd = ind+i
					print(nd)
					if nd != ind:
						try:
							cm[nd] = '*'+str(typ)+'<br>'+'Groups: '+str(groups)+"<br><b>continues ..</b>"
						except:
							continue

	return cm

#Takes in the list of lists of couses and creates a dictionary with codes as keys and some 
#other data like rows
def analyzer(obj, codes):
	mond = {}

	for i in obj:
		load = []
		if len(i) >= 1:
			rows = ['row'+str(v+1) for v in range(len(i))]

			for p in range(len(rows)):
				ff = []
				cc = []
				for o in range(len(i[p])):

					ff.append(i[p][o])
					cc = combiner(ff)
				load.append(cc)


		mond[codes[obj.index(i)]] = load

	return mond
	#print(json.dumps(mond, indent = 4))








