##Tinh dien tich hinh chu nhat

print "===============Tinh dien tich hinh chu nhat:CUONGVM====================="

chieudai = input ("Nhap vao chieu dai:")
print "Chieu dai la:%d"%(chieudai)
chieurong = input ("Nhap vao chieu rong:")
print "Chieu rong la %d"%(chieurong)

if chieurong > chieudai:
	print "Vui long nhap lai"
else:
	print "Dien tich hinh chu nhat la:%d"%(chieudai * chieurong)