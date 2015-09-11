# Tupples
# T = (a,b,c)
#Gan tupple ko can dau ngoac

###n:10,anh:11,dt:5,tra:15,15(5:2:2:3:3)

print "Chuoi can tach: fromXwithLove: I love Python. Send email to loitd@pythonvietnam.info"
str = "fromXwithLove: I love Python. Send email to loitd@pythonvietnam.info"

#cut lay chuoi nguoi gui
str1 = str.split(':',1)
#cut lay ten nguoi gui
str2 = str1[0].split('m')
print "From people: %s"%str2[1]

#Cut lay noi dung cua mail
body = str1[1].split('.')
print "Content:%s"%(body[0])

#Lay dia chi mail
mail = str1[1].split()
print "From mail:%s"%mail[6]