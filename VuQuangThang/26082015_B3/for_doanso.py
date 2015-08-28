###### for doan so#####3
try:
		a=int(raw_input("Nhap so n>=0 \n"))
		while a<=0: 
			a=int(raw_input("Nhap lai so n>=0\n ")) 
			print "%d" %(a) 
		b=pow(a,2)
		for i in range(3):
			c=int(raw_input("Doan lai so binh phuong cua ban\n"))
			if c==b:
					print "Chinh xac"
					break
			elif c<b:
					print "Tang len"
			else:
					print "Giam xuong"
			
				
		print "Nhap qua 3 lan roi"
except:
		print "Loi, qua time hoac khong dung kieu"	
