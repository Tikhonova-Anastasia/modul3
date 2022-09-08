import json

data = {'testlog': 'testpasswd'}
with open('d.json', 'w') as f:
	json.dump(data, f)

def reg_data(log, passwd):
	with open('d.json', 'r') as f:
		data = json.load(f)
	if log not in data.keys():
		data[log] = passwd
		with open('d.json', 'w') as f:
			json.dump(data, f)
	else:
		print('login busy!')
		
while True:
	q1 = input('enter or registration? ')
	if q1 == 'enter':
		print('enter login and password')
		break
	else:
		reg_data(input('login: '), input('password: '))
