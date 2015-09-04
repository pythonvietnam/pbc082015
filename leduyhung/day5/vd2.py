#hungld
'''
-----------------------------------
Bai toan tinh gia tri trung binh
-----------------------------------
'''
print ''' 
Chuong trinh tinh gia tri trung binh:
'''
d =[]
try:
	for i in range(3):
		b = int(raw_input("Nhap vao 3 so bat ky:  "))
		d.append(b)
	a = sum(d)/3.0
	print "Gia tri trung binh la: %f"%(a)
except:
        print "Hay nhap vao 1 so tu nhien"

