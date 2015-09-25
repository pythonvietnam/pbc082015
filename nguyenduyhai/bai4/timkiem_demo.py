



ds = list()

while 1:
	c = raw_input("Ban muon nhap thong tin hs? ")
	if c == 'q':
#		print ds
		break
	elif c == '1':
		print "Tao thong tin hoc sinh"
		hs = dict()
		ht = raw_input("Ho va ten: ")
		ns = raw_input("Ngay sinh: ")


		hs['hoten'] = ht
		hs['ngaysinh'] = ns

		#Them hs vao ds
		ds.append(hs)

	elif c == '2':
		print "Tim kiem hoc sinh"
		qr = raw_input("Nhap ten hoc sinh muon tim kiem: ")
		kqtk = list()
		for i in ds:
			if i['hoten'] == qr:
				kqtk.append(i)

		print "Da ket thuc tim kiem. Ket qua tim kiem la:"
		print kqtk
