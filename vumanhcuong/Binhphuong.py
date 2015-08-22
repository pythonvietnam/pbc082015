
#Tinh binh phuong

print "===========Tinh binh phuong===================="
import math

a = 10
nhapvao = input ( "Nhap vao so du doan:" )
ketqua = pow(a,2)
	print "Ket qua la: %d" %(pow(a,2))

if nhapvao <  ketqua:
	print "Nhap so lon hon"
elif nhapvao == ketqua:
	print "Tra loi dung"
else:
	nhapvao > ketqua
	print "Nhap so nho hon"
	