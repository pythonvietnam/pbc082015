import os
import zipfile
import csv

#tao ham Menu hien thi
def menu():
        print '''
        Chao mung ban den voi chuong trinh demo I/O file!

                Su dung:
                1. File thong thuong
                2. File CSV
                3. File Zip
                4. Thoat chuong trinh (quit)
                '''
        return input("Moi ban lua chon: ")
# tao ham demo1
def demo1():
	print ""
	filename = "a.csv"
	content = " sysadmin"

	if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
        	print "File exists and accesss OK!"
        	with open(filename, "rb") as fh:
                	for i in fh:
                        	print i
	else:
        	print "File not exists. Create new file"
        	with open(filename,"wb") as fh:
                	fh.write(content)
# tao ham demo2
def demo2():
	with open("a1.csv","wb") as fh:
        	writer = csv.writer(fh,delimiter=",",quotechar="|", quoting=csv.QUOTE_MINIMAL)
        	writer.writerow(["hungld","Peacesoft","net", "sysadmin"])
        	print"Done writing!"

	# read the file
	print "Begin reading..."
	with open("a1.csv","rb") as fh:
        	reader = csv.reader(fh,delimiter=",",quotechar="|")
        	for row in reader:
                	print row
# tao ham demo3
def demo3():
	filename = "a1.zip"
	content = "a.csv"
	file2 = "a1.csv"

	if (os.access(filename, os.R_OK) and os.path.isfile(filename)):
        	print "File exists and access OK!"
        	with zipfile.ZipFile(filename,"a") as zf:
                	print zf.namelist()
                	print " Now adding new file to archive"
                	zf.write(file2) # duplicate multiple filename 
	else:
        	print " File not exists. Create new file"
        	with zipfile.ZipFile(filename, "w") as zf:
                	zf.write(content)
