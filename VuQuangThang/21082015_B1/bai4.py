#def binh_phuong()
try:
		a=int(raw_input("Nhap so n>=0 \n"))
		while a<=0: 
			a=int(raw_input("Nhap lai so n>=0\n ")) 
			print "%d" %(a) 
		b=pow(a,2)
		c=int(raw_input("Doan so binh phuong cua ban\n"))
		while c!=b:
			if c<b:
				print"chua dung, cao len 1 chut\n"
				c=input()
			else:
				print"qua rui giam xuong ti\n"
				c=input()
		print "Chinh xac ket qua la %d" %(c)
except:
		print "Ban nhap khong dung kieu Integer"	
