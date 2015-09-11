#bai 8
#xay dung huong trinh python calculator
print '''
	chon 1 de thuc hien phep cong
	chon 2 de thuc hien phep tru
	chon 3 de thuc hien phep nhan
	chon 4 de thuc hien phep chia
	'''
a =  input("moi ban chon phep tinh :" )
b = input("nhap vao so thu nhat : ")
c = input("nhap vao so thu 2 : ")
if a==1:
	print "tong cua 2 so la %d" %(c+b)
elif a==2:
	print "hieu cua 2 so la %d" %(c-b)
elif a==3:
	print "tich cua 2 so la %d" %(c*b)
else:
	print "thuong cua 2 so la %d" %(c/b)