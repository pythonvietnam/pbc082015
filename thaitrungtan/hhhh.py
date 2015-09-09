#su dung dictionary dem
print '''
   chuong trinh dem so lan xuat hien cua cac 
   chuoi do ng dung nhap vao
   '''



D = {}
for i in  range(10):
	a = raw_input("nhap vao chuoi:")
	if (a == 'q' or a =='Q'):
		break
	else:
		v =D.get(a,0)
		v = v + 1
		D[a] = v
print ' ket qua sau khi tinh la:'
for k in D:
	print"chuoi %s da nhap %d lan"%(k, int(D[k]))


