#hay su dung dictionary de dem so lan xuat hien cua cac tu trong 10 lan nhap cua nguoi dung
#haind

print '''
====================================================================
Ung dung Dictionary de dem so lan xuat hien cac tu trong 10 lan nhap
====================================================================
'''

d = {}
for i in range(10):
	x = raw_input("Moi ban nhap chuoi:")
	if (x == 'q' or x == 'Q'):
		print "Cam on ban da su dung chuong trinh."
		break
	else:
		h = d.get(x,0)
		h = h + 1
		d[x] = h
print "Ket qua cua chuong trinh tinh toan la:"
for k in d:
	print "Chuoi %s da duoc nhap %d lan"%(k,int(d[k]))



