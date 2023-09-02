#Develop a program to sort the contents of a text file and write the sorted contents into a separate text file.

ifile = open('text.txt') 
ofile = open('otext.txt', mode = 'w') 
sentence = ifile.read() 
words sentence.split() 
words.sort() 
print (words) 
for word in words:
  ofile.write(word + " ")
ofile.close() 
