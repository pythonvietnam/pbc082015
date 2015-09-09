# nhap vao 1 so
#doan binh phuong cua so day
#them chuc nang neu nguoi dung an x
#thi thong bao da huy lan doan day
#tu dong sinh ra so moi
print '''
	Nhap vao mot so
	Doan binh phuong cua so do
	an q or Q neu ban muon thoat ra
	an x or X neu ban muon huy lan doan



'''


for i in  range(10):
	a = raw_input("nhap vao mot so : ")
	if (a=='q' or a=='Q'):
		print "ban da thoat chuong trinh !"
		break
	else:
		b = raw_input("nhap so ban doan")
		while b!=a*a:
			if (a=='x' or a=='X'):
				print "ban da huy lan nhap nay"
				continue
			
			elif:
					print "ban da doan sai hay doan lai : "
					b = input("nhap so ban doan : ")
			else:
				print "ban da doan dung !"