import matplotlib.pyplot as plt 
import pymongo
import pprint
from pymongo import MongoClient
from collections import defaultdict
import numpy as np
import matplotlib as mpl
from matplotlib import style
import xlrd
import math

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
degI=defaultdict(int)
dnWI=defaultdict(list)
degNwI=defaultdict(int)


loc = ("C:\Users\Akanksha Chandna\Downloads\Indian_faculty.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
authorNameIn=[]
sheet.cell_value(3, 3)

for i in range(2,sheet.nrows):
    authorNameIn.append(sheet.cell_value(i,3))


for i in x:
	for k in i:
		for name in i:
			if name!=k and name in authorNameIn:
				di[k].append(name)										#weighted degree
			if name not in dnWI[k] and name in authorNameIn:
				dnWI[k].append(name)									#non weighted degree
	
for name in authorNameIn:
	degI[name]=len(di[name])
	degNwI[name]=len(dnWI[name])-1



countIn=defaultdict(int)

for name in authorNameIn:
	if degNwI[name]!=0:
		c=(degI[name])/(degNwI[name])
		if c!=0:
			countIn[c]=countIn[c]+1

print(countIn)

x1=[]
y1=[]
for key in countIn:
	x1.append(key)
	y1.append(countIn[key])



db = client.vehicle
collection = db.car
query={
	"authors":{"$exists": True},
	

}
projection={
	
	"authors":[],
}
rm =list(collection.find(query,projection))
x=[y['authors'] for y in rm]
wb = xlrd.open_workbook("C:\Users\Akanksha Chandna\Downloads\USA Faculties.xlsx")
sheet = wb.sheet_by_index(0)
 
sheet.cell_value(0, 0)
authorNameUs=[] 
for i in range(2,sheet.nrows):
    authorNameUs.append(sheet.cell_value(i,3))


du=defaultdict(list)
degU=defaultdict(int)
dnWU=defaultdict(list)
degNwU=defaultdict(int)

for i in x:
	for k in i:
		for name in i:
			if name!=k and name in authorNameUs:
				du[k].append(name)
			if name not in dnWU[k] and name in authorNameUs:
				dnWU[k].append(name)

for name in authorNameUs:
	degU[name]=len(du[name])
	degNwU[name]=len(dnWU[name])-1





countUS=defaultdict(int)
for name in authorNameUs:
	if degNwU[name]!=0:
		c=degU[name]/degNwU[name]
		if c!=0:
			countUS[c]=countUS[c]+1

x2=[]
y2=[]
for key in countUS:
	x2.append(key)
	y2.append(countUS[key])

print(countUS)

style.use('ggplot')
fig, axs = plt.subplots()

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=None)

plt.title('Collaboration of authors')
plt.ylabel('authors count')
plt.xlabel('Average Weighted Degree Count')
s1=len(x1)
s2=len(x2)
for i in range(0,s1):
	
	axs.scatter(x1[i],y1[i],s=np.pi*y1[i]*1.25,c='red')
for i in range(0,s2):
	axs.scatter(x2[i],y2[i],s=np.pi*y2[i]*1.25,c='blue')

plt.show()
