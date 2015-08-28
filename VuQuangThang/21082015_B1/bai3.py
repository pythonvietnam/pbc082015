###Tinh dien Tich##
l = int(raw_input("Nhap chieu dai, dang so >0 \n"))
while l<=0:
	l=int(raw_input("Nhap LAI chieu dai, dang so >0 \n"))
w = int(raw_input("Nhap chieu rong, dang so > 0, nho hon chieu dai. \n"))
while w<=0 or w>=l:
	w=int(raw_input("Nhap LAI chieu rong phai nho hon chieu dai va >0\n"))
print "Dien Tich la: %d*%d = %d \n"%(l,w,l*w)