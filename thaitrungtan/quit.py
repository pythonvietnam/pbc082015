a = input("nhap vao mot so ")
q = input("quit chuong trinh")
if a==q:
	print "quit"
	break
elif a!=q:
	b = input("doan binh phuong cua so day")
	while b!=a*a:
		print"ban da nhap sai hay nhap lai"
		b = input("doan binh phuong cua so day")
else:
	print "ban da doan dung"
