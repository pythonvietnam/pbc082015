#bai toan doan so
import random 

X = random.randint(1,20)	#chon so ngau nhien tu 1 den 20
number = pow(X,2)
	
for B in range(10) :	#vong lap, de thuc hien doan dc 4 lan
	print "Moi ban doan"
	B = input()
	B = int(B)

	if B < number:
		print "Ban phai doan mot so lon hon nua."
	elif B > number:
		print "Ban can phai doan mot so nho hon."
	else: break

if B == number:
	print "Xin chuc mung ban, ban la nguoi chien thang."
else:
	print "Rat tiec, ban da doan sai, so can phai doan la " + str(number) + ". Chuc ban may man lan sau."
