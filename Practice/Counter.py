#Finding the most frequent item
from collections import  Counter

text = 'This Agreement contains important information regarding your rights with respect to the Site'\
       'and the Services, including your relationship with us, and include an arbitration provision '\
       'that may limit your ability to pursue claims against us in court. Please read them carefully'\
       'This This This This is me and cool'
word = text.split()
counter = Counter(word) #gives the nnumber of words appearing in a string
top_three = counter.most_common(3)
print(top_three
      )
