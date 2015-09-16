# hungld
# demo file zip I/O
import os
import zipfile

filename = "a1.zip"
content = "a.csv"
file2 = "a1.csv"

if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
	print "File exists and access OK!"
	with zipfile.ZipFile(filename,"a") as zf:
		print zf.namelist()
		print " Now adding new file to archive"
		zf.write(file2) # duplicate multiple filename 
else:
	print " File not exists. Create new file"
	with zipfile.ZipFile(filename, "w") as zf:
		zf.write(content)
