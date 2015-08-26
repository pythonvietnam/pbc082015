#hungld
'''
-----------------
Bai toan doan so
----------------
'''
try:
	a = int(raw_input("Nhap vao mot so bat ky A = "))
	for i in range(1,10):
		b = int(raw_input("Nhap vao so ban doan la binh phuong cua A = "))
		if b>0:
			c=a*a
			if b < c:
				print "Ban hay nhap so lon hon"
			elif b ==c:
				print "Chuc mung ban da doan dung: %d la binh phuong cua %d"%(b,a)
				break
			else:
				print "Ban hay nhap so be hon" 
		else:
			print "So binh phuong khong the la so am"
	print "Ban da het luot  du doan"
except:
	print "Hay nhap vao 1 so tu nhien"

