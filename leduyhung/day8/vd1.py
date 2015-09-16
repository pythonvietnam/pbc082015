# hungld
# Demo file I/O
import os

# main
filename = "a.csv"
content = " sysadmin"

if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
	print "File exists and accesss OK!"
	with open(filename, "rb") as fh:
		for i in fh:
			print i
else:
	print "File not exists. Create new file"
	with open(filename,"wb") as fh:
		fh.write(content)
