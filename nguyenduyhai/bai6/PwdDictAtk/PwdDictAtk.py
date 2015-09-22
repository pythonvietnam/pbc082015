#Chuong trinh PwdDictAtk
#haind
#python

import os
import zipfile

#Module chuc nang doc file Zip va giai nen file Zip co chua mat khau
def checkZip(filename, password):
	try:
		z = zipfile.ZipFile(filename)
		z.extractall(pwd = password)
		print "Mat khau chinh xac."
		return password
	except Exception, a: 
		print a
		return False

#Module chuc nang doc file Dictionary Pass va thuc hien check khi giai nen file Zip
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
	except Exception, a:
		print a
		return False


