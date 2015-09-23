#python
#loitd

#quan ly thong tin hoc sinh + tim kiem

ds = list()

while 1:
	c = raw_input("Ban muon lam gi?")
	if c =='q':
		break
	elif c == '1':
		print "Them moi hs"
		hs = dict()
		ht = raw_input("Ho va ten:")
		ns = raw_input("Ngay sinh:")
		# qq = raw_input("Que quan:")
		#tao 1 dict hs
		hs['hoten'] = ht
		hs['ns'] = ns
		# hs['qq'] = qq
		#them hs vao ds toan truong
		ds.append(hs)
	elif c == '2':
		print "Tim kiem hs"
		qr = raw_input("Nhap ten hs muon tim kiem:")
		kqtk = list()
		for i in ds:
			if i['hoten'] == qr:
				kqtk.append(i)

		print "Da ket thuc tim kiem. Ket qua tim kiem la:"
		print kqtk

#





