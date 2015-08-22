#Bai2:
import time

year_n = time.strftime("%Y")
type(year_n) 	

year_n = int(year_n)
print "Nam %s"%year_n

print '====================Bai2=================='
year = input ("Nhap nam sinh :")
print "Nam sinh cua ban la:%d:"%(year)
tuoi = year_n - year
print "Tuoi cua ban la %d"%tuoi
if tuoi > 20:
	print "ok"
else:
	print "Khong du tuoi"



