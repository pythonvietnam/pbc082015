# quit

import math
import sys
try:
	_input = raw_input("nhap vao 1 so: ")
	print _input
	if _input == 'q' or _input == 'Q':
		sys.exit(0)
	else:
		_input = int(_input)
		#_binhPhuong = 0
		_cacBinhPhuong = int(pow(_input,2))
		#while _binhPhuong >= 0:
		while 1:
			_binhPhuong = raw_input("du doan binh phuong cua so vua nhap: ")	
			if _binhPhuong == 'q' or _binhPhuong == 'Q':
				sys.exit(0)
			else:
				_binhPhuong = int(_binhPhuong)
				if _binhPhuong >= 0:
					if _binhPhuong > _cacBinhPhuong:
						print ("nhap giam di.")
					elif _binhPhuong < _cacBinhPhuong:
						print ("nhap tang len.")
					else:
						print "Good"
						break
				else:
					print "So chinh phuong >=0"
					continue

except Exception, e:
	print e