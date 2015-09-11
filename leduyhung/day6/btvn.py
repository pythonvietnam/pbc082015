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
ds=dict()
l1=list()
while 1:
	n = raw_input("Ban co muon nhap tiep du lieu nguoi dung (Y/N): ")
	if n == "n" or n == "N":
		break
	elif n == "y" or n == "Y":
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
while 1:
	m = raw_input("Ban co muon tim kiem du lieu nguoi dung (Y/N): ")
	if m == "n" or m == "N":
		break
	elif m == "y" or m == "Y":
		k = raw_input("Search keyword: ")
		u = [x[0] for x in a].index(k)
		print l[u]
