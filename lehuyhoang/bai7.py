
print '''
nhap 1 de cong 
nhap 2 de tru 
nhap 3 de nhan 
nhap 4 de chia
'''
while True:
	try:
		s=int(raw_input("ban su dung phep tinh nao:"))
		s1=int(raw_input("so thu nhat:"))
		s2=int(raw_input("so thu hai:"))
		if s==1:
			print "tong la:%d"%(s1+s2)
		if s==2:
			
			print "hieu la:%d"%(s1-s2)
		if s==3:
			
			print "tich la:%d"%(s1*s2)
		if s==4:
			if s2 == 0:
				break
			else:
				print "thuong la:%d"%(s1/s2)
	except:
		print 'Vui Long Nhap 1 So'
 

 dictt ={
 'hoang': 'day la gia tri',
 'quang': 'day la quang'
 }
 