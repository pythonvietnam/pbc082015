#thanghl
# modlue doc file zip
import os
import zipfile

def giainen(read,listname):
#read=raw_input(' Nhap file zip chua dic  :')
	if (os.access(read, os.R_OK) and os.path.isfile(read)):
		print 'File exists and access OK'
		with zipfile.ZipFile(read, 'r') as zf:
			print zf.namelist()[0]
			listname=zf.namelist()[0]
			print (' Extract zip file now  ')
			zf.extractall()
			print listname



def giainenpw(readpw):
#	if (os.access(readpw, os.R_OK) and os.path.isfile(readpw)):
	#	print 'File exists and access OK'
	zip_file=zipfile.ZipFile(readpw)
	password = None
	with open('dictionaryAttk2.txt', 'r') as rtxt:
		for passzip in rtxt.readlines():
			password=passzip.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				print password
			except:
				pass
		print password
#def scanpass(readtxt):
#	with open(dictionaryAttk.txt, 'r') as rtxt:
	#	for passzip in rtxt:
#			passex=giainenpw(readpw,passzip)
	#		if passex:
	#			print 'Pass =' + passzip + '\n'


				
		