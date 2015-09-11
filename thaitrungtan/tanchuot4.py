#doan binh phuong trong 10 lan
print '''
-------CHUOT NHAT XIN CHAO BAN----------
'''
a = input("moi ban nhap vao mot so")
for i in range(10):
	b = input("hay doan binh phuong cua so day")
	if b!=a*a:
		print "ban da doan sai hay doan lai"
	else:
		print "ban da doan dung"
		break
else:
	print "ban da nhap qua so lan cho phep"