#module chuc nang Tim kiem hoc sinh
#haind
#python

#chuc nang tim kiem hoc sinh
def timHS():
	print "Ban da lua chon Tim kiem hoc sinh"

	global ds

	timkiem = raw_input("Moi ban nhap ten hoc sinh muon tim: ")
	ketquatim = list()

	for i in ds:
		if i['Ho ten'] == timkiem:
			ketquatim.append(i)
	print ""
	print "Da ket thuc tim kiem. Ket qua tim kiem la: "
	print ketquatim
	print ""