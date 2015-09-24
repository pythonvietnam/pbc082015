#Chuong trinh Quan ly hoc sinh. Xay dung ham tim kiem, them moi
#haind
#python

import json
import os

#tao menu lua chon
def menu():
	print '''
	Chao mung ban den voi chuong trinh Quan ly hoc sinh!

		Su dung:
		1. Them moi hoc sinh
		2. Tim kiem hoc sinh
		3. Load du lieu hoc sinh
		4. Thoat chuong trinh (quit)
		'''
	return input("Moi ban lua chon: ")

#tao danh sach lam bien global
ds = list()		

#load lai du lieu hoc sinh
def loadHS(filename):
	global ds 
	if (os.path.isfile(filename)):
		print "Da co file, bat dau load danh sach hoc sinh."
		with open(filename, 'rb') as fh:
			data = fh.readline()
			ds = json.loads(data)
		print "Da load danh sach hoc sinh!"
	else:
		print "File du lieu khong dung."

#chuc nang them moi hoc sinh
def themHS():
	print "Ban da lua chon Them moi hoc sinh"
	hs = dict()

	name = raw_input("Ho va ten: ")
	birth = raw_input("Ngay sinh: ")
	addr = raw_input("Dia chi: ")
	global ds
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
	timkiem = raw_input("Moi ban nhap ten hoc sinh muon tim: ")
	ketquatim = list()
	for i in ds:
		if i['Ho ten'] == timkiem:
			ketquatim.append(i)
	print ""
	print "Da ket thuc tim kiem. Ket qua tim kiem la: "
	print ketquatim
	print ""

#luu hs vao file
def saveHS():
	global ds
	#conver ds ra json
	datajson = json.dumps(ds)
	#ghi vao file text
	try:
		with open ("dbhs.txt","wb") as fh:
			fh.write(datajson)
		print "Da luu danh sach hoc sinh thanh cong."
	except e, Exception:
		print "Co loi khi luu file"

#thuc hien vong lap chuong trinh
vonglap = 1
choice = 0

while vonglap == 1:
	choice = menu()
	if choice == 1:
		themHS()
	elif choice == 2:
		timHS()
	elif choice == 3:
		loadHS("dbhs.txt")
	elif choice == 4:
		vonglap = 0
		saveHS()
print "Cam on ban da su dung chuong trinh"
