#hungld
'''
-----------------
Bai toan doan so
----------------
'''
try:
	a = input ("Nhap vao mot so bat ky A = ")
	while a>0:
		b = input ("Nhap vao so ban doan la binh phuong cua A = ")
		c=a*a
		if b < c:
			print "Ban hay nhap so lon hon"
			continue
		elif b ==c:
			print "Chuc mung ban da doan dung: %d la binh phuong cua %d"%(b,a)
			break
		else:
			print "Ban hay nhap so be hon" 
			continue
	else:
		print "Hay nhap vao 1 so tu nhien lon hon 0"
except:
	print "Hay nhap vao 1 so tu nhien"

