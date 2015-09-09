
#Tinh binh phuong

print "===========Tinh binh phuong===================="
#import thu vien math
import math
a = 10
try:
	nhapvao = raw_input ( "Nhap vao so du doan:" )
	#Ham tinh binh phuon pow
	ketqua = int(pow(a,2))
#print "Ket qua la: %d" %(pow(a,2))
except:
	print "Vui long nhap vao 1 so:"

while True:
	if nhapvao <  ketqua:
		print "Nhap so lon hon:"
		nhapvao = input ( "Nhap vao so du doan:" )
	elif nhapvao > ketqua:
		print "Nhap so nho hon:"
		nhapvao = input ( "Nhap vao so du doan:" )
	else:
		nhapvao == ketqua
		print "Dung roi"
		break

