#hungld
'''
-----------------
Bai toan doan so
----------------
'''
try:
	a = int(raw_input ("Nhap vao mot so bat ky A = "))
	while 1:
		b = raw_input ("Nhap vao so ban doan la binh phuong cua A hoac an q de quit  ")
		if b=="q":
			print "bb"
			break
		if b=="Q":
			print "bb"
			break
		d=int(b)
		c=a*a
		if d>0:
			if d < c:
				print "Ban hay nhap so lon hon"
			elif d ==c:
				print "Chuc mung ban da doan dung: %d la binh phuong cua %d"%(d,a)
				break
			else:
				print "Ban hay nhap so be hon" 
		else:
			print "Hay nhap vao 1 so tu nhien lon hon 0"
except:
	print "Hay nhap vao 1 so tu nhien"

