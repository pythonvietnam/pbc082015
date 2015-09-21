#Chuong trinh PwdDictAtk
#haind
#python

import os
import zipfile

def checkZip(filename, password):
	try:
		z = zipfile.ZipFile(filename)
		z.extractall(pwd = password)
		print "Mat khau chinh xac."
		return password
	except Exception, e: 
		print e
		return False

def readPWD(filename, dictfile):
	try:
		keys = open(dictfile, 'r')
		for key in keys.readlines():
			key = key.strip('\n')
			print "Dang thuc hien thu mat khau voi mat khau la: " + key 
			checkresult = checkZip(filename, key)
			if checkresult != False:
				print "Da tim thay mat khau la: " + checkresult
				exit(0)
			else:
				print "Mat khau khong chinh xac!"
		return
	except Exception, e:
		print e
		return False


