#Module chuc nang Xu ly file (open, read, write, csv, zip)
#haind
#python

#tao menu lua chon
def menu():
	print '''
	Chao mung ban den voi chuong trinh Xu ly File!

		Su dung:
		1. Tao moi file .TXT
		2. Lam viec voi file .CSV
		3. Lam viec voi file .ZIP 
		4. Thoat chuong trinh (quit)
		'''
	return input("Moi ban lua chon: ")

#chuc nang tao file TXT
def creatFile():

	import os

	filename = 'haind.txt'
	content = '''Bai tap tao file voi python
				duoc viet boi Haind'''

	if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
		print 'File exists and access OK!'
		with open(filename, 'rb') as fh:
			for line in fh:
				print line
	else: 
		print 'Flie not exists. Create new file'
		with open(filename, 'wb') as fh:
			fh.write(content)

#chuc nang lam viec voi file CSV
def creatCSV():

	import csv

	with open('haind.csv' , 'wb') as fh:
		writer = csv.writer(fh, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) #demiliter la theo chuan cua csv
		writer.writerow(['STT', 'Account', 'Email', 'Email1', 'Email2', 'Position'])
		writer.writerow(['1', 'haind', 'fpt', 'com', 'vn', 'admin'])
		print 'Done writing!'

	###read the file
	print 'Begin reading ...'
	with open('haind.csv', 'rb') as fh:
		reader = csv.reader(fh, delimiter=',', quotechar='|')
		for row in reader:
			print row

#chuc nang lam viec voi file ZIP
def creatZIP():

	import os
	import zipfile

	filename = 'haind.zip'
	content = 'haind.txt'
	file2 = 'haind.csv'

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