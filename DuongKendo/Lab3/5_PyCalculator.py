# Author:
#		Kendo
#
# De bai	
# 	Nguoi dung nhap vao: _phep toan can tinh
#						 _2 toan tu
# In kq


import sys

_phepToan = raw_input("Nhap vao phep toan can tinh: ")
if _phepToan == '+' or _phepToan == '-' or _phepToan == '*' or _phepToan == '/':
	try:
		_toanTu1 = raw_input("Nhap vao toan tu thu 1: ")
		_toanTu2 = raw_input("Nhap vao toan tu thu 2: ")
		_toanTu1 = float(_toanTu1)
		_toanTu2 = float(_toanTu2)
		if _phepToan == '+':
			_tong = _toanTu1 + _toanTu2
			print "%d + %d = %d" %(_toanTu1, _toanTu2, _tong) 
		elif _phepToan == '-':
			_hieu = _toanTu1 - _toanTu2
			print "%d - %d = %d" %(_toanTu1, _toanTu2, _hieu)
		elif _phepToan == '*':
			_tich = _toanTu1 * _toanTu2
			print "%d * %d = %d" %(_toanTu1, _toanTu2, _tich)
		else:
			#if _toanTu2 == 0:
			#	print "Phep chia cho 0"
			#else: 
			_thuong = (_toanTu1) / _toanTu2
			print "%f / %f = %f" %(_toanTu1, _toanTu2, _thuong)
	except Exception, e:
		print "Nhap vao so tu nhien"
else:
	print "Khong phai toan tu"