import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import matplotlib as mpl
import pandas as pd
import pymongo
import pprint
from pymongo import MongoClient
from collections import defaultdict
import xlrd

client = MongoClient()
db = client.solarsystem
collection = db.sun
query={
	"authors":{"$exists": True},

}
projection={
	
	"authors":[],
}
rm =list(collection.find(query,projection))
x=[y['authors'] for y in rm]
di=defaultdict(list)
authorsIn=[]             #No. of authors
papersI=defaultdict(int) #No. of papers of an author

loc = ("C:\Users\Akanksha Chandna\Downloads\Indian_faculty.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
authorNameIn=[]
sheet.cell_value(3, 3)

for i in range(2,sheet.nrows):
    authorNameIn.append(sheet.cell_value(i,3))


for i in x:
	for k in i:
		if k not in authorsIn:
			authorsIn.append(k)
		papersI[k]=papersI[k]+1


for i in x:
	for k in i:
		for name in i:
			if name not in di[k] and name in authorNameIn:
				di[k].append(name)
				

degI=defaultdict(int)
for j in authorsIn:
	degI[j]=len(di[j])-1


countIn=defaultdict(int)
for name in authorNameIn:
	c=degI[name]
	countIn[c]=countIn[c]+1

print(countIn)
x1=[]
y1=[]
for key in countIn:
	if key!=0:
		x1.append(key)
		y1.append(countIn[key])



dbs = client.vehicle
collect = dbs.car
quer={
	"authors":{"$exists": True},

}
project={
	
	"authors":[],
}

rms =list(collect.find(quer,project))
z=[y['authors'] for y in rms]
wb = xlrd.open_workbook("C:\Users\Akanksha Chandna\Downloads\USA Faculties.xlsx")
sheet = wb.sheet_by_index(0)
 

sheet.cell_value(0, 0)

authorNameUs=[] 
for i in range(2,sheet.nrows):
    authorNameUs.append(sheet.cell_value(i,3))

du=defaultdict(list)
authors=[]
papersU=defaultdict(int)
for i in z:
	for k in i:
		if k not in authors:
			authors.append(k)
		papersU[k]=papersU[k]+1;

for i in z:
	for k in i:
		for name in i:
			if name not in du[k] and name in authorNameUs :
				du[k].append(name)
				

degU=defaultdict(int)
for x in authors:
	degU[x]=len(du[x])-1

 


countU=defaultdict(int)
for name in authorNameUs:
	c=degU[name]
	countU[c]=countU[c]+1

print(countU)

x2=[]
y2=[]
for key in countU:
	if key!=0:
		x2.append(key)
		y2.append(countU[key])

style.use('ggplot')
fig, axs = plt.subplots()

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=None)

plt.title('Collaboration of authors')
plt.ylabel('authors count')
plt.xlabel('Non-weighted Degree Count')
s1=len(x1)
s2=len(x2)
for i in range(0,s1):
	
	axs.scatter(x1[i],y1[i],s=np.pi*y1[i]*1.00,c='red')
for i in range(0,s2):
	axs.scatter(x2[i],y2[i],s=np.pi*y2[i]*1.00,c='blue')

plt.show()


