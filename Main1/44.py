#Finding the most frequent items

from collections import Counter
text = 'This Agreement contains important information regarding your rights with respect to the Site'\
       'and the Services, including your relationship with us, and include an arbitration provision '\
       'that may limit your ability to pursue claims against us in court. Please read them carefully'\
       'This This This This is me and cool'

words = text.split()
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
