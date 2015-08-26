print "******Doan so binh phuong***********"
a= input ("Nhap mot so a : ")
if a< 0:
	print "Ban nhap sai roi, hay nhap lai "
bpa = pow(a,2)
b=input ("So ban du doan la : ")
if b<bpa:
	print "Ban doan thap qua tang len di"
elif b>bpa:
	print "So ban doan cao qua giam xuong di"
else: 
	print "Ok.ban doan dung roi"		
