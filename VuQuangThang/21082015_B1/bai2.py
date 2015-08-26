year = input("Vui long nhap nam hien tai, dang yyyy  \n")
age = input("Nhap nam sinh cua ban, dang yyyy \n ")
a = year - age
print "So tuoi cua ban la %d" %(a)
if a < 16:
	print "Nho tuoi qua, ve ti me di :)"
else:
	print "OK Ban da du tuoi hanh dong :D"