#bai toan doan so
import random 

X = random.randint(1,20)	#chon so ngau nhien tu 1 den 20
number = pow(X,2)

print "Moi ban doan"
B = input()
B = int(B)

while B != number :	#vong lap
	print "Moi ban doan lai:"
	B = input ()
	B = int(B)
	if B < number:
		print "Ban phai doan mot so lon hon nua."
	elif B > number:
		print "Ban can phai doan mot so nho hon."
	else:
		print "Chuc mung ban."
