#minhdt
#Cho phep nguoi dung nhap vao 5 so tinh gia tri trung binh cua 5 so do

a = list()

for i in range(5):
	b = int(raw_input('nhap vao so bat ky:'))
	a.append(b)
	x = sum(a)/5.0
	print ('gia tri tong trung binh cua %f so tu nhien la:')%(x)
