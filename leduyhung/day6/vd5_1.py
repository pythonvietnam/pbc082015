hs = dict()
ds = list()

while 1:
	c = raw_input("Ban muon nhap thong tin hs?")
	if c=='n':
		print ds
		break
	elif c=='y':
		ht = raw_input("Ho va ten: ")
		ns = raw_input("Ngay sinh: ")
		hs['hoten']= ht
		hs['ns']=ns
		ds.append(hs)
