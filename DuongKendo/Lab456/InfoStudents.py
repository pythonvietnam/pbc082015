import sys
Students = list()
i = 0
while(1):
	print "\tNhap vao Student thu %d"%(i+1)

	Student = list()
	_hoTen = raw_input("Ho ten:\t")
	if(_hoTen == 'q' or _hoTen == 'Q'):
		break
	else:
		Student.append(_hoTen)
#############
	_ngaySinh = raw_input("Ngay sinh:\t")
	if(_ngaySinh == 'q' or _ngaySinh == 'Q'):
		break
	else:
		Student.append(_ngaySinh)
#############		
	_gioiTinh = raw_input("Gioi tinh:\t")
	if(_gioiTinh == 'q' or _gioiTinh == 'Q'):
		break
	else:
		Student.append(_gioiTinh)
#############		
	_diaChi = raw_input("Dia chi:\t")
	if(_diaChi == 'q' or _diaChi == 'Q'):
		break
	else:
		Student.append(_diaChi)
#############		
	_lopHoc = raw_input("Lop hoc:\t")
	if(_lopHoc == 'q' or _lopHoc == 'Q'):
		break
	else:
		Student.append(_lopHoc)
#############		
	_queQuan = raw_input("Que quan:\t")

	if(_queQuan == 'q' or _queQuan == 'Q'):
		break
	else:
		i = i + 1
		Student.append(_queQuan)
	Students.append(Student)
for k in range(i):
	print Students[k]
_searchNameStudent = raw_input("Nhap vao ten sinh vien can tim kiem: ")
print _searchNameStudent
print len(Students)
for k in range(len(Students)):
	if _searchNameStudent == Students[k][0]:
		print Students[k]
		continue
	else:
		print "Sinh vien %s khong co trong danh sach"		
