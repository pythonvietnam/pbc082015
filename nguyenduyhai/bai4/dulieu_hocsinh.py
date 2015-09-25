#Hoi thong tin nguoi dung va in ra man hinh cac thong tin da nhap vao voi noi dung nhu sau:
#Ho ten, ngay sinh, gioi tinh, dia chi, lop hoc, que quan
#haind

print '''
--------------------------
QUAN LY DANH SACH HOC SINH
--------------------------'''

hs = dict()
ds = list()

while 1: 
	choice = raw_input("Ban muon nhap thong tin hs?")
	if choice == 'n':
		print ds			#danh sach hs
		break
	elif choice == 'y':
		name = raw_input("Hay nhap ten cua ban: ")
		birth = raw_input("Hay nhap ngay/thang/nam sinh cua ban: ")
		sex = raw_input("Hay nhap gioi tinh cua ban: ")
		addr = raw_input("Hay nhap dia chi cua ban: ")
		clas = raw_input("Hoc sinh lop: ")
		hometw = raw_input("Que quan: ")
		#Tao dict
		hs['hoten'] = name
		hs['ngaysinh'] = birth
		hs['gioitinh'] = sex
		hs['diachi'] = addr
		hs['lop'] = clas
		hs['quequan'] = hometw

		#Them hs vao ds
		ds.append(hs)
		



