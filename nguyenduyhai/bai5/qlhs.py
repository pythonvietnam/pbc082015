#Quan ly hoc sinh. Xay dung ham tim kiem, them moi
#haind
#python

def menu():
	print '''Chao mung ban den voi chuong trinh Quan ly hoc sinh!

		Su dung:
		1. Them moi hoc sinh
		2. Tim kiem hoc sinh
		3. Thoat chuong trinh (quit)'''
	return input("Moi ban lua chon: ")

def themHS():
	print "Ban da lua chon Them moi hoc sinh"
	hs = dict()
	ds = list()
	name = raw_input("Ho va ten: ")
	birth = raw_input("Ngay sinh: ")
	addr = raw_input("Dia chi: ")
	#Tao dict
	hs['Ho ten'] = name
	hs['Ngay sinh'] = birth
	hs['Dia chi'] = addr
	#Them hoc sinh vao danh sach
	ds.append(hs)
	print ""
	print "Thong tin hoc sinh vua duoc them vao: %s"%(ds)
	print ""

def timkiemHS():
	print "Ban da lua chon Tim kiem hoc sinh"
	timkiem = raw_input("Moi ban nhap ten hoc sinh muon tim: ")
	ketquatim = list()
	for i in ds:
		if i['Ho ten'] == timkiem:
			ketquatim.append(i)
	print ""
	
vonglap = 1
choice = 0
while vonglap == 1:
	choice = menu()
	if choice == 1:
		themHS()
	elif choice == 2:
		timkiemHS()
	elif choice == 3:
		vonglap = 0

print "Cam on ban da su dung chuong trinh"
