#dientichchunhat.py
#Tinh dien tich hinh chu nhat

a = float(input("Chieu rong cua hinh chu nhat:"))
b = float(input("Chieu dai cua hinh chu nhat:"))
if b > a and b > 0 and a > 0:
	print "Dien tich cua hinh chu nhat la: %d"%(a*b)
else: 
	print "Ban can kiem tra lai cac so da nhap"
