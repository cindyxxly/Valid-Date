
def main():
	print('This program accepts a date in the form month/day/year and outputs whether or not the date is valid')
	Date = input('Please enter a date (mm/dd/yyyy): ' )
	mm, dd, yyyy = Date.split("/")
	m = int(mm)
	d = int(dd)
	y = int(yyyy)

	if (datecheck(m, d, y)):
		print(Date + ' is valid')
	elif (datecheck(m, d, y) == False):
		print(Date + ' is invalid')


def datecheck(m, d, y):
	try:
		if (m > 12):
			return False
		elif (m == 1, 3, 5, 7, 8, 10, 12):
			if (d <= 31):
				return True
			else:
				return False
		elif (m == 4, 6, 9, 11):
			if (d <= 30):
				return True
			else:
				return False
		elif (m == 2):
			if(leapcheck(m, d, y)):
				if (d <= 28):
					return True
				else:
					return False
			else:
				if (d <= 29):
					return True
				else: 
					return False
	except ValueError:
		print('Please enter the date according to the format')



def leapcheck(m, d, y):
	if (y % 4 == 0):
		return True
	else:
		return False

main()