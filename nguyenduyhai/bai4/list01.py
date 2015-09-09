#cho phep nguoi dung nhap vao 10 lan, tinh gia tri trung binh cua 10 so 

l = []
for i in range(3):
	x = input('Moi ban nhap so:')
	l.append(x)
	print l
	a = ((sum(l))/3.0)
print "Ket qua trung binh cua 3 lan nhap la: %d"%(a)