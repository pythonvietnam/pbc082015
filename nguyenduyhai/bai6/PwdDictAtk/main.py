#test checkPWD	
#haind

import PwdDictAtk

print "Thuc hien check file ZIP:"
PwdDictAtk.checkZip('lab.skype.pythonclass.zip','dictionaryAttk.haind')

print "Doc file Dictionary PWD"
PwdDictAtk.readPWD('lab.skype.pythonclass.zip','dictionaryAttk.haind')
