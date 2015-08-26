#
# Kendo
# bai3:
# 	Hoi nam sinh
#	tinh tuoi & kiem tra du tuoi de truy cap khong
#

print 'Bai3'
namSinh = input("Nhap vao nam sinh cua ban: ")
tuoi = 2015 - namSinh + 1
print 'Tuoi cua ban la: %d '%(tuoi)

if tuoi < 16:
	print "Di ra!!!"
else:
	print "Welcome!!!"