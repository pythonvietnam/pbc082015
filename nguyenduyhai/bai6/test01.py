#demo file IO

import os

### creat a new file

filename = 'test.csv'
content = '''Sass is the common lime on me
and Python is a part of it.!!!!!'''

if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
	print 'File exists and access OK!'
	with open(filename, 'rb') as fh:
		for line in fh:
			print line
else: 
	print 'Flie not exists. Create new file'
	with open(filename, 'wb') as fh:
		fh.write(content)