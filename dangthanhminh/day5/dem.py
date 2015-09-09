#minhdt
#Hay su dung dictionary de dem so lan xuat hien cuar cac tu trong 10 lan nhap cua nguoi dung
d = {}

for i in range(10):
	a = raw_input ("Hay nhap chuoi:")
	if a == 'q' or a == 'Q':
	    break
	else:
 	    v = d.get(a,0)
	    v = v+1
	    d[a] = v

##
print 'Ket qua sau khi tinh toan la:'

for k in d:
	print "Chuoi %s da duoc nhap %d lan"%(k, int(d[k]))
