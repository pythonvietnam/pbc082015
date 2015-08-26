#
# Kendo
# bai4:
# Tinh dien tich HCN
#

chieuDai = input("Nhap vao chieu dai HCN: ")
chieuRong = input("Nhap vao chieu rong HCN: ")
print "Thong so HCN: chieu dai %f , chieu rong %f" %(chieuDai, chieuRong)
if (chieuDai > 0 & chieuRong > 0 & chieuRong <= chieuDai):
	print "Dien tich HCN la: %f" %(chieuDai * chieuRong)
if (chieuDai > 0 | chieuRong > 0):		
	print "Chieu dai & chieu rong phai la so duong >0."	
else:
	print "Sai: chieuDai >= chieuRong"
