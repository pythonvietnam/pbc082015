#python
#loitd

#quan ly thong tin hoc sinh

ds = list()

while 1:
	c = raw_input("Ban muon nhap thong tin hs?")
	if c =='n':
		print ds
		break
	elif c == 'y':
		hs = dict()
		ht = raw_input("Ho va ten:")
		ns = raw_input("Ngay sinh:")
		# qq = raw_input("Que quan:")
		#tao 1 dict hs
		hs['hoten'] = ht
		hs['ns'] = ns
		# hs['qq'] = qq
		print hs
		#them hs vao ds toan truong
		ds.append(hs)
		print ds

# print ds
#





