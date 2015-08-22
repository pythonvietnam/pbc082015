#bai toan doan so
import random

solandoan = 0

print "Chao mung ban den voi tro choi Doan so. Ban ten la gi?"
name = raw_input()

print ('''Chao ''' + name + ''' toi vua doan mot con so
	Ban hay doan mot so ma ban cho do la binh phuong so toi vua doan''')

X = random.randint(1,20)
number = pow(X,2)

while solandoan < 4:
	print "Moi ban doan"
	B = input()

	B = int(B)
	solandoan = solandoan + 1

	if B < number:
		print "Ban phai doan mot so lon hon nua."
	elif B > number:
		print "Ban can phai doan mot so nho hon."
	else: break

if B == number:
	print "Xin chuc mung ban, ban la nguoi chien thang."
else:
	print "Rat tiec, ban da doan sai, so can phai doan la " + str(number) + ". Chuc ban may man lan sau."
