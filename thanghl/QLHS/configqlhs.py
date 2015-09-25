import os
import sys
def confighs(datainput):	
 # tao bien gloabal
	global database	
	database=datainput + '.txt'
	if (os.access(database, os.R_OK) and os.path.isfile(database)):
		print 'Da co database'
	else:
		print 'Database not exists. Create new database'
	#	with open(database, 'w') as fh:
	#		khoitao=str()
	#		fh.write(khoitao)
	print 'Database dang truy xuat hien tai la : ' + database 
