#hungld
'''
-----------------------------------
Bai toan doan so su dung Dictionary
-----------------------------------
'''
print ''' 
Chuong trinh dem so ky tu do nguoi dung nhap vao
'''

d={}
for i in range(10):
	b = raw_input("Nhap vao mot chuoi bat ky  ")
	if (b == "q" or b == "Q"):
		break
	else:
		v = d.get(b,0)
		v = v + 1
		d[b] = v
print "Ket qua tinh toan la:"
for k in d:
	print "chuoi %s da duoc nhap %d lan "%(b,int(d[b]))	
	
