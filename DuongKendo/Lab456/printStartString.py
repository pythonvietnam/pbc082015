# Nhap vao 1 chuoi
#	In nhung chuoi bat dau = chatmsg
#	q => thoat

import sys

A = list()

while(1):
	_input = raw_input("Nhap vao:")
	if(_input == 'q' or _input == 'Q'):
		print A
		sys.exit()
	elif (_input.startswith('chatmsg:')):
		A.append(_input)

