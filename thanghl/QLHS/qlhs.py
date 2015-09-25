#Chuong trinh Quan ly hoc sinh. Xay dung ham tim kiem, them moi
#haind
#python


import json
import os
import configqlhs
global database
#tao menu lua chon
def menu():
	print '''
	Chao mung ban den voi chuong trinh Quan ly hoc sinh!

		Su dung:
		1. Chon database 
		2. Them moi hoc sinh
		3. Tim kiem hoc sinh
		4. Load danh sach hoc sinh
		5. Thoat chuong trinh (quit)
		'''
	return input("Moi ban lua chon: ")

#tao danh sach lam bien global
ds = list()		

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
	print '''Thong tin hoc sinh vua duoc them vao: 
	-------------------------------
	%s''' %(ds)
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

# su dung json de them dictionary vao file 
def addfile(database):
#conver ds ra json
	global ds
	global data
	#global database
	data=json.dumps(ds)
	print ' Database dang duoc luu lai tai file ' + database
	try:
		with open(database,'w') as fh:
			fh.write(data)
		print "Da luu danh sach hoc sinh thanh cong."
	except:
		print "Co loi khi luu file"
#ham load file truoc khi input json 
def loadfile():
	global ds 
	if (os.path.isfile(database)):
		print "Da co file, bat dau load danh sach hoc sinh trong database : " + database 
		with open(database, 'rb') as fh:
			# doc du lieu json theo dong 
			data = fh.readline()
			ds = json.loads(data)
		print "Da load danh sach hoc sinh!"

	else:
		print "File du lieu khong dung."
#thuc hien import file config
#def configql():
	 # tao bien gloabal
#	global database
#	database =raw_input('Nhap thong tin database :') + '.txt'
#	print 'database dang truy xuat hien tai la : ' + database

	
#thuc hien vong lap chuong trinh
vonglap = 1
choice = 0
while vonglap == 1:
	choice = menu()
	if choice ==1:			
		# goi ham configql()
		#configqlhs.configql()
		datainput = raw_input('Nhap file name database : ') 
		configqlhs.confighs(datainput)
		#print 'database cua ban hien la : ' + database
		#loadfile(database)
		#print ds
		print configqlhs.confighs(database)
	if choice == 2:
		themHS()
	elif choice == 3:
		timHS()
	elif choice == 4:
		loadfile()
		print ds
	elif choice == 5:
		#print database	
		addfile(database)
		vonglap = 0
print "Cam on ban da su dung chuong trinh"
