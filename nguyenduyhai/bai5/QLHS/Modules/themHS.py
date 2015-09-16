#module chuc nang Them moi hoc sinh
#haind
#python

#chuc nang them moi hoc sinh
def themHS():
	print "Ban da lua chon Them moi hoc sinh"
	hs = dict()

	name = raw_input("Ho va ten: ")
	birth = raw_input("Ngay sinh: ")
	addr = raw_input("Dia chi: ")

	#Tao dict
	hs['Ho ten'] = name
	hs['Ngay sinh'] = birth
	hs['Dia chi'] = addr

	#Them hoc sinh vao danh sach
	ds.append(hs)
	print ""
	print "Thong tin hoc sinh vua duoc them vao: %s"%(ds)
	print ""
