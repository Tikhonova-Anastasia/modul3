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
			print('registration successful')
	else:
		print('login busy!')

def login_function(log, passwd):
	with open('d.json', 'r') as f:
		data = json.load(f)
	if log in data.keys():
		if data[log] == passwd:
			print('successfully')
	else:
		print('wrong login or password')
		
while True:
	q1 = input('enter or registration? ')
	if q1 == 'enter':
		login_function(input('login: '), input('password: '))	
	else:
		reg_data(input('login: '), input('password: '))
