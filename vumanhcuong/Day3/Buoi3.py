
#Buoi 3

a = 1
while (a < 10):
	print 'Gia tri nay:', a
	a = a + 1
print 'ket thuc'


for i in  range (1,10):
	print "xxx"
else:
	print "bbbb"


####Luon tao try exception:
e = int (raw_input("Nhap vao day so:"))
try:
	print "So nay là:",e
except:
	print "nhap sai"



##finnally: câu lệnh cuối cùng sẽ thực hiện khi có exception hay ko. Ví dụ : đóng file, đóng kết nối khi mở.