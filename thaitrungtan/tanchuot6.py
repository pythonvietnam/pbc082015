#nhap vao chuc nang thoat chuong trinh

print ''' 
   		 nhap vao mot so
 		 doan binh phuong cua no
  ** an q or Q neu ban muon thoat khoi chuong trinh **
 '''


for i in  range(10):
	a = raw_input("nhap vao mot so : ")
	if (a=='q' or a=='Q'):
		print "ban da thoat chuong trinh !"
		break
	else:
		b = input("nhap so ban doan")
	
		while b!=a*a:
			print "ban da doan sai hay doan lai : "
			b = input("nhap so ban doan : ")
		else:
			print "ban da doan dung !"
			