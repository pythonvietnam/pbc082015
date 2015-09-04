#Kendo

# Sd dictionary dem so lan xuat hien cua 1 tu trong 10 lan nguoi dung nhap vao

print '''
	Chuong trinh dem so lan xuat hien cuar cacs chuoi
	nguoi dung nhap vao.
'''

D = {}
for i in range(0,10):
	_input = raw_input("Nhap vao 1 chuoi bat ky: ")
	#if _input in D:
	#	D[_input] = D[_input] + 1
	#else:
	#	D[_input] = 1
	

	if (_input == 'q' or _input == 'Q'):
		print D
		break
	else:
		a = D.get(_input, 0)
		a = a + 1
		D[_input] = a

print "Ket qua"
for k in D:
	print "D[%s] = %d " %(k, D[k])
	#print k, D[k]