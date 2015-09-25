#tim kiem du lieu
#haind
#python

print '''
Welcome to my program
I. Usage
	a. Nhap du lieu hoc sinh
	b. Tim kiem du lieu hoc sinh
'''

hs = dict()
ds = list()


while 1:
	choice = raw_input("Please input your choice? (a/b): ")
	if choice == 'a':
		while 1:
			choice1 = raw_input("BAN CO MUON NHAP THONG TIN HOC SINH? (y/n): ")
			if choice1 == 'y':
				name = raw_input("Hay nhap ten cua ban: ")
				birth = raw_input("Hay nhap ngay/thang/nam sinh cua ban: ")
				sex = raw_input("Hay nhap gioi tinh cua ban: ")
#				addr = raw_input("Hay nhap dia chi cua ban: ")
#				clas = raw_input("Hoc sinh lop: ")
#				hometw = raw_input("Que quan: ")
			#Tao dict
				hs['hoten'] = name
				hs['ngaysinh'] = birth
				hs['gioitinh'] = sex
#				hs['diachi'] = addr
#				hs['lop'] = clas
#				hs['quequan'] = hometw
	#Them hs vao ds
				ds.append(hs)

			elif choice1 == 'n':
				print ds
		break

	else:
		print "Moi ban nhap ten ban muon tim kiem"
	for i in max(ds):
		tk = raw_input("Hay nhap ten ban muon tim")
		if tk == hs['hoten']:
			ht['hoten'] = name
			print ht['hoten']
