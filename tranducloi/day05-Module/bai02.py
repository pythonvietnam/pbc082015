#loitd
#python
# su dung bien toan cuc va bien cuc bo

global motd 
motd = "I am the global"
mitd = "am I another global?"

def f1(motd=""):
	print motd
	print mitd

def f2(mitd=""):
	global motd
	print motd
	print mitd

if __name__ == '__main__':
	f1("I am the arg")
	f2("I am the arg")
	print motd
	print mitd