#Module thuc hien cac chuc nang cua chuong trinh
#haind
#python

#tao menu lua chon
import json

def menu():
	print '''
	Chao mung ban den voi chuong trinh Quan ly hoc sinh!

		Su dung:
		1. Them moi hoc sinh
		2. Tim kiem hoc sinh
		3. Thoat chuong trinh (quit)
		'''
	return input("Moi ban lua chon: ")

#chuc nang them moi hoc sinh
def themHS():
	print "Ban da lua chon Them moi hoc sinh"
	hs = dict()
	global ds
	
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

#chuc nang tim kiem hoc sinh
def timHS():
	print "Ban da lua chon Tim kiem hoc sinh"

	global ds

	timkiem = raw_input("Moi ban nhap ten hoc sinh muon tim: ")
	ketquatim = list()

	for i in ds:
		if i['Ho ten'] == timkiem:
			ketquatim.append(i)
	print ""
	print "Da ket thuc tim kiem. Ket qua tim kiem la: "
	print ketquatim
	print ""