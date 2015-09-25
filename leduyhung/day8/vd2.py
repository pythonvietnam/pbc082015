# hungld
# Demo file CSV I/O

import csv
with open("a1.csv","wb") as fh:
	writer = csv.writer(fh,delimiter=",",quotechar="|", quoting=csv.QUOTE_MINIMAL)
	writer.writerow(["hungld","Peacesoft","net", "sysadmin"])
	print"Done writing!"

# read the file
print "Begin reading..."
with open("a1.csv","rb") as fh:
	reader = csv.reader(fh,delimiter=",",quotechar="|")
	for row in reader:
		print row
