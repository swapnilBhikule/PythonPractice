import datetime

name 	= input('Enter your name: ')
age 	= input('Enter your age: ')

current_time = datetime.datetime.now()
current_year = current_time.year

print('Dear ' + name + ', the year when you will be 100 years old: ', int(age) + current_year)