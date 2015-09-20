#demo csv file

import csv

with open('test1.csv' , 'wb') as fh:
	writer = csv.writer(fh, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) #demiliter la theo chuan cua csv
	writer.writerow(['haind', 'fpt', 'com', 'vn', 'admin'])
	print 'Done writing!'

###read the file
print 'Begin reading ...'
with open('test1.csv', 'rb') as fh:
	reader = csv.reader(fh, delimiter=',', quotechar='|')
	for row in reader:
		print row