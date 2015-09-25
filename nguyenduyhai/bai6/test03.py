#demo zip file

import os
import zipfile

filename = 'test1.zip'
content = 'test.csv'
file2 = 'test1.csv'

if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
	print 'File exists and access OK'
	with zipfile.ZipFile(filename, 'a') as zf:
		print zf.namelist()
		print "Now adding new file to archive"
		zf.write(file2) #duplicate multiple filename will
else: 
	print 'File not exists. Creat new file'
	with zipfile.ZipFile(filename, 'w') as zf:
		zf.write(content)