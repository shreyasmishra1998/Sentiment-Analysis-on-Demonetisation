import csv
import codecs
import matplotlib.pyplot as plt
from afinn import Afinn
import numpy as np
afinn = Afinn()
#Sentiment values
positive=0
negative=0
neutral=0
total=0
# reading csv file
filepath = "Demonetisation Tweets.csv"
with codecs.open(filepath,"r") as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]
i = 0
j = 0
x = 0
y = 0
z = 0
avg = 0
pcount = 0
ncount = 0
neutral = 0

plist = []
nlist = []
nnlist = []
pid = []
nid = []
nnid = []
x = (np.shape(data))
print (x)
print (x[0])
aa = []
bb = []
while (i<x[0]):
    
    print("Sentiment of tweet",i," = ",afinn.score((data[i][1])))
    y = afinn.score((data[i][1]))
    z = z + y
    if(y>0):
        plist.append(y)
        
        pcount = pcount + 1
        
    elif(y<0):
        
        nlist.append(y)
        ncount = ncount + 1
        
    elif(y == 0):
        
        neutral = neutral + 1        
    if(i<(x[0]-1)):
        i = i + 1
    else:
        break
  
print("Number of Positive Sentiments: ",pcount)
print("Number of Negative Sentiments: ",ncount)
print("Number of Neutral Sentiments: ",neutral)

# Pie chart
labels = ['Positive', 'Negative', 'Neutral']
sizes = [pcount,ncount,neutral]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')
plt.tight_layout()
plt.show()

index = np.arange(len(labels))
plt.bar(index,sizes)
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.xticks(index, labels, rotation=0)
plt.title('Sentiment Analysis for Demonetisation Tweets')
plt.show()
if(pcount>ncount):
    print("General Sentiment regarding Demonetisation is Generally Positive")
elif(ncount>pcount):
    print("General Sentiment regarding Demonetisation is Generally Negative")
    