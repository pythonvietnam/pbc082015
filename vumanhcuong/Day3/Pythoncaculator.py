###Pythoncaculator

import math

print '''1.Nhap vao so 1 de thuc hien phep cong
		 2.Nhap vao so 2 de thuc hien phep tru
		 3.Nhap vao so 3 de thuc hien phep nhan
		 4.Nhap vao so 4 de thuc hien phep chia'''

a = raw_input ("Nhap vao so thu 1: ")
b = raw_input ("Nhap vao so thu 2: ")
c = raw_input ("Vui long chon so tu 1 den 4 de thuc hien phep toan: ")

if c == "1":
	print "Ket qua:%s" %(int(a) + int(b))
elif c == "2":
	print "Ket qua:%s" %(int(a) - int(b))
elif c == "3":
	print "Ket qua:%s" %(int(a) * int(b))
elif c == "4":
	print "Ket qua:%s" %(float(a) / float(b))
else:
	print "Nhap sai so"