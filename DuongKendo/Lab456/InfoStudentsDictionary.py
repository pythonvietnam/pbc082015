
Students = list()

while 1:
	_question = raw_input("Ban muon nhap thong tin sinh vien? ")
	if _question == 'n':
		print Students
		break
	elif _question =='y':
		Student = dict()
		_hoTen = raw_input("\tHo va ten:\t")
		_ngaySinh = raw_input("\tNgay sinh:\t")
		_gioiTinh = raw_input("\tGioi Tinh:\t")
		_diaChi = raw_input("\tDia chi:\t")
		_lopHoc = raw_input("\tLop hoc:\t")
		_queQuan = raw_input("\tQue quan:\t")
		
		Student['hoTen'] = _hoTen
		Student['ngaySinh'] = _ngaySinh
		Student['gioiTinh'] = _gioiTinh
		Student['diacChi'] = _diacChi
		Student['lopHoc'] = _lopHoc
		Student['queQuan'] = _queQuan
		
		Students.append(Student)
		
_searchNameStudent = raw_input("Nhap vao ten sinh vien can tim kiem: ")
print _searchNameStudent
print len(Students)
SearchStudents = list()
for k in Students:
	if _searchNameStudent == k['hoTen']:
		SearchStudents.append(k)
		continue
#	else:
#		print "Sinh vien %s khong co trong danh sach"		

print SearchStudents
	 