import os
file = open ('text2.txt','w')
file.write('buena')
file = open('text2.txt', 'r')
print (file.read())
os.remove('text.txt')



