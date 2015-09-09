# NHAP NAM SINH
#TINH TUOI
# XAC DINH DO TUOI TRUY NHAP
print '''
   chao mung ban den voi dau truong game thu
   '''
a = input("nhap vao nam sinh cua ban")
b = 2015 - a
print "tuoi cua ban la %d" %(b)
if b<16:
	print "ban khong du tuoi vao chuong trinh nay"
else:
	print "chao mung ban den voi dau truong"