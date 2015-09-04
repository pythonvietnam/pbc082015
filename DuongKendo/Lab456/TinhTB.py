#Kendo

#Nhap 10 lan 
#Tinh gia tri trung binh cua cac so nhap vao

L = []
for i in range(3):
	_input = raw_input("Nhap vao 1 so: ")
	_input = float(_input)
	L.append(_input)
_sum = sum(L)
_len = len(L)
print "avg = %f" %(_sum/_len)
