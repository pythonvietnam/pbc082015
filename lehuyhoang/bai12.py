#mo file
import csv

with open('a.csv','wb') as fh:
	writer = csv.writer(fh, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['lehoang','akakak'])
	print 'done'
#read
print 'begin read'
with open('a.csv','rb') as fh:
	read = csv.reader(fh, delimiter=',',quotechar='|')
	for row in reader:
		print row