#Bai2:
import time

#Lay thoi gian la nam hien tai
year = time.strftime("%Y")
#Xem kieu cho nam string
print "Kieu %s"%type(year) 	

#Chuyen nam sang dang INT
year = int(year)
print "Nam %s"%year

print '====================Bai2=================='
year_born = input ("Nhap nam sinh :")
print "Nam sinh cua ban la:%d:"%(year)
tuoi = year - year_born

print "Tuoi cua ban la %d"%tuoi
if tuoi > 20:
	print "ok"
else:
	print "Khong du tuoi"



