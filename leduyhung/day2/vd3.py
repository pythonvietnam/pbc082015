#hungld
print ''' 
-----------------------------------------
Bai toan doan so
-----------------------------------------
'''
# asking for input
#int(a)
#int(b)
a = input("Hay nhap vao mot so bat ky:  ")
b = input("Hay nhap so binh phuong cua no:  ")
c = a*a
if b == c:
	print "Chuc mung ban" 
elif b > c:
	print "Ban hay nhap so nho hon"
else:
	print "Ban hay nhap so lon hon "
