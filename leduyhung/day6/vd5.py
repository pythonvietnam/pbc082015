#hungld
'''
-----------------------------------------------
Bai toan nhap va hien thi thong tin nguoi dung:
-----------------------------------------------
'''
L=list()
d=dict()
print'''
Nhap vao thong tin cua cua nguoi dung bao gom:
1. Ho ten
2. Ngay sinh
3. Gioi tinh
4. Dia chi
5. Lop hoc
6. Que quan
'''
while 1:
	g=raw_input("Ban co muon nhap tiep du lieu nguoi dung Y/N ")
	if g=="n" or g=="N":
		break
	elif g=="y" or g=="Y":
		a=raw_input("Ho va Ten: ")
		b=raw_input("Ngay sinh: ")
		c=raw_input("Gioi tinh: ")
		d=raw_input("Dia chi: ")
		e=raw_input("Lop hoc: ")
		f=raw_input("Que quan: ")
		d['HovaTen']=a	
		d['Ngaysinh']=b
		d['Gioitinh']=c
		d['Diachi']=d
		d['Lophoc']=e
		d['Quequan'] =f
		L.append(d)
