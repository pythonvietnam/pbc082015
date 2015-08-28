#xay dung chuong trinh PythonCalculator

print '''PythonCalculator:
		1. Thuc hien phep +
		2. Thuc hien phep -'''
while 1:
	a = input('Moi ban lua chon:')
	b = input("Moi ban nhap so hang 1:")
	c = input("Moi ban nhap so hang 2:")
	if a == 1:
		Ketqua = b + c
		print Ketqua
		continue
	elif a == 2:
		Ketqua = b - c
		print Ketqua