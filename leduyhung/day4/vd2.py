#hungld
'''
-----------------
PythonCalculator
----------------
'''
try:
	n=int(raw_input("Nhap so 1 de thuc hien phep cong, 2 de thuc hien phep tru, 3 de thuc hien phep Nhan, 4 de thuc hien phep chia: "))
	a=int(raw_input("hay nhap vao so thu nhat: "))
	b=int(raw_input("Hay nhap vao so thu hai: "))
	if n==1: 
		s1 = a + b
		print"Tong cua %d va %d la %d"%(a,b,s1)
	elif n==2:
		s2 = a - b
		print"Hieu cua %d va %d la %d"%(a,b,s2)
	elif n==3:
		s3 = a * b
		print"Tich cua %d va %d la %d"%(a,b,s3)
	else:
		if b==0:
			print "Khong chia cho 0"
		else:
			s4 = a/b
			print"Thuong cua %d chia cho %d la %d"%(a,b,s4)
except:
	print "Hay nhap vao 1 trng cac so 1,2,3,4"

