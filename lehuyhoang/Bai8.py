# Dem so lan xuat hien cua cac tu trong 10 lan nhap cua nguoi dung

D={}

for i in range(10):
	x=raw_input("nhap ki tu: ")
	if 'x'=='Q':
		print"ban da thoat"
		break
	else:
		v=D.get(x,0)
		v=v+1
		D[x]=v
print'ket qua tinh toan'
for k in D:
	print'chuoi %s da duoc nhap %d lan'%(k,int(D[k]))
	