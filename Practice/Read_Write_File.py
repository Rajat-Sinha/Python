#Read and Write File

#write a file
fw = open('sample.txt','w')
fw.write('Hello Babes\n')
fw.write('This is for you')
fw.close()

#Read a file
fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()
