
import random
b=random.randint(1,5)
c= b*b
i=0
for i in range(5):
	i = i + 1
	a=input('Nhap mot so bat ky ban doan:')
	int(a)
	if c>a:
		print (' Ban doan cao len')
	elif c<a:
		print (' Ban doan nho xuong ')
	else: break
if c==a:
	print (' Ban da doan dung')

	
	







