#hungld
'''
-----------------------------------
Bai toan thay the ky tu trong chuoi
-----------------------------------
'''
s="The most common text encodings for SMS text (user data) are GSM encoding (7bits) and Unicode (16bits). GSM encoding is commonly used for Latin (English, German, Spanish, ...) text messages where GSM get each character is represented using 7bits only. The GSM encoding can map 128 Latin characters. So do you think we should use GSM network"
print "Chuoi ban dau:"
print s
print '''
'''
print "Chuoi sau khi thay the GSM bang CDMA 3 lan:"
print s.replace("GSM","CDMA",3)
