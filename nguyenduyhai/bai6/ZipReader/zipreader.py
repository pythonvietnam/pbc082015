#Chuong trinh PythonZipReader
#haind
#Python

import os
import zipfile

def menu():
	print '''
	Chao mung ban den voi chuong trinh Python Zip Reader!

		Su dung:
		1. Nen file Zip
		2. Giai nen file Zip
		3. Thoat chuong trinh (quit)
		'''
	return input("Moi ban lua chon: ")

def nenZip(filename, filenen):

	#fileZip = raw_input("Hay nhap file can giai nen Zip: ")
	#global filenen

	if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
		print 'File da ton tai, co the truy nhap OK'
		with zipfile.ZipFile(filename, 'a') as zf:
			print zf.namelist()
			print "Bat dau thuc hien nen zip"

	else: 
		print ''
		print 'File chua ton tai. Da thuc hien nen file'
		with zipfile.ZipFile(filename, 'w') as zf:
			zf.write(filenen)

def giainenZip(filegiainen):


	if (os.access(filegiainen, os.R_OK) and os.path.isfile(filegiainen)):
		print ''
		print 'Dang thuc hien giai nen, ket qua giai nen: '
		z = zipfile.ZipFile(filegiainen)
		z.extractall()
		print z.namelist()
		print "Da thuc hien giai nen thanh cong"

	else: 
		print ''
		#print 'File chua ton tai. Da thuc hien nen file'
		#z = zipfile.ZipFile(filename)

		print "Khong tim thay file, giai nen khong thanh cong"
