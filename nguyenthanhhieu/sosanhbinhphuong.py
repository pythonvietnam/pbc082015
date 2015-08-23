print"""DAY LA TRO CHOI DOAN SO BINH PHUONG"""
a = input("Nhap vao 1 so da binh phuong:")
b = input("Nhap vao 1 so du doan binh phuong cua ban:")
c = b**b
print ("so cho truoc la:%d") %(a)
print ("so du doan cua ban la:%d") %(b)
print ("Ket qua la:%d") %(c)
if a < c:
	print ("Ban doan sai roi, nhap so du doan nho hon nhe!")
elif a > c:
	print ("Ban doan sai roi, nhap so du doan lon hon!")
else:
	print ("OK,Ban da doan dung!")