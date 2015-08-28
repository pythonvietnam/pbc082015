###### Thuc hien dem ki tu a,b,c tu nhap vao #####
a = raw_input("nhap vao chuoi cua ban\n")
print "Chuoi cua ban la %s "%(a)
da=db=dc=0
for i in a:
	if i=="a":
		da=da+1
	elif i=="b":
		db=db+1
	elif i=="c":
		dc=dc+1
	else:
		continue
print "So lan xuat hien ki tu thieu thu tu a,b,c la %s %s %s " %(da,db,dc)
