#BT ve Dictionary
#CRUD ( create, read, update,delete)

# dict = { 'Name': 'Vu Manh Cuong', 'Age': '25', 'Year': '1990'}
# print "Length:%d" %len(dict)
# print "Chuoi:%s" %str(dict)

# word = raw_input("Press to char:")
# d = {'char': word}
# print "Display string:%s" %str(d)

#dict = { 'Name': 'cuong', 'Name1':'Binh', 'Name2': 'Chien'}
#print "Display:%s" %dict

#a = raw_input ("Press string:")
#b = dict["Name"]

#print "Name 1:%s" %b
#if a == b:
#	print "ok"
#else:
#	print "not ok"
d = {}
for i in range(1,10):
	b = raw_input ("Press string:")
	if (b == 'Q' or b == 'q'):
		break
	else:
		v = d.get(b,0)
		v = v + 1
		d[b] = v
print d
#	for k in d:
#		print "So %s lan chuôi %d:" %(k, int(d[k]))


