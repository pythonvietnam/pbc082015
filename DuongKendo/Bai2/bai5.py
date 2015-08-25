#
# Kendo
# bai5:
# nhap vao 1 so
#
import math
_input = input("Nhap vao 1 so: ")
#print "So ban vua nhap la %d" %_input
_binhPhuong = input("Du doan binh phuong cua so vua nhap la: ") 
_calBinhPhuong = pow(_input,2)
#print _calBinhPhuong
if _binhPhuong >= 0:
	if _binhPhuong < _calBinhPhuong:
		print "Nhap tang len."
	elif _binhPhuong == _calBinhPhuong:
			print "GOOD"
	else:
			print "Nhap giam di."
else:
	print "So chinh phuong phai >=0"