#demo file IO
import os

#create a new file
filename = 'a1.csv'
content = ''' Chao moi nguoi'''
if (os.access(filename,os.R_OK) and os.path.isfile(filename)):
	print 'file exists and access OK !'
	with open(filename,'rb') as fh:
		for line in fh:
			print line
else:
	print' File not exists. create new file'
	with open(filename,'wb') as fh:
		fh.write(content)
