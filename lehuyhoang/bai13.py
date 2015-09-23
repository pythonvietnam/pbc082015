#demo zip file
import os
import zipfile
filename = 'a1.zip'
content = 'a.csv'
file2= 'a1.csv'
if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
	print 'file....'
	with zipfile.ZipFile(filename,'a') as zf:
		print zf.namelist()
		print "zip file"
		zf.write(file2)
else:
	print 'create new file'
	with zipfile.ZipFile(filename,'w') as zf:
		zf.write(content)