print '''
Nhap 1	 de cong
Nhap 2 de tru
nhap 3 de nhan
nhap 4 de chia
'''
value_input=raw_input('vui long chon phep tinh')
a = input("nhap vao so thu nhat :")
b = input("nhap vap so thu hai :")
if int(value_input) == 1:
	print"tong cua hai so %d" %(a + b)
elif int(value_input) == 2:
	print"hieu cua 2 so %d" %(a - b)

