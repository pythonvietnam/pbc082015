# Author:
#		Kendo
#
#De bai	
# 	nhap vap 1 so
# 		sd for 10lan doan binh phuong cua so vua nhap
# 		cho nhap lai
###############################################################

import math
try:
	_input = input("nhap vao 1 so: ")
	_binhPhuong = 0
	_cacBinhPhuong = float(pow(_input,2))
	flag = 0
	for i in range(1,10):
		_binhPhuong = input("du doan binh phuong cua so vua nhap: ")
		if _binhPhuong >= 0:	
			if _binhPhuong > _cacBinhPhuong:
				print ("nhap giam di.")
			elif _binhPhuong < _cacBinhPhuong:
				print ("nhap tang len.")
			else:
				print "Good"
				flag = 1
				break

		else:
			print "So chinh phuong >=0"
	if flag == 1:
		print "dung roi! binh phuong cua %f la %f " %(_input, _binhPhuong)
	else:
		print "Ban chua doan dung"
except Exception, e:
	print e