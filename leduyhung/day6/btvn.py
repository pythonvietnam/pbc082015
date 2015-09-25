#hungld
'''
-----------------------------------------------
Bai toan nhap va hien thi thong tin nguoi dung:
-----------------------------------------------
'''
print'''
Nhap vao thong tin cua cua nguoi dung bao gom:
1. Ho ten
2. Ngay sinh
3. Gioi tinh
4. Dia chi
5. Lop hoc
6. Que quan
'''
l=list()
while 1:
	n = raw_input("Ban muon lam gi")
	if n == "n" or n == "N":
		break
	elif n == "1":
		ds=dict()
		a = raw_input("Ho va Ten: ")
		b = raw_input("Ngay sinh: ")
		c = raw_input("Gioi tinh: ")
		d = raw_input("Dia chi: ")
		e = raw_input("Lop hoc: ")
		f = raw_input("Que quan: ")
		ds["Ho va Ten"] = a	
		ds['Ngay sinh'] = b
		ds['Gioi tinh'] = c
		ds['Dia chi'] = d
		ds['Lop hoc'] = e
		ds['Que quan'] = f
		l.append(ds)
	elif n == "2":
		print " Tim kiem hoc sinh"
		qr = raw_input("Nhap vao ten ban muon tim kiem: ")	
		kqtk = list()
		for i in ds:
			if i["Ho va Ten"]== qr:
				kqtk.append(i)
		print "Ket qua tim kiem"
		print kqtk
