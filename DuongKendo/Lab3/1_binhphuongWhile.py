# Author:
#		Kendo
#
#De bai	
# 	nhap vap 1 so
# 		sd while doan binh phuong cua so vua nhap
# 		cho nhap lai den khi doan dung thi dung chuong trinh
###############################################################


import math


try:
	_input = input("nhap vao 1 so: ")
	_binhPhuong = 0
	_cacBinhPhuong = float(pow(_input,2))
	while _binhPhuong >= 0:
		input("du doan binh phuong cua so vua nhap: ")	
		if _binhPhuong > _cacBinhPhuong:
			print ("nhap giam di.")
		elif _binhPhuong < _cacBinhPhuong:
			print ("nhap tang len.")
		else:
			print "Good"
			break
	else:
		print "So chinh phuong >=0"

except Exception, e:
	print e