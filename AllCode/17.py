#Read and Write a file

#write a file
fw = open('sample.txt','w')
fw.write('Hey This is me\n')
fw.write('Hey What"s up guyss\n')
fw.close()

#Read a file
fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()