#python
#loitd
#demo csv file

import csv

with open('a.csv', 'wb') as fh:
	writer = csv.writer(fh, delimiter=',', quotechar='|'
		, quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['loitd', 'pythonvietnam', 'org', 'admin'])
	print 'Done writing!'

####read the file
print 'Begin reading ...'
with open('a.csv', 'rb') as fh:
	reader = csv.reader(fh, delimiter=',', quotechar='|')
	for row in reader:
		print row